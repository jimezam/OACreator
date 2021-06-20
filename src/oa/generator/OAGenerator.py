import logging

logger = logging.getLogger('root')

class OAGenerator:
    def __init__(self, writer, entries):
        self.writer = writer
        self.entries = entries
        
    def generate(self):
        self.sort()
    
    def sort(self):
        # TODO: still to test
        self.entries.sort()