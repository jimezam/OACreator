import chevron
import logging
import os

from src.oa.io.FileData import FileData
from src.oa.io.MarkdownFileData import MarkdownFileData
from src.oa.io.DirectoryData import DirectoryData
from src.oa.io.writer.OAWriter import OAWriter

logger = logging.getLogger('root')

class OAGenerator:
    def __init__(self, metadata, writer, theme, entries):
        self.metadata = metadata
        self.writer = writer
        self.theme = theme
        self.entries = entries
        
    def generate(self, entries = None, theme = None, template = None):
        if(not entries):
            entries = self.entries
        
        if(not theme):
            theme = self.theme
        
        if(not template):
            template = "index.html"
        
        # TODO: still to test
        entries.sort()
        
        for entry in entries:
            if(isinstance(entry, FileData) or 
               isinstance(entry, DirectoryData)):
                                
                data = {
                    "content": self.generateContent(entry),
                    "items": self.generateItems(entries),
                    "breadcrumbs": self.generateBreadcrumbs(entry),
                    "header": self.generateHeader(),
                    "footer": self.generateFooter()
                }

                content = self.renderTemplate(theme, template, data)

                self.writer.write(entry, content)
    
            # TODO: problemas cuando se genera al interior de los "folder" -> breadcrumb
    
            if(isinstance(entry, DirectoryData)):
                self.generate(entry.getEntries())
    
    def renderTemplate(self, theme, template, data):
        templateFile = os.path.join('themes', theme, template)
        
        try:
            templateContents = open(templateFile, 'r')
        except FileNotFoundError:
            logger.error(f"Template file [{templateFile}] was not found, ignoring render")
            return None
        
        return chevron.render(templateContents, data)
    
    def generateBreadcrumbs(self, entry):
        breadcrumbs = []
        levels = ["OA"] + os.path.normpath(entry.getFullPath()).split(os.sep)[1:-1]
        
        path = ["."]
        url = "#"
        
        # TODO: breadcrumbs URLs
        
        for level in levels:
            if(level == "OA"):
                url = "./#"
            else:
                path.append(os.path.join(path[-1] or "", level))
                url = os.path.join(path[-2], level+".html")
            
            # print(path)
            # print(url)
            # print(level)
            
            crumb = {
                "name": level,
                "hint": level,
                "url": url
            }
            
            breadcrumbs.append(crumb)
        return breadcrumbs
    
    def generateType(self, entry):
        if isinstance(entry, FileData):
            return "page"
        elif isinstance(entry, DirectoryData):
            return "folder"
            
        return "unknown"

    def generateItems(self, entries):
        items = []
        
        for entry in entries:            
            path, filePath = OAWriter.createEntryPath("", entry)
            
            item = {
                "name": entry.getProperty('name'),
                "hint": entry.getProperty('hint') or entry.getProperty('name'),
                "url": filePath,
                "type": self.generateType(entry)
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
        
        content = self.renderTemplate(theme=self.theme, template="directory_listing.html", data=data)
        
        return content

    def generateHeader(self):
        defaultTitle = "The most interesting learning object"
        defaultSubtitle = "Create a \"_metadata.md\" file to customize this messages"

        # TODO: change logo por defecto (true con imagen default)

        data = {
            "show": self.metadata.getProperty("header-show") if self.metadata.hasProperty("header-show") else True,
            "logo": self.metadata.getProperty("header-logo") if self.metadata.hasProperty("header-logo") else True,  
            "title": self.metadata.getProperty("header-title") if self.metadata.hasProperty("header-title") else defaultTitle,
            "subtitle": self.metadata.getProperty("header-subtitle") if self.metadata.hasProperty("header-subtitle") else defaultSubtitle
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