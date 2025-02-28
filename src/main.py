from copystatic import clean_copy_src_dest
from generate import generate_pages_recursive
import os
import shutil
import sys

src = "./static"
dest = "./docs"
content = "./content"
template_path = "./template.html"

def main():
    basepath = "/"
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    print(f"BASEPATH: {basepath}")


    print("Deleting public directory...")
    if os.path.exists(dest):
        shutil.rmtree(dest)
     
    print("Copying static files to public directory...")
    clean_copy_src_dest(src, dest)

    print("Generating page...")
    generate_pages_recursive(content, template_path, dest, basepath)



if __name__ == "__main__":
    main()
