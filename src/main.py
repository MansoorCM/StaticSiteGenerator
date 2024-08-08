from textnode import TextNode
import shutil
from copystatic import copy_files_recursive

def main():
    src = "./static/"
    des = "./public/"
    shutil.rmtree(des)
    copy_files_recursive(src, des)

main()