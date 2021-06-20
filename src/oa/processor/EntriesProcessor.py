from os import path
import logging
from os.path import join

from src.oa.io.FileData import FileData
from src.oa.io.MarkdownFileData import MarkdownFileData
from src.oa.io.DirectoryData import DirectoryData
from src.oa.converters.ConverterMarkdown2HTML import ConverterMarkdown2HTML

logger = logging.getLogger('root')

class EntriesProcessor:
    # def __init__(self):
    #     pass

    def process(self, entries):
        for entry in entries:
            if(isinstance(entry, FileData)):
                if(isinstance(entry, MarkdownFileData)):      # markdown
                    try:
                        self.processMarkdownFile(entry)                    
                    except Exception as e:
                        entries.remove(entry)
                        logger.warning(f"Source file [{entry.getFullPath()}] {e}, will be ignored.")    
                else:
                    logger.warning(f"Source file [{entry.getFullPath()}] with no supported type, will be ignored.")

            if(isinstance(entry, DirectoryData)):
                # TODO
                logger.error(f"Process a directory IS NOT IMPLEMENTED yet!")
    
    def processMarkdownFile(self, entry):
        # Read front matter / Read contents
        entry.loadContents()

        if(entry.getContents()==None):
            raise Exception('has no contents')

        # Process contents
        ## TODO

        # Convert it to HTML
        converter = ConverterMarkdown2HTML(entry.getContents() or '')
        html = converter.convert()
        
        entry.setRenderedContents(html)
        
        return html