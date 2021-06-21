import chevron
import logging
import os

from src.oa.io.FileData import FileData
from src.oa.io.MarkdownFileData import MarkdownFileData
from src.oa.io.DirectoryData import DirectoryData
from src.oa.io.writer.OAWriter import OAWriter

logger = logging.getLogger('root')

# TODO: tercerizar manejo de rutas
# TODO: tercerizar la genración?


class OAGenerator:
    def __init__(self, metadata, writer, theme, entries):
        self.metadata = metadata
        self.writer = writer
        self.theme = theme
        self.entries = entries

    def generate(self, level=0, localEntries=None, theme=None, template=None):
        rootDirectory = False
        indexPresent = False

        if(not localEntries):
            rootDirectory = True
            localEntries = self.entries

        if(not theme):
            theme = self.theme

        if(not template):
            template = "index.html"

        ###################################################################

        # TODO: still to test
        localEntries.sort()

        if(not self.directoryHasIndex(localEntries)):
            indexPresent = True

        for entry in localEntries:
            if(isinstance(entry, FileData) or
               isinstance(entry, DirectoryData)):

                data = {
                    "head-base": self.generateHeadBase(level),
                    "content": self.generateContent(entry),
                    # TODO: caché
                    "items": self.generateItems(self.entries),
                    "breadcrumbs": self.generateBreadcrumbs(entry),
                    "header": self.generateHeader(),
                    "footer": self.generateFooter()
                }

                content = self.renderTemplate(theme, template, data)

                self.writer.write(entry, content)

            if(isinstance(entry, DirectoryData)):
                self.generate(level+1, entry.getEntries())

    def directoryHasIndex(self, localEntries):
        for entry in localEntries:
            if(entry.getName().lower() == "index.md"):
                if(isinstance(entry, DirectoryData)):
                    logger.warning(
                        f"Directory [{entry.getFullPath()}] may conflict by its name")
                    return True
                if(isinstance(entry, FileData)):
                    return True

        return False

    def renderTemplate(self, theme, template, data):
        templateFile = os.path.join('themes', theme, template)

        try:
            templateContents = open(templateFile, 'r')
        except FileNotFoundError:
            logger.error(
                f"Template file [{templateFile}] was not found, ignoring render")
            return None

        return chevron.render(templateContents, data)

    def generateHeadBase(self, level):
        base = "../" * (level)
        return base

    def generateBreadcrumbs(self, entry):
        if(isinstance(entry, DirectoryData)):
            parent = entry
        else:
            parent = entry.getParent()

        breadcrumbs = []

        # Add parent breadcrumbs if available

        if(parent):
            while(parent != None):
                path, filePath = OAWriter.createEntryPath(parent)
                
                crumb = {
                    "name": parent.getName(),
                    "hint": parent.getName(),
                    "url": filePath
                }
                
                breadcrumbs.append(crumb)

                parent = parent.getParent()

        # Add root's breadcrumb (OA)

        path, filePath = OAWriter.createEntryPath(self.entries[0])

        crumb = {
            "name": "OA",
            "hint": "Raíz",
            "url": filePath
        }
        
        breadcrumbs.append(crumb)

        return breadcrumbs[::-1]

    def generateType(self, entry):
        if isinstance(entry, FileData):
            return "page"
        elif isinstance(entry, DirectoryData):
            return "folder"

        return "unknown"

    def generateItems(self, localEntries):
        items = []

        for entry in localEntries:
            path, filePath = OAWriter.createEntryPath(entry)

            item = {
                "name": entry.getProperty('name'),
                "hint": entry.getProperty('hint') or entry.getProperty('name'),
                "url": filePath,
                "type": self.generateType(entry),
                "icon": "file" if self.generateType(entry) == "page" else "folder"
            }
            
            items.append(item)

        return items

    def generateContent(self, entry):
        if(isinstance(entry, FileData)):
            return entry.getRenderedContents()

        elif(isinstance(entry, DirectoryData)):
            return self.generateDirectoryContent(entry)

        else:
            logger.error(f"Entry [{entry.getFullPath()}] has an unknown type")
            return "*** Unknown contents ***"

    def generateDirectoryContent(self, directoryEntry):
        elements = self.generateItems(directoryEntry.getEntries())

        data = {
            "elements": elements
        }

        content = self.renderTemplate(
            theme=self.theme, template="directory_listing.html", data=data)

        return content

    def generateHeader(self):
        defaultTitle = "The most interesting learning object"
        defaultSubtitle = "Create a \"_metadata.md\" file to customize this messages"

        # TODO: change logo por defecto (true con imagen default)

        path, filePath = OAWriter.createEntryPath(self.entries[0])

        data = {
            "show": self.metadata.getProperty("header-show") if self.metadata.hasProperty("header-show") else True,
            "logo": self.metadata.getProperty("header-logo") if self.metadata.hasProperty("header-logo") else True,
            "title": self.metadata.getProperty("header-title") if self.metadata.hasProperty("header-title") else defaultTitle,
            "subtitle": self.metadata.getProperty("header-subtitle") if self.metadata.hasProperty("header-subtitle") else defaultSubtitle,
            "link": filePath
        }

        return data

    def generateFooter(self):
        # TODO: improve default message with version
        defaultMessage = "Generated with OACreator"

        data = {
            "show": self.metadata.getProperty("footer-show") if self.metadata.hasProperty("footer-show") else True,
            "message": self.metadata.getProperty("footer-message") if self.metadata.hasProperty("footer-message") else defaultMessage
        }

        return data
