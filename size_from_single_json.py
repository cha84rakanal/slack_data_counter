# -*- coding: utf-8 -*-
import sys
import argparse
import json

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("FILE_Input", help="Set File Path", type=argparse.FileType('r'))
    args = parser.parse_args()

    json.load(args.FILE_Input)

    args.FILE_Input.close()
    
# main関数呼び出し
if __name__ == "__main__":
    main() 