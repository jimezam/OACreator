import logging

logger = logging.getLogger('root')

class OAWriter:
    def __init__(self, inputPath, outputPath):
        self.inputPath = inputPath
        self.outputPath = outputPath
        
    # def write(self, inputPath, outputPath, entries):
    #     print(inputPath)
    #     print(outputPath)
