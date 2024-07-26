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

def json_to_html(json_path, html_path):
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    description = data.get('Description', '').replace('\n', '<br>')
    html_content = f"""
    <html>
    <head>
        <title>{data['name']}</title>
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
    </head>
    <body>
    <div class="container">
        <h1 class="mt-5">{data['name']}</h1>
        <p>{description}</p>
        <table class="table table-striped mt-3">
    """
    if 'table' in data:
        for item in data['table']:
            value = item['Value'].replace('\n', '<br>')
            html_content += f"<tr><td>{item['Parameter']}</td><td>{value}</td></tr>"
    if 'sections' in data:
        for section in data['sections']:
            section_content = section['content'].replace('\n', '<br>')
            html_content += f"<h2>{section['title']}</h2><p>{section_content}</p>"
    if 'references' in data:
        html_content += "<h2>References</h2>"
        for ref in data['references']:
            html_content += f"<p><a href='{ref['link']}'>{ref['text']}</a></p>"
    html_content += """
        </table>
        <a href="../index.html" class="btn btn-primary">Back to Index</a>
    </div>
    </body>
    </html>
    """
    
    with open(html_path, 'w', encoding='utf-8') as file:
        file.write(html_content)
    print(f"HTML file created for {os.path.basename(html_path)}")

def generate_html_index(json_folder, output_folder):
    datasets = ""
    # Process each JSON file
    for filename in os.listdir(json_folder):
        if filename.endswith('.json') and filename.lower() != 'template.json':  # Skip the template
            data = read_json(os.path.join(json_folder, filename))
            dataset_name = data['name']
            labeled = data.get('Labeled', '')
            time_series = data.get('Time Series', '')
            simulation = data.get('Simulation', '')
            additional_tags = ', '.join(data.get('Additional Tags', []))
            dataset_filename = f"{dataset_name.replace(' ', '_').lower()}.html"
            datasets += f"<tr><td><a href='html/{dataset_filename}'>{dataset_name}</a></td><td>{labeled}</td><td>{time_series}</td><td>{simulation}</td><td>{additional_tags}</td></tr>"

    # Generate the index.html content with a search box
    index_content = f"""
    <html>
    <head>
        <title>Dataset Index</title>
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery.tablesorter/2.31.3/js/jquery.tablesorter.min.js"></script>
        <script>
        $(document).ready(function() {{
            $("table").tablesorter();
            $('#searchInput').on('keyup', function() {{
                var value = $(this).val().toLowerCase();
                $("table tbody tr").filter(function() {{
                    $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
                }});
            }});
        }});
        </script>
    </head>
    <body>
    <div class="container">
        <h1 class="mt-5">Dataset Index</h1>
        <input class="form-control mb-3" id="searchInput" type="text" placeholder="Search by tags...">
        <table class="table table-bordered mt-3 tablesorter">
            <thead class="thead-light">
                <tr>
                    <th>Dataset Name</th>
                    <th>Labeled</th>
                    <th>Time Series</th>
                    <th>Simulation</th>
                    <th>Additional Tags</th>
                </tr>
            </thead>
            <tbody>
    """ + datasets + """
            </tbody>
        </table>
    </div>
    </body>
    </html>
    """
    with open(os.path.join(output_folder, 'index.html'), 'w', encoding='utf-8') as f:
        f.write(index_content)
    print("index.html created in the root folder.")

def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as jsonfile:
        return json.load(jsonfile)

# Paths setup
json_folder_path = 'json'
md_folder_path = 'markdown'
html_folder_path = 'html'
readme_file_path = 'README.md'
os.makedirs(md_folder_path, exist_ok=True)
os.makedirs(html_folder_path, exist_ok=True)

# Process JSONs to generate Markdown and HTML
for filename in os.listdir(json_folder_path):
    if filename.endswith('.json') and filename.lower() != 'template.json':  # Skip template.json
        json_path = os.path.join(json_folder_path, filename)
        md_path = os.path.join(md_folder_path, filename.replace('.json', '.md'))
        html_path = os.path.join(html_folder_path, filename.replace('.json', '.html'))
        json_to_markdown(json_path, md_path)
        json_to_html(json_path, html_path)

# Update the README with dataset information directly from JSON files
update_readme_with_data(json_folder_path, readme_file_path, md_folder_path)

# Generate index.html in the root directory
generate_html_index(json_folder_path, '.')
