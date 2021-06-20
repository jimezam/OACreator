from src.oa.io.EntryData import EntryData

import logging

logger = logging.getLogger('root')

class FileData (EntryData):

    def __init__(self, path, name):
        super().__init__(path, name)
    
        self.contents = None
        self.renderedContents = None

    def setContents(self, contents):
        self.contents = contents

    def setRenderedContents(self, contents):
        self.renderedContents = contents

    def loadContents(self):
        logger.error("This is method is not implemented in this class!")
        
    def getContents(self):
        return self.contents
    
    def getRenderedContents(self):
        return self.renderedContents