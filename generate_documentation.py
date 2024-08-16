import json
import os

def generate_json_data(json_folder):
    datasets = []
    # Process each JSON file in the folder
    for filename in os.listdir(json_folder):
        if filename.endswith('.json') and filename.lower() not in ['template.json', 'datasets.json']:  # Skip template and datasets.json
            print(f"Processing dataset {filename}...")
            try:
                with open(os.path.join(json_folder, filename), 'r', encoding='utf-8') as jsonfile:
                    data = json.load(jsonfile)
                    # Generate the link based on the filename, not the dataset name
                    link_name = filename.replace('.json', '').replace(' ', '_').replace('.', '_').lower()
                    datasets.append({
                        "Dataset Name": data.get("Name", ""),
                        "Labeled": data.get("Labeled", ""),
                        "Time Series": data.get("Time Series", ""),
                        "Simulation": data.get("Simulation", ""),
                        "Missing Values": data.get("Missing Values", ""),
                        "Dataset Characteristics": data.get("Dataset Characteristics", ""),
                        "Associated Tasks": data.get("Associated Tasks", ""),
                        "Number of Instances": data.get("Number of Instances", ""),
                        "Number of Features": data.get("Number of Features", ""),
                        "Date Donated": data.get("Date Donated", ""),
                        "Summary": data.get("Summary", ""),
                        "Additional Tags": "; ".join(data.get("Additional Tags", [])),
                        "Link": f"html/pages/{link_name}.html"  # Use the filename for the link
                    })
            except Exception as e:
                print(f"Error processing {filename}: {e}")

    return datasets


def inject_json_to_html(json_data, html_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    # Remove any previous JSON data by finding and removing the existing script tag
    start_script = html_content.find('<script type="application/json" id="dataset-json">')
    if start_script != -1:
        end_script = html_content.find('</script>', start_script) + len('</script>')
        html_content = html_content[:start_script] + html_content[end_script:]

    # Create the new script tag with the JSON data
    script_tag = f'<script type="application/json" id="dataset-json">\n{json.dumps(json_data, indent=4)}\n</script>\n'
    
    # Check if the placeholder exists, replace it; if not, append the script tag before closing </body>
    if "<!-- JSON_PLACEHOLDER -->" in html_content:
        html_content = html_content.replace("<!-- JSON_PLACEHOLDER -->", script_tag)
    else:
        html_content = html_content.replace("</body>", f"{script_tag}</body>")

    with open(html_file, 'w', encoding='utf-8') as file:
        file.write(html_content)
    
    print(f"Injected JSON data into {html_file}")



def json_to_markdown(json_path, md_path):
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)
    
    markdown_content = f"# {data['Name']}\n\n"
    if 'table' in data:
        markdown_content += "| Parameter | Value |\n"
        markdown_content += "| --- | --- |\n"
        for item in data['table']:
            markdown_content += f"| {item['Parameter']} | {item['Value']} |\n"
        markdown_content += "\n"
    
    for section in data['Sections']:
        markdown_content += f"## {section['Title']}\n{section['Content']}\n\n"
    
    if 'References' in data:
        markdown_content += "## References\n"
        for ref in data['References']:
            markdown_content += f"- [{ref['Text']}]({ref['Link']})\n"
        markdown_content += "\n"
    
    with open(md_path, 'w', encoding='utf-8') as file:
        file.write(markdown_content)
    print(f"Markdown file created for {os.path.basename(md_path)}")

def json_to_html(json_path, html_path):
    with open(json_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Start building the HTML content
    html_content = """
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>""" + data['Name'] + """</title>
        <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
        <link href="../assets/css/styles.css" rel="stylesheet">
    </head>
    <body>
        <div class="container mt-5">
            <h1 class="mb-4">""" + data['Name'] + """</h1>

            <p>""" + data.get('Summary', '').replace('\n', '<br>') + """</p>

            <table class="table table-striped mt-4">
                <tbody>
    """

    # Add the table with the relevant information
    for key in ['Name', 'Labeled', 'Time Series', 'Simulation', 'Missing Values', 'Dataset Characteristics', 'Feature Type', 'Associated Tasks', 'Number of Instances', 'Number of Features', 'Date Donated', 'Source']:
        if key in data:
            html_content += "<tr><td><strong>{}</strong></td><td>{}</td></tr>".format(key, data[key])

    html_content += """
                </tbody>
            </table>
    """

    # Add sections
    if 'Sections' in data:
        for section in data['Sections']:
            section_content = section['Content'].replace('\n', '<br>')
            html_content += "<h2>{}</h2><p>{}</p>".format(section['Title'], section_content)

    # Add tags section
    if 'Additional Tags' in data and data['Additional Tags']:
        html_content += "<h2>Tags</h2><ul>"
        for tag in data['Additional Tags']:
            html_content += "<li>{}</li>".format(tag)
        html_content += "</ul>"

    # Add references
    if 'References' in data:
        html_content += "<h2>References</h2><ul>"
        for ref in data['References']:
            html_content += "<li><a href='{}'>{}</a></li>".format(ref['Link'], ref['Text'])
        html_content += "</ul>"

    # Close the HTML content
    html_content += """
            <a href="../../index.html" class="btn btn-primary mt-4">Back to Index</a>
        </div>
        <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script>
    </body>
    </html>
    """

    # Write the HTML content to the file
    with open(html_path, 'w', encoding='utf-8') as file:
        file.write(html_content)

    print(f"HTML file created for {os.path.basename(html_path)}")




# Paths setup
json_folder_path = 'json'
md_folder_path = 'markdown'
html_folder_path = 'html/pages'
index_html_file = 'index.html'
os.makedirs(md_folder_path, exist_ok=True)
os.makedirs(html_folder_path, exist_ok=True)

# Generate JSON data
datasets_json = generate_json_data(json_folder_path)

# Inject JSON data directly into the HTML file
inject_json_to_html(datasets_json, index_html_file)

# Process JSONs to generate Markdown and HTML
for filename in os.listdir(json_folder_path):
    if filename.endswith('.json') and filename.lower() not in ['template.json', 'datasets.json']:  # Skip template.json and datasets.json
        print(f"Processing dataset {filename}...")
        try:
            json_path = os.path.join(json_folder_path, filename)
            md_path = os.path.join(md_folder_path, filename.replace('.json', '.md'))
            html_path = os.path.join(html_folder_path, filename.replace('.json', '.html'))
            json_to_markdown(json_path, md_path)
            json_to_html(json_path, html_path)
        except Exception as e:
            print(f"Error processing {filename}: {e}")
