################################################

# Set the application's logger

import log

logger = log.setup_custom_logger('root')

################################################

from src.oa.io.reader.EntriesLocator import EntriesLocator
from src.oa.processor.EntriesProcessor import EntriesProcessor
from src.oa.io.writer.OAWriter import OAWriter
from src.oa.generator.OAGenerator import OAGenerator

################################################

def main():
    ############################################
    
    ## Define input requirements
    
    logger.info("Running main ...")

    inputPath = "./input"
    outputPath = "./output"
    
    ############################################

    ## Get the available entries
    
    locator = EntriesLocator()
    
    entryList = locator.list(inputPath, recursive=True)

    # locator.printList(entryList)
    
    ############################################

    ## Process the entries (render them)

    processor = EntriesProcessor()

    processor.process(entryList)

    # locator.printList(entryList)

    ############################################
    
    ## Generate the OA
    
    writer = OAWriter(inputPath, outputPath)
    generator = OAGenerator(writer, entryList)
    
    generator.generate()
    
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