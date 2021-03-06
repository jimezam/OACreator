from genericpath import isdir
from os import listdir
from os.path import isfile, join, splitext
import logging

from src.oa.io.MarkdownFileData import MarkdownFileData
from src.oa.io.DirectoryData import DirectoryData

logger = logging.getLogger('root')

class EntriesLocator:
    def __init__(self):
        pass
        
    def list(self, path, directory=None, recursive=True):
        entries = []
        
        for entry in listdir(path):
            entry_path = join(path, entry)
            
            obj = None        
            
            if(isfile(entry_path)):
                filename = splitext(entry)[0]
                extension = splitext(entry)[1]
                
                if(extension == ".md" or extension == ".MD"):      # markdown files
                    obj = MarkdownFileData(path, entry)   
                    obj.setParent(directory)                 
                else:
                    logger.warning(f"Not source file [{entry_path}] will be ignored.")
            
            if(isdir(entry_path) and recursive):
                obj = DirectoryData(path, entry)
                obj.setParent(directory)
                
                directoryEntries = self.list(obj.getFullPath(), obj, recursive)
                    
                if(len(directoryEntries) > 0):                                    
                    obj.setEntries(directoryEntries)
                else:
                    obj = None
                    logger.warning(f"Directory [{entry_path}] has no valid entries, will be ignored.")
                        
            if(obj):
                entries.append(obj)
            
        return entries

    def printList(self, entries):
        for entry in entries:
            print("> " + str(entry))
