from site_map_extraction import map
from scrapper import scrape
import sys
import time
import logging

def setup_logging(filepath):
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(levelname)s - %(message)s',handlers=[logging.FileHandler(f'{filepath}/logs.log'),logging.StreamHandler()])

def main():
    start_time = time.time()
    if len(sys.argv) != 2:
        print("Usage: python script.py <filepath>")
        sys.exit(1)

    filepath = sys.argv[1]
    setup_logging(filepath)
    try:
        with open(f"{filepath}/site_map", 'r') as file:
           sitemap_index = file.readline().strip()
        urls = map(sitemap_index)
        
        #index
        for key, value in urls.items():
            with open(f"{filepath}/index.txt", 'a') as file:
                file.write(f"{key}: {len(value)} Entries\n")
                for url in value:
                    file.write(f"{url}\n")
                file.write("\n")
        
        #scraping        
        for key, value in urls.items():
            outputname = key
            logging.info(f"Scraping {outputname}...")
            with open(f"{filepath}/{outputname}.txt", 'a') as file:
                    for url in value:
                        reuslt = scrape(url)
                        file.write(f"{url}\n")
                        for tag in reuslt:
                            file.write(f"{tag.text.strip()}\n")
                        file.write("\n")
    except FileNotFoundError:
        logging.error(f"The file {filepath} was not found.")
        sys.exit(1)
        
    end_time = time.time()
    logging.info(f"Finish Scrapping in: {end_time - start_time} seconds.")
if __name__ == "__main__":
    main()