import re

def extract_markdown_links(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return (matches)

def extract_markdown_images(text):
    matches = re.findall(r"\[(.*?)\]\((.*?)\)", text)
    return (matches)


# [("rick roll", "https://i.imgur.com/aKaOqIh.gif"), ("obi wan", "https://i.imgur.com/fJRm4Vk.jpeg")]

# text = "I have a (cat) and a (dog)"
# matches = re.findall(r"\[(.*?)\]", text)


# [("to boot dev", "https://www.boot.dev"), ("to youtube", "https://www.youtube.com/@bootdotdev")]