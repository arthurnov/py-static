import re, os, shutil
from block_markdown import markdown_to_blocks, block_to_block_type, markdown_to_html_node

def extract_title(markdown):
    # mblocks = markdown_to_blocks(markdown)
    # heading = ""
    # for block in mblocks:
    #     if re.findall(r"^# ", block) != []:
    #          heading = block[2:]
    #          break
    # if heading == "":
    #     raise Exception("Please include a main header line ('# ') in the markdown file")
    # return heading
    lines = markdown.split("\n")
    for line in lines:
        if line.startswith("# "):
            return line[2: ]
    raise ValueError("No title found")    
        
def generate_page(from_path, template_path, dest_path, basepath):

    print(f"Generating page from {from_path} to {dest_path} using {template_path}")

    markdown_file = open(from_path)
    template_file = open(template_path)
    markdown = markdown_file.read()
    template = template_file.read()
    markdown_file.close()
    template_file.close()

    html_string = markdown_to_html_node(markdown).to_html()
    title = extract_title(markdown)
    template = template.replace(r"{{ Title }}", title)
    template = template.replace(r"{{ Content }}", html_string)
    template = template.replace(f"href=\"/", f"href=\"{basepath}")
    template = template.replace(f"src=\"/", f"src=\"{basepath}")
    
    # ?
    dest_dir = os.path.dirname(dest_path)
    if dest_dir != "":
        os.makedirs(dest_dir, exist_ok=True)

    file = open(dest_path, 'w')
    file.write(template)
    file.close()

def generate_pages_recursive(dir_path_content, template_path, dest_dir_path, basepath):
    if not os.path.exists(dest_dir_path):
        os.mkdir(dest_dir_path)
    
    for item in os.listdir(dir_path_content):
        if os.path.isfile(os.path.join(dir_path_content, item)):
            generate_page(os.path.join(dir_path_content, item), template_path, os.path.join(dest_dir_path, item[:-2]+"html"), basepath)
        else:
            generate_pages_recursive(os.path.join(dir_path_content, item), template_path, os.path.join(dest_dir_path, item), basepath)