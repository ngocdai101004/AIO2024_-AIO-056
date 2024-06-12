import gdown
import re


def count_word(file_path):
    words_list = {}
    with open(file_path, 'r', encoding='utf-8') as f:
        for line in f:
            line = line.lower()

            words = re.findall(r'\b\w+\b', line)
            for word in words:
                if word in words_list:
                    words_list[word] += 1
                else:
                    words_list[word] = 1

    return dict(sorted(words_list.items(), key=lambda item: item[1]))


if __name__ == "__main__":
    url = 'https://drive.google.com/uc?id=1IBScGdW2xlNsc9v5zSAya548kNgiOrko'
    output = 'file.txt'
    gdown.download(url, output, quiet=False)
    print("File downloaded successfully!")
    file_path = 'file.txt'
    print(count_word(file_path)['man'])
