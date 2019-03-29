# -*- coding: utf-8 -*-
import sys
import argparse
import json

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("FILE_Input", help="Set File Path", type=argparse.FileType('r'))
    args = parser.parse_args()

    json_dict = json.load(args.FILE_Input)

    total_size = 0
    
    # 投稿ごとにループ
    for msg in json_dict:
        if msg['type'] == "message":
            if 'hidden' in msg:
                if msg['hidden'] == True:
                    continue

            if 'subtype' in msg:
                if msg['subtype'] == "message_changed":
                    continue
            
            if 'files' in msg:
                for f in msg['files']:
                    print(f['name'] + " " + str(f['size']) + " byte")
                    total_size = total_size + f['size']

    print("total file size: " + str(total_size) + " byte")

    args.FILE_Input.close()
    
# main関数呼び出し
if __name__ == "__main__":
    main()