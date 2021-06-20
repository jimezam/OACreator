import logging
import os
from functools import reduce

logger = logging.getLogger('root')

class OAWriter:
    def __init__(self, inputPath, outputPath):
        self.inputPath = inputPath
        self.outputPath = outputPath
        
    def write(self, entry, content):
        # Split the entry's full path
        sourcePath = os.path.normpath(entry.getFullPath()).split(os.sep)
        
        # Get the "real" name of the entry
        if(entry.hasProperty('name')):
            filename = entry.getProperty('name')
        else:
            filename = sourcePath[-1]
        
        # Get the filename with no extension
        filenameNoExtension = os.path.splitext(filename)[0]
        
        # Get the output's full path
        path = self.outputPath
        
        if(sourcePath[1:-1]):
            path = os.path.join(path, reduce(os.path.join, sourcePath[1:-1]))
        
        # Create the output's directory structure for the entry
        if not os.path.exists(path):
            os.makedirs(path)
            
        path = os.path.join(path, filenameNoExtension+".html")
            
        # Write the entry contents
            
        file = open(path, 'w')
        file.write(content)
        file.close()