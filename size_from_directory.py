# -*- coding: utf-8 -*-
import sys
import os
import argparse
import json

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument("DIR_Input", help="Set Slack JSON Data Directory", type=str)
    args = parser.parse_args()

    path = args.DIR_Input

    files = os.listdir(path)
    files_dir = [f for f in files if os.path.isdir(os.path.join(path, f))]

    # ディレクトリごとの処理
    for dir_i in files_dir:
        files = os.listdir(path+dir_i+"/")
        for file_i in files:
            print(path+dir_i+"/"+file_i)

# main関数呼び出し
if __name__ == "__main__":
    main()