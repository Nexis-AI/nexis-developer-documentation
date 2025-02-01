import os
import re

def add_image_styles(content):
    # Regular expression to find markdown and HTML images, but not logo/button/tab images
    image_pattern = r'(!\[.*?\]\(.*?\)|<img.*?src=["\']((?!.*(?:logo|button|tab)).*?)["\'].*?>)'
    
    # The style wrapper
    style_wrapper = '<div class="p-2 not-prose relative bg-gray-50/50 rounded-2xl overflow-hidden dark:bg-gray-800/25">\n<div class="absolute inset-0 bg-grid-neutral-200/20 [mask-image:linear-gradient(0deg,#fff,rgba(255,255,255,0.6))] dark:bg-grid-white/5 dark:[mask-image:linear-gradient(0deg,rgba(255,255,255,0.1),rgba(255,255,255,0.5))]" style="background-position: 10px 10px;"></div>\n{}\n</div>'
    
    def replace_image(match):
        # Don't wrap if it's a logo, button, or tab image
        if 'logo' in match.group(0).lower() or 'button' in match.group(0).lower() or 'tab' in match.group(0).lower():
            return match.group(0)
        return style_wrapper.format(match.group(0))
    
    return re.sub(image_pattern, replace_image, content)

def process_file(file_path):
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Skip if no images found
        if not re.search(r'!\[.*?\]\(.*?\)|<img.*?src=["\']((?!.*(?:logo|button|tab)).*?)["\'].*?>', content):
            return
        
        # Add styles to images
        updated_content = add_image_styles(content)
        
        # Write back to file if content changed
        if updated_content != content:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(updated_content)
            print(f"Updated {file_path}")
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")

def main():
    # Walk through all directories
    for root, dirs, files in os.walk('.'):
        # Skip hidden directories and specific folders
        if '/.' in root or '\\.' in root or any(x in root.lower() for x in ['logo', 'button', 'tab']):
            continue
        
        # Process MDX files
        for file in files:
            if file.endswith('.mdx'):
                file_path = os.path.join(root, file)
                process_file(file_path)

if __name__ == '__main__':
    main() 