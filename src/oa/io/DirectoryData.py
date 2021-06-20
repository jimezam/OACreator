from src.oa.io.EntryData import EntryData

class DirectoryData (EntryData):

    def __init__(self, path, name):
        super().__init__(path, name)
        self.entries = []
        
    def addEntry(self, entry: EntryData):
        self.entries.append(entry)
        
    def setEntries(self, entries):
        self.entries = entries
        
    def __str__(self):
        response = f"path: {self.path}; name: {self.name}; entries: \n"
        
        for entry in self.entries:
            response += str(entry)
            
        return response