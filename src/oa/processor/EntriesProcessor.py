import logging

from src.oa.io.FileData import FileData
from src.oa.io.DirectoryData import DirectoryData

logger = logging.getLogger('root')


class EntriesProcessor:
    # def __init__(self):
    #     pass

    def process(self, entries, metadata, parent = None):
        markedForRemoval = []
        
        for entry in entries:
            if(isinstance(entry, FileData)):
                entry.loadContents()
                
                if(entry.getName().lower() == "_metadata.md"):
                    if(parent):                             # inside a directory
                        parent.addProperties(entry.getProperties())
                    else:                                   # root (project's metadata)
                        metadata.addProperties(entry.getProperties())

                    markedForRemoval.append(entry)
                else:
                    if(entry.getContents() == None):
                        logger.warning(
                            f"Source file [{entry.getFullPath()}] has no contents, will be ignored.")
                        markedForRemoval.append(entry)

            if(isinstance(entry, DirectoryData)):
                self.process(entry.getEntries(), metadata, parent = entry)

        for marked in markedForRemoval:
            entries.remove(marked)