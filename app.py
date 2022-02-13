from pprint import pprint
import pandas as pd
import os
import re
import textcleaner as tc

keywords = {
    "Keitaro": "k",
    "Hiro": "hi",
    "Natsumi": "n",
    "Hunter": "hu",
    "Yoichi": "yi",
    "Yoshinori": "yo",
    "Yuri": "yu",
    "Taiga": "t",
    "Eduard": "e",
    "Lee": "l",
    "Seto": "s",
    "Felix": "f",
    "Aiden": "a",
    "Goro": "g",
    "William": "w",
    "Yuki": "y",
    "???": "d"
}

keywords_list = ""

not_allowed_words = ['#', 'null']

data = {
    'name': [],
    'line': []
}

log = ""


def convert_to_list(word):
    return (word.split())

camp_buddy_assets_dir = './'


def get_keywords(keywords_list=""):
    for root, dirs, files in os.walk(camp_buddy_assets_dir):
        for file in files:
            if file.endswith('.rpy'):

                with open(f'{camp_buddy_assets_dir}{file}') as script:
                    for line in script:
                        line = line.strip()
                        line_list = convert_to_list(line)
                        
                        # for word in line_list:
                        try:
                            word = line_list[0]
                            if len(word) == 1 or len(word) == 2:
                                if word not in keywords_list and word not in ['$']:
                                    keywords_list += f"{word}\n"
                                    print(f"kw: {word} | sample statement: {line}")
                        except:
                            pass
                        

    keywords_list_text = open("keywords_list.txt", "w")
    keywords_list_text.write(keywords_list)
    keywords_list_text.close()



def main(log=""):
    for root, dirs, files in os.walk(camp_buddy_assets_dir):
        for file in files:
            if file.endswith('.rpy'):

                with open(f'{camp_buddy_assets_dir}{file}') as script:
                    for line in script:
                        line = line.strip()
                        line_list = convert_to_list(line)

                        skip = False
                        for not_allowed_word in not_allowed_words:
                            if not_allowed_word in line_list:
                                skip = True
                                break

                        if skip == True:
                            continue

                        
                        for character in keywords:
                            keyword = keywords[character]
                            if keyword in line_list:
                                sentence_with_apostrophe = ' '.join(line_list[1:])
                                
                                if '{i}' in sentence_with_apostrophe:
                                    line = sentence_with_apostrophe[5:-6]
                                    print(line)
                                else:
                                    line = sentence_with_apostrophe[1:-1]
                                    print(line)

                                if len(line) > 0:

                                    data['name'].append(character)
                                    data['line'].append(line)
                                    log += f"{line}\n{line_list}\n{character}: {line}"
                                    # # log.append(line)
                                    # log.append(f"{line_list}")
                                    # log.append(f"{character}: {line}")

    # pprint(data)
    df = pd.DataFrame(data)
    print(df.head(n=10))
    df.to_csv('camp-buddy.csv', index=False)
    df.to_csv('camp-buddy_semicolon-separated.csv', index=False, sep=";")

    log_text = open("log.txt", "w")
    log_text.write(log)
    log_text.close()

main()