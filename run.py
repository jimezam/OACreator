################################################

# Set the application's logger

import log

logger = log.setup_custom_logger('root')

################################################

import src.oa.io.reader.oa_reader as reader
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
    
    entryList = reader.list(inputPath, recursive=True, sort=True)

    # reader.printList(entryList)
    
    ############################################

    # Process the entries and save the products

    processor.process(entryList, outputPath)

    ############################################

################################################

if __name__ == "__main__":
    main()
    
################################################