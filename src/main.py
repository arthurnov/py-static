from copystatic import clean_copy_src_dest
import os
import shutil

src = "./static"
dest = "./public" 

def main():
    print("Deleting public directory...")
    if os.path.exists(dest):
        shutil.rmtree(dest)
    
    print("Copying static files to public directory...")
    clean_copy_src_dest(src, dest)


if __name__ == "__main__":
    main()
