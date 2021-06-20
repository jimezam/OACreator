from os.path import join

import logging

logger = logging.getLogger('root')

class EntryData:

    def __init__(self, path, name):
        self.path = path
        self.name = name
        self.properties = {}

    def __str__(self):
        return f"path: {self.path}; name: {self.name}\n"

    def getFullPath(self):
        return join(self.path, self.name)

    def setProperties(self, properties):
        self.properties = properties

    def __eq__(self, other):
        return self.getFullPath() == other.getFullPath()

    def __lt__(self, other):
        if(not self.hasSpecialOrderedFilename()):
            return self.getFullPath() < other.getFullPath()

        return self.getIndexOrderedFilename() < other.getIndexOrderedFilename()

    def getProperties(self):
      return self.properties

    def getProperty(self, name):
      return self.properties[name]

    def hasProperty(self, name):
      return name in self.properties

    def hasSpecialOrderedFilename(self):
        tokens = self.name.split()
        return tokens[0].isdigit()

    def getIndexOrderedFilename(self):
        tokens = self.name.split()
        return int(tokens[0])
      
    def getNameWithoutIndexOrdered(self):
      if(not self.hasSpecialOrderedFilename()):
        return self.name
      
      index = self.getIndexOrderedFilename()
      
      return self.name[len(f"{index}"):].strip()
