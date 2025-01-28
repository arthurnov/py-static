from textnode import TextNode
import os
import shutil

def clean_copy_src_dest(src, dest):
    if os.path.exists(dest):
        shutil.rmtree(dest)
    src_content = os.listdir(src)
    os.mkdir(dest)
    print(src_content)
    for item in src_content:
        print(item)
        if os.path.isfile(os.path.join(src, item)):
            shutil.copy(os.path.join(src, item), os.path.join(dest, item))
        else:
            clean_copy_src_dest(os.path.join(src, item), os.path.join(dest, item))
    

def main():
    src_path = "static"
    dest_path = "public"
    src_contents = os.listdir(src_path)
    src_isfile = list(map(lambda x: os.path.isfile(os.path.join(src_path, x)), src_contents))
    # print(src_contents)
    # print(src_isfile)
    # print(os.path.exists(dest_path))
    # print(os.path.exists("./feugf"))
    clean_copy_src_dest(src_path, dest_path)


if __name__ == "__main__":
    main()
