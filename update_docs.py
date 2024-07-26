import json
import os
import pandas as pd

def update_readme_with_data(json_folder, readme_file, md_folder_path):
    # Collecting dataset information
    datasets = []
    for filename in os.listdir(json_folder):
        if filename.endswith('.json') and filename.lower() != 'template.json':  # Skip the template
            with open(os.path.join(json_folder, filename), 'r', encoding='utf-8') as jsonfile:
                data = json.load(jsonfile)
                datasets.append({
                    'Dataset Name': data.get('name', ''),
                    'Labeled': data.get('Labeled', ''),
                    'Time Series': data.get('Time Series', ''),
                    'Simulation': data.get('Simulation', ''),
                    'Additional Tags': '; '.join(data.get('Additional Tags', [])),
                    'Description': data.get('Description', ''),
                    'Link': data.get('Link', '')
                })

    # Convert list to DataFrame
    df = pd.DataFrame(datasets)
    df.fillna('', inplace=True)
    df['Link'] = df['Dataset Name'].apply(lambda x: f"[{x}]({md_folder_path}/{x.replace(' ', '_').lower()}.md)")
    df['Dataset Name'] = df.apply(lambda x: x['Link'], axis=1)
    df.drop(['Link', 'Description'], axis=1, inplace=True)
    markdown_table = df.to_markdown(index=False)

    # Read the existing README content and update
    with open(readme_file, 'r', encoding='utf-8') as file:
        content = file.readlines()

    start_marker = "## Datasets Table\n"
    start_index = content.index(start_marker) + 2
    end_index = start_index
    while end_index < len(content) and content[end_index].strip() != '':
        end_index += 1

    # Update the section with new table
    content = content[:start_index] + [markdown_table + '\n\n'] + content[end_index:]

    # Write the updated content back to the README
    with open(readme_file, 'w', encoding='utf-8') as file:
        file.writelines(content)
    print("Updated README with the new Markdown table.")

def json_to_markdown(json_path, md_path):
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    markdown_content = f"# {data['name']}\n\n"
    if 'table' in data:
        markdown_content += "| Parameter | Value |\n"
        markdown_content += "| --- | --- |\n"
        for item in data['table']:
            markdown_content += f"| {item['Parameter']} | {item['Value']} |\n"
        markdown_content += "\n"
    
    for section in data['sections']:
        markdown_content += f"## {section['title']}\n{section['content']}\n\n"
    
    if 'references' in data:
        markdown_content += "## References\n"
        for ref in data['references']:
            markdown_content += f"- [{ref['text']}]({ref['link']})\n"
        markdown_content += "\n"
    
    with open(md_path, 'w', encoding='utf-8') as file:
        file.write(markdown_content)
    print(f"Markdown file created for {os.path.basename(md_path)}")

# Paths setup
json_folder_path = 'dataset_docs'
md_folder_path = 'dataset_docs/md_docs'
readme_file_path = 'README.md'
os.makedirs(md_folder_path, exist_ok=True)

# Process JSONs
for filename in os.listdir(json_folder_path):
    if filename.endswith('.json') and filename.lower() != 'template.json':  # Skip template.json
        json_path = os.path.join(json_folder_path, filename)
        md_path = os.path.join(md_folder_path, filename.replace('.json', '.md'))
        json_to_markdown(json_path, md_path)

# Update the README with dataset information directly from JSON files
update_readme_with_data(json_folder_path, readme_file_path, md_folder_path)
