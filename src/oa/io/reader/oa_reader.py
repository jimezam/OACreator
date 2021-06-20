from genericpath import isdir
from os import listdir
from os.path import isfile, join

from src.oa.io.FileData import FileData
from src.oa.io.DirectoryData import DirectoryData

def list(path, recursive=True):
    elements = []

    for entry in listdir(path):
        entry_path = join(path, entry)
        
        read = None        
        
        if(isfile(entry_path)):
            read = FileData(path, entry)
            pass
        
        if(isdir(entry_path)):
            read = DirectoryData(path, entry)

            if(recursive):
                entries = list(read.getFullPath(), recursive)
                                
                read.setEntries(entries)
                
        elements.append(read)
        
    return elements

def printList(entries):
    for entry in entries:
        print(entry)