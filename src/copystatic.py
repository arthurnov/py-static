import os
import shutil

def clean_copy_src_dest(src, dest):
    if not os.path.exists(dest):
        os.mkdir(dest)
    
    for item in os.listdir(src):
        if os.path.isfile(os.path.join(src, item)):
            shutil.copy(os.path.join(src, item), os.path.join(dest, item))
        else:
            clean_copy_src_dest(os.path.join(src, item), os.path.join(dest, item))