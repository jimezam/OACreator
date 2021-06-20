from os.path import join
import sys
import logging

logger = logging.getLogger('root')

class EntryData:

    def __init__(self, path, name):
        self.path = path
        self.name = name
        self.properties = {
            "weight": sys.maxsize
        }

    def __str__(self):
        return f"path: {self.path}; name: {self.name}\n"

    def getFullPath(self):
        return join(self.path, self.name)

    def setProperties(self, properties):
        self.properties = properties

    def getProperties(self):
      return self.properties

    def getProperty(self, name):
        if (not self.hasProperty(name)):
            return None
        
        return self.properties[name]

    def hasProperty(self, name):
      return name in self.properties

    # Overiding magic methods for relational operators
  
    def __eq__(self, other):
        return self.getProperty("weight") == other.getProperty("weight")

    def __ne__(self, other):
        return self.getProperty("weight") != other.getProperty("weight")

    def __lt__(self, other):
        return self.getProperty("weight") < other.getProperty("weight")

    def __gt__(self, other):
        return self.getProperty("weight") > other.getProperty("weight")

    def __le__(self, other):
        return self.getProperty("weight") <= other.getProperty("weight")

    def __ge__(self, other):
        return self.getProperty("weight") >= other.getProperty("weight")
