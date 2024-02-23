from dewiki_functions import *
import os

#wiki_xml_file = 'F:/simplewiki-20210401/simplewiki-20210401.xml'  # update this
wiki_xml_file = 'G:/enwiki-20210401/enwiki-20210401.xml'  # update this
json_save_dir = 'G:/wiki_plaintext/'

if __name__ == '__main__':
    import argparse

    parser = argparse.ArgumentParser(description='Process some integers.')
    parser.add_argument('--xml-file', type=str,
                    help='input xml file from mediawiki')
    parser.add_argument('--output-dir', type=str,
                    help='output directory where json is to be saved')
    
    args = parser.parse_args()
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)
    
    process_file_text(args.xml_file, args.output_dir)