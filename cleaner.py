import sys

def main():
    filename = sys.argv[1]
    with open(filename, 'r') as file:
        text = file.read()
    cleaned_text = clean_text(text)
    
    cleaned_filename = f"{filename}-cleaned"
    with open(cleaned_filename, 'w') as file:
        file.write(cleaned_text)
        
def clean_text(text):
    # Clean up duplicate lines and remove url lines for language model maximum length
    seen = set()
    unique_lines = []
    for line in text.splitlines():
        if line.startswith("http"):
            continue
        if line not in seen:
            seen.add(line)
            unique_lines.append(line)
    
    cleaned_text = "\n".join(unique_lines)
    return cleaned_text

if __name__ == "__main__":
    main()