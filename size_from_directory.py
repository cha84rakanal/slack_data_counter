# -*- coding: utf-8 -*-
import sys
import os
import argparse
import json

def size_from_single_json(dir_path):

    with open(dir_path) as f:

        json_dict = json.load(f)

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
                        if 'is_external' in f:
                            if f['is_external'] == False:
                                
                                if 'name' in f:
                                    print(f['name'] + " " + str(f['size']) + " byte")
                                elif 'title' in f:
                                    print(f['title'] + " " + str(f['size']) + " byte")
                                else:
                                    print("File" + " " + str(f['size']) + " byte")
                                
                                total_size = total_size + f['size']

        print("total file size: " + str(total_size) + " byte")

    return total_size

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("DIR_Input", help="Set Slack JSON Data Directory", type=str)
    args = parser.parse_args()

    path = args.DIR_Input

    files = os.listdir(path)
    files_dir = [f for f in files if os.path.isdir(os.path.join(path, f))]

    all_size = 0

    # ディレクトリごとの処理
    for dir_i in files_dir:
        files = os.listdir(path+dir_i+"/")
        for file_i in files:
            all_size = all_size + size_from_single_json(path+dir_i+"/"+file_i)

    print("")
    print("total file size: " + str(all_size) + " byte")

# main関数呼び出し
if __name__ == "__main__":
    main()