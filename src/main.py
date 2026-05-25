import os
import shutil
from textnode import TextNode, TextType


def main():
    src = "static"
    dst = "public"
    publicCleanup(src,dst)

def publicCleanup(src,dst):

    if os.path.exists(dst):        
        shutil.rmtree(dst)
    os.mkdir(dst)
    files = os.listdir(src)
    for file in files:
        if os.path.isfile(os.path.join(src,file)) is True:
            shutil.copy(os.path.join(src,file), os.path.join(dst,file)) 
        else:
            publicCleanup(os.path.join(src, file), os.path.join(dst, file))

    


if __name__ == "__main__":
    main()