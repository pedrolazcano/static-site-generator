from textnode import *
import re

def split_nodes_delimiter(old_nodes, delimiter, text_type):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        split_text = old_node.text.split(delimiter)  
        if len(split_text) % 2 == 0:
            raise ValueError("invalid Markdown, odd number of delimiters")
        split_nodes = [
            TextNode(text, TextType.TEXT if (i % 2 == 0) else text_type)
            for i, text in enumerate(split_text)
        ]
        new_nodes.extend(split_nodes)

    return new_nodes

def extract_markdown_images(text):
    return re.findall(r"!\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def extract_markdown_links(text):
    return re.findall(r"(?<!!)\[([^\[\]]*)\]\(([^\(\)]*)\)", text)

def split_nodes_image(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        images_matched = extract_markdown_images(old_node.text)

        cur = old_node.text
        for alt, url in images_matched:
            split_text = cur.split(f"![{alt}]({url})", maxsplit = 1)  
             
            split_nodes = [
                TextNode(split_text[0], TextType.TEXT),
                TextNode(alt, TextType.IMAGE, url) 
            ]
            new_nodes.extend(split_nodes)
            cur = split_text[1]

        if cur:
            new_nodes.append(TextNode(cur, TextType.TEXT))

    return new_nodes

def split_nodes_link(old_nodes):
    new_nodes = []
    for old_node in old_nodes:
        if old_node.text_type != TextType.TEXT:
            new_nodes.append(old_node)
            continue

        links_matched = extract_markdown_links(old_node.text)

        cur = old_node.text
        for anchor, url in links_matched:
            split_text = cur.split(f"[{anchor}]({url})", maxsplit = 1)  
             
            split_nodes = [
                TextNode(split_text[0], TextType.TEXT),
                TextNode(anchor, TextType.LINK, url) 
            ]
            new_nodes.extend(split_nodes)
            cur = split_text[1]

        if cur:
            new_nodes.append(TextNode(cur, TextType.TEXT))

    return new_nodes

def text_to_textnodes(text):
    nodes = [TextNode(text, TextType.TEXT)]
    nodes = split_nodes_delimiter(nodes, "**", TextType.BOLD)
    nodes = split_nodes_delimiter(nodes, "_", TextType.ITALIC)
    nodes = split_nodes_delimiter(nodes, "`", TextType.CODE)
    nodes = split_nodes_image(nodes)
    nodes = split_nodes_link(nodes)
    return nodes
    

