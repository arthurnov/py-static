from copystatic import clean_copy_src_dest
from generate import generate_page
import os
import shutil

src = "./static"
dest = "./public"
content = "./content"
template_path = "./template.html"

def main():

    print("Deleting public directory...")
    if os.path.exists(dest):
        shutil.rmtree(dest)
     
    print("Copying static files to public directory...")
    clean_copy_src_dest(src, dest)

    print("Generating page...")
    generate_page(os.path.join(content, "index.md"), template_path, os.path.join(dest, "index.html"))



if __name__ == "__main__":
    main()
