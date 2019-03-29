# -*- coding: utf-8 -*-
import sys
import argparse
import json

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("FILE_Input", help="Set File Path", type=argparse.FileType('r'))
    args = parser.parse_args()

    json_dict = json.load(args.FILE_Input)
    
    # 投稿ごとにループ
    for msg in json_dict:
        print(msg['type'])
        print('files' in msg)

    args.FILE_Input.close()
    
# main関数呼び出し
if __name__ == "__main__":
    main()