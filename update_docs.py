import json
import os
import csv
import pandas as pd

def generate_csv_from_jsons(json_folder, csv_path):
    headers = ['Dataset Name', 'Labeled', 'Time Series', 'Simulation', 'Additional Tags', 'Description', 'Link']
    data_rows = []
    
    # Iterate over all JSON files in the directory
    for filename in os.listdir(json_folder):
        if filename.endswith('.json'):
            with open(os.path.join(json_folder, filename), 'r', encoding='utf-8') as jsonfile:
                data = json.load(jsonfile)
                row = [
                    data.get('name', ''),
                    data.get('Labeled', ''),
                    data.get('Time Series', ''),
                    data.get('Simulation', ''),
                    '; '.join(data.get('Additional Tags', [])),
                    data.get('Description', ''),
                    data.get('Link', '')
                ]
                data_rows.append(row)
    
    # Write data to CSV file
    with open(csv_path, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(headers)
        writer.writerows(data_rows)
    print(f"CSV file created at {csv_path}")

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

def csv_to_markdown(csv_file, readme_file, md_folder_path):
    # Load the CSV file using the specified delimiter
    df = pd.read_csv(csv_file, delimiter=',')
    
    # Replace NaN values with an empty string
    df.fillna('', inplace=True)
    
    # Modify the 'Dataset Name' to link to the Markdown files within the repository
    # Ensure the link is in lowercase and spaces are replaced with underscores
    df['Link'] = df['Dataset Name'].apply(lambda x: f"[{x}]({md_folder_path}/{x.replace(' ', '_').lower()}.md)")
    
    # Combine the 'Dataset Name' with the modified 'Link'
    df['Dataset Name'] = df.apply(lambda x: x['Link'], axis=1)
    
    # Drop the 'Link' and 'Description' columns as they're no longer needed
    df.drop(['Link', 'Description'], axis=1, inplace=True)
    
    # Convert DataFrame to markdown table string
    markdown_table = df.to_markdown(index=False)

    # Read the existing README content
    with open(readme_file, 'r', encoding='utf-8') as file:
        content = file.readlines()
    
    # Locate the section where the datasets table should be inserted or updated
    start_marker = "## Datasets Table\n"
    start_index = content.index(start_marker) + 2  # assuming there's an extra line you want to preserve after the marker
    
    # Remove the old table and all content after the table
    content = content[:start_index] + [markdown_table + '\n']
    
    # Write the updated content back to the README
    with open(readme_file, 'w', encoding='utf-8') as file:
        file.writelines(content)

# Paths setup
json_folder_path = 'dataset_docs'
csv_file_path = 'datasets_table.csv'
md_folder_path = 'dataset_docs/md_docs'
readme_file_path = 'README.md'
os.makedirs(md_folder_path, exist_ok=True)

# Process JSONs
for filename in os.listdir(json_folder_path):
    if filename.endswith('.json'):
        json_path = os.path.join(json_folder_path, filename)
        md_path = os.path.join(md_folder_path, filename.replace('.json', '.md'))
        json_to_markdown(json_path, md_path)
        print(f"Markdown file created for {filename.replace('.json', '')}")

# Generate CSV and update the README
generate_csv_from_jsons(json_folder_path, csv_file_path)
csv_to_markdown(csv_file_path, readme_file_path, md_folder_path)
print("Updated README with the new Markdown table.")
