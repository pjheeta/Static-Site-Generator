import sys
from textnode import TextNode, TextType
from cleanup import publicCleanup
from generate import generate_page, generate_pages_recursive

def main():
    src = "static"
    dst = "docs"
    
    if len(sys.argv) > 1:
        basepath = sys.argv[1]
    else:
        basepath = "/"
    
    publicCleanup(src,dst)
    # generate_page("content/index.md", "template.html", "public/index.html")
    # generate_pages_recursive("content", "template.html", "public")
    generate_pages_recursive("content", "template.html", "docs", basepath)

if __name__ == "__main__":
    main()