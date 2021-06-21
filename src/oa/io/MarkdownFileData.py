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
        data = frontmatter.load(self.getFullPath())
        
        # print(frontmatter.dumps(data))
        
        if(data.content):
            self.contents = data.content
        
        if(data.keys()):
            self.addProperties(data.metadata)

        # Process contents
        ## TODO

        # Convert it to HTML
        converter = ConverterMarkdown2HTML(self.getContents() or '')
        html = converter.convert()
        
        self.setRenderedContents(html)