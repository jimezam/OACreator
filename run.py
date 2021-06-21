#!/usr/bin/env python

################################################

# Set the application's logger

import log

logger = log.setup_custom_logger('root')

################################################

from src.oa.io.EntryData import EntryData
from src.oa.io.reader.EntriesLocator import EntriesLocator
from src.oa.processor.EntriesProcessor import EntriesProcessor
from src.oa.io.writer.OAWriter import OAWriter
from src.oa.generator.OAGenerator import OAGenerator

################################################

def main():
    ############################################

    logger.info("Running main ...")
    
    ## Define input requirements

    inputPath = "./input"
    outputPath = "./output"
    
    ############################################

    logger.info("Locating entries ...")

    ## Get the available entries
    
    locator = EntriesLocator()
    
    entryList = locator.list(inputPath, recursive=True)

    # locator.printList(entryList)
    
    ############################################

    logger.info("Processing entries ...")

    metadata = EntryData(None, "metadata")

    ## Process the entries (render them)

    processor = EntriesProcessor()
    
    processor.process(entryList, metadata)

    # print(metadata.getProperties())
    # locator.printList(entryList)
    # print([str(item) for item in entryList])

    ############################################
    
    logger.info("Generating OA ...")
    
    ## Generate the OA
    
    writer = OAWriter(inputPath, outputPath)
    generator = OAGenerator(metadata, writer, "default", entryList)

    generator.generate()
    
    ############################################
    
################################################

if __name__ == "__main__":
    main()
    
################################################ 