import logging

from src.oa.io.FileData import FileData
from src.oa.io.DirectoryData import DirectoryData

logger = logging.getLogger('root')


class EntriesProcessor:
    # def __init__(self):
    #     pass

    def process(self, entries):
        for entry in entries:
            if(isinstance(entry, FileData)):
                entry.loadContents()

                if(entry.getContents() == None):
                    logger.warning(
                        f"Source file [{entry.getFullPath()}] has no contents, will be ignored.")
                    entries.remove(entry)
            # TODO: falsos positivos con DIRECTORY
            else:
                logger.warning(
                    f"Source file [{entry.getFullPath()}] with no supported type, will be ignored.")

            if(isinstance(entry, DirectoryData)):
                self.process(entry.getEntries())
