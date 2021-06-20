from os import path
import logging
from os.path import join

from src.oa.io.FileData import FileData
from src.oa.io.MarkdownFileData import MarkdownFileData
from src.oa.io.DirectoryData import DirectoryData
from src.oa.converters.ConverterMarkdown2HTML import ConverterMarkdown2HTML

logger = logging.getLogger('root')

def process(entries, outputPath):
    for entry in entries:
        if(isinstance(entry, FileData)):
            extension = path.splitext(entry.name)[1]
            
            if(extension == ".md" or extension == ".MD"):      # markdown
                html = processMarkdownFile(entry)
            else:
                logger.warning(f"Not source file [{entry.getFullPath()}] will be ignored.")

            # if(not html):
            #     logger.warning(f"Source file [{entry.getFullPath()}] has no contents, will be ignored.")
            # else:
            #     name = entry.getProperty('name') if entry.hasProperty('name') else path.splitext(entry.getNameWithoutIndexOrdered())[0]
                
            #     writer.write(entry.path, outputPath, name, html)

        if(isinstance(entry, DirectoryData)):
            # TODO
            logger.error(f"Process a directory IS NOT IMPLEMENTED yet!")
            pass
    
def processMarkdownFile(entry):

    markdownEntry = MarkdownFileData(entry)

    # Read front matter
    # Read contents
    markdownEntry.loadContents()

    # Backpropagating the markdown's only properties
    entry.setProperties(markdownEntry.getProperties())

    # Process contents
    ## TODO

    # Convert it to HTML
    converter = ConverterMarkdown2HTML(markdownEntry.getContents() or '')
    html = converter.convert()
    
    return html