import os

def main():
    current_dir = os.getcwd()
    file_list = os.listdir(current_dir)
    file_list.sort()
    for f in file_list:
        print(f)


if __name__ == '__main__':
    main()