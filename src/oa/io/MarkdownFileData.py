from src.oa.io.FileData import FileData

import logging
import frontmatter

logger = logging.getLogger('root')

class MarkdownFileData (FileData):

    def __init__(self, path, name):
        super().__init__(path, name)

    def __init__(self, fileData):
        super().__init__(fileData.path, fileData.name)
        self.contents = fileData.contents

    def loadContents(self):
        data = frontmatter.load(self.getFullPath())
        
        # print(frontmatter.dumps(data))
        
        if(data.content):
            self.contents = data.content
        
        if(data.keys()):
            self.setProperties(data.metadata)

    # def getProperty(self, name):
    #   print(type(self.properties))