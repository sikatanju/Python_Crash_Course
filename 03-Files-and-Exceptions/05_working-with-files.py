# ** Text file for now

# *** We could also analyze text file: 

# * For example, let's count the words in `multi-line.txt` file

from pathlib import Path

def count_words(path):

    path = Path(path)

    try:
        content = path.read_text(encoding='utf-8')

    except FileNotFoundError:
        print("File Not found in the specified locatoin")

    else:    
        words = content.split()
        # print(f'Word len of the given path `{path}` : {len(words)}')
        return len(words)
    
# * Let's we needed to find several file's word length:

file_names = ['single-line.txt', 'multi-line.txt', 'pi_digits.txt']

for name in file_names:
    path = Path(f'contents/{name}')
    print(f"Word len of the given path `{path}` : {count_words(path)}")

    
