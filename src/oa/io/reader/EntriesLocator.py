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
        
    def list(self, path, recursive=True):
        entries = []
        
        for entry in listdir(path):
            entry_path = join(path, entry)
            
            obj = None        
            
            if(isfile(entry_path)):
                extension = splitext(entry)[1]
                
                if(extension == ".md" or extension == ".MD"):      # markdown
                    obj = MarkdownFileData(path, entry)
                else:
                    logger.warning(f"Not source file [{entry_path}] will be ignored.")
            
            if(isdir(entry_path) and recursive):
                obj = DirectoryData(path, entry)

                directoryEntries = self.list(obj.getFullPath(), recursive)
                    
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
            # if(isinstance(entry, MarkdownFileData)):
            #     print(">> [" + str(entry.getRenderedContents()) + "]")
