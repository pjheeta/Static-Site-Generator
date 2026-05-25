from textnode import TextNode, TextType
from cleanup import publicCleanup
from generate import generate_page


def main():
    src = "static"
    dst = "public"
    publicCleanup(src,dst)
    generate_page("content/index.md", "template.html", "public/index.html")

if __name__ == "__main__":
    main()