import re, os, shutil
from block_markdown import markdown_to_blocks, block_to_block_type

def extract_title(markdown):
    print(f"markdown: {markdown}")
    mblocks = markdown_to_blocks(markdown)
    h1headers = list(filter(block_to_block_type == "header", mblocks))
    print(f"h1headers: {h1headers}")
    if h1headers == []:
        raise Exception("Please include a main header line ('# ') in the markdown file")
    
extract_title("## and now, we go on\n\n# hello\n\n## how are we doing tonight?\n")