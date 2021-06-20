################################################

# Set the application's logger

import log

logger = log.setup_custom_logger('root')

################################################

from src.oa.io.reader.ResourcesLocator import ResourcesLocator

import src.oa.processor.oa_processor as processor

################################################

def main():
    ############################################
    
    # Define input requirements
    
    logger.info("Running main ...")

    inputPath = "./input"
    outputPath = "./output"
    
    ############################################

    # Get the entries available
    
    locator = ResourcesLocator()
    
    entryList = locator.list(inputPath, recursive=True)

    locator.printList(entryList)
    
    ############################################

    # Process the entries and save the products

    # processor.process(entryList, outputPath)

    ############################################

################################################

if __name__ == "__main__":
    main()
    
################################################ 