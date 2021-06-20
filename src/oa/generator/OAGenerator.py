import chevron
import logging
from os.path import join

from src.oa.io.FileData import FileData
from src.oa.io.MarkdownFileData import MarkdownFileData
from src.oa.io.DirectoryData import DirectoryData

logger = logging.getLogger('root')

class OAGenerator:
    def __init__(self, writer, theme, entries):
        self.writer = writer
        self.theme = theme
        self.entries = entries
        
    def generate(self, entries = None):
        if(not entries):
            entries = self.entries
        
        # TODO: still to test
        entries.sort()
        
        for entry in entries:
            if(isinstance(entry, FileData)):
                # TODO: fix this!
                
                template = open(join('themes', self.theme, 'index.html'), 'r')
                content = chevron.render(template, {'mustache': 'World'})

                self.writer.write(entry, content)
    
            if(isinstance(entry, DirectoryData)):
                self.generate(entry.getEntries())