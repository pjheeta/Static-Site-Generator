from textnode import TextNode, TextType
from cleanup import publicCleanup


def main():
    src = "static"
    dst = "public"
    publicCleanup(src,dst)

if __name__ == "__main__":
    main()