from map_site_extraction import map
from scrapper import scrape
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python script.py <filepath>")
        sys.exit(1)

    filepath = sys.argv[1]

    try:
        urls = []
        with open(f"{filepath}/site_map.txt", 'r') as file:
            for line in file:
              line = line.strip()
              urls = map(line)
              outputname = line.split('/')[-1].split('.')[0]
              # print(outputname)
              
              with open(f"{filepath}/{outputname}.txt", 'a') as file:
                      for url in urls:
                          reuslt = scrape(url)
                          file.write(f"{url}\n")
                          for tag in reuslt:
                              file.write(f"{tag.text.strip()}\n")
                          file.write("\n")
    except FileNotFoundError:
        print(f"The file {filepath} was not found.")
        sys.exit(1)

if __name__ == "__main__":
    main()