import json
# import pandas as pd
import glob
import re
from anyascii import anyascii
import tqdm
import numpy as np
import os

def replace_eq(string):
    string = string.group(0)
    num_eq = 0
    for char in string:
        if char =="=":
            num_eq +=1
        else:
            break
    return "\n\n" + "#"*num_eq + " "+ string.replace("=", "") + "\n\n"


def clean_data(json_dir, markdown_dir, return_clean=False):
    if not os.path.exists(markdown_dir):
        os.makedirs(markdown_dir)
    paths = glob.glob(os.path.join(json_dir, "*.json"))
    for i in tqdm.tqdm(paths):
        with open(i, 'r', encoding='utf-8') as fp:
            data = json.load(fp)
        data_cleaned = "\n# "+data['title'] + "\n\n" + re.sub(r'=+([^=]+)=+', replace_eq, data['text'])
        if return_clean:
            return data
        output_path = i.replace(json_dir, markdown_dir).replace('.json', '.md')
        with open(output_path, 'w') as fp:
            fp.write(anyascii(data_cleaned))

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--json-dir', type=str,
                    help='dir where json files are stored')
    parser.add_argument('--markdown-dir', type=str,
                    help='dir where markdown files are to be stored')
    args = parser.parse_args()
    
    clean_data(args.json_dir, args.markdown_dir)