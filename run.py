################################################

# Set the application's logger

import log

logger = log.setup_custom_logger('root')

################################################

from src.oa.io.reader.EntriesLocator import EntriesLocator
from src.oa.processor.EntriesProcessor import EntriesProcessor

################################################

def main():
    ############################################
    
    # Define input requirements
    
    logger.info("Running main ...")

    inputPath = "./input"
    outputPath = "./output"
    
    ############################################

    # Get the entries available
    
    locator = EntriesLocator()
    
    entryList = locator.list(inputPath, recursive=True)

    # locator.printList(entryList)
    
    ############################################

    # Process the entries and save the products

    processor = EntriesProcessor()

    processor.process(entryList)

    locator.printList(entryList)

    ############################################

                # if(not html):
                #     logger.warning(f"Source file [{entry.getFullPath()}] has no contents, will be ignored.")
                # else:
                #     name = entry.getProperty('name') if entry.hasProperty('name') else path.splitext(entry.getNameWithoutIndexOrdered())[0]
                    
                #     writer.write(entry.path, outputPath, name, html)

################################################

if __name__ == "__main__":
    main()
    
################################################ 