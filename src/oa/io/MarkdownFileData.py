from src.oa.io.FileData import FileData
from src.oa.converters.ConverterMarkdown2HTML import ConverterMarkdown2HTML

import logging
import frontmatter

logger = logging.getLogger('root')

class MarkdownFileData (FileData):

    def __init__(self, path, name):
        super().__init__(path, name)

    # def __init__(self, fileData):
    #     super().__init__(fileData.path, fileData.name)
    #     self.contents = fileData.contents

    def loadContents(self):
        # Read the front matter
        data = frontmatter.load(self.getFullPath())
        
        # print(frontmatter.dumps(data))
        
        # Load the raw contents
        if(data.content):
            self.contents = data.content
        
        # Load the properties
        if(data.keys()):
            self.addProperties(data.metadata)

        # Process contents
        ## TODO

        # Render the contents to HTML
        if(self.getContents()):
            converter = ConverterMarkdown2HTML(self.getContents())
            html = converter.convert()
        
            self.setRenderedContents(html)