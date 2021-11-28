import os


def main():
    path = "./"
    for root, dirs, files in os.walk(path):
        if root.count('.') != 2:
            print(root)
            for i in files:
                if i.split('.')[1] == 'pdf':
                    os.rename(os.path.join(root, i), os.path.join(root, f'{i.split("_")[0]}'))


if __name__ == '__main__':
    main()
