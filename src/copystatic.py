import os
import shutil

def copy_files_recursive(src, des):
    if not os.path.exists(des):
        os.mkdir(des)
    for file_name in os.listdir(src):
        src_path = os.path.join(src, file_name)
        des_path = os.path.join(des, file_name)
        print(f"* {src_path} -> {des_path}")
        if os.path.isfile(src_path):
            shutil.copy(src_path, des)
        else:
            copy_files_recursive(src_path, des_path)