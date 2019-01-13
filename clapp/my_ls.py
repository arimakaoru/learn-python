#!/usr/bin/env python3
import os

def main():
    current_dir = os.getcwd()
    file_list_all = os.listdir(current_dir)
    file_list_all.sort()

    # 隠しファイルを除く
    file_list = [f for f in file_list_all if f[0] != '.']
    for f in file_list:
        print(f)

if __name__ == '__main__':
    main()