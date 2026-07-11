import json
import os
import pandas as pd

# Define folders
json_folder_path = 'json'
md_folder_path = 'markdown'
html_folder_path = 'html/pages'
index_html_file = 'index.html'
readme_file_path = 'README.md'
csv_file_path = 'datasets.csv'

os.makedirs(md_folder_path, exist_ok=True)
os.makedirs(html_folder_path, exist_ok=True)

V2_TABLE_FIELDS = [
    'Dataset',
    'Domain',
    'Asset / Process',
    'Modality',
    'Task',
    'Annotation',
    'Source Type',
    'Access',
    'Size',
    'Year',
    'License'
]

def get_dataset_slug(filename):
    return filename.replace('.json', '').replace(' ', '_').replace('.', '_').lower()

def get_v2_value(data, field):
    if field == 'Dataset':
        return data.get('Name', '')
    return data.get(field, 'Information not available')

def format_markdown_cell(value):
    text = str(value if value is not None else '')
    return text.replace('\r\n', '\n').replace('\n', '<br>').replace('|', '\\|')

def make_markdown_table(rows, fields):
    header = '| ' + ' | '.join(fields) + ' |'
    separator = '| ' + ' | '.join(['---'] * len(fields)) + ' |'
    body = [
        '| ' + ' | '.join(format_markdown_cell(row.get(field, '')) for field in fields) + ' |'
        for row in rows
    ]
    return '\n'.join([header, separator] + body)

def load_combined_json_data():
    combined_data = {}
    for filename in sorted(os.listdir(json_folder_path)):
        path = os.path.join(json_folder_path, filename)
        if not os.path.isfile(path):
            continue
        if filename.endswith('.json') and filename.lower() not in ['template.json', 'datasets.json']:
            with open(path, 'r', encoding='utf-8') as f:
                try:
                    data = json.load(f)
                    combined_data[filename] = data
                except Exception as e:
                    print(f"Error loading {filename}: {e}")
    return combined_data

def generate_json_index(combined_data):
    datasets = []
    for filename, data in combined_data.items():
        link_name = get_dataset_slug(filename)
        dataset = {field: get_v2_value(data, field) for field in V2_TABLE_FIELDS}
        dataset["Link"] = f"html/pages/{link_name}.html"
        datasets.append(dataset)
    return datasets

def remove_stale_generated_files(combined_data):
    expected_slugs = {get_dataset_slug(filename) for filename in combined_data}
    generated_folders = [
        (md_folder_path, '.md'),
        (html_folder_path, '.html'),
    ]

    for folder, extension in generated_folders:
        for filename in os.listdir(folder):
            if not filename.endswith(extension):
                continue
            slug = filename[:-len(extension)]
            if slug not in expected_slugs:
                os.remove(os.path.join(folder, filename))
                print(f"Removed stale generated file {os.path.join(folder, filename)}")

def get_dataset_url(data):
    for reference in data.get('References', []):
        link = reference.get('Link', '')
        if link and link != 'Information not available':
            return link

    source = data.get('Source', '')
    if isinstance(source, str) and source.startswith(('http://', 'https://')):
        return source

    return ''

def update_csv_with_data(combined_data, csv_file):
    datasets = []
    for _, data in combined_data.items():
        dataset = {field: get_v2_value(data, field) for field in V2_TABLE_FIELDS}
        dataset['URL'] = get_dataset_url(data)
        datasets.append(dataset)

    df = pd.DataFrame(datasets)
    df.fillna('', inplace=True)
    df.sort_values(by='Dataset', inplace=True)
    df.to_csv(csv_file, index=False)

    print(f"Updated CSV with Version 2 dataset metadata: {len(datasets)} rows")

def inject_json_to_html(json_data, html_file):
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()

    script_tag = f'<script type="application/json" id="dataset-json">\n{json.dumps(json_data, indent=4)}\n</script>\n'

    if "<!-- JSON_PLACEHOLDER -->" in html_content:
        html_content = html_content.replace("<!-- JSON_PLACEHOLDER -->", script_tag)
    else:
        start_script = html_content.find('<script type="application/json" id="dataset-json">')
        if start_script != -1:
            end_script = html_content.find('</script>', start_script) + len('</script>')
            html_content = html_content[:start_script] + html_content[end_script:]
        html_content = html_content.replace("</body>", f"{script_tag}</body>")

    with open(html_file, 'w', encoding='utf-8') as file:
        file.write(html_content)

    print(f"Injected JSON data into {html_file}")

def update_readme_with_data(combined_data, readme_file, md_folder_path):
    datasets = []
    for filename, data in combined_data.items():
        link_name = get_dataset_slug(filename)
        dataset = {field: get_v2_value(data, field) for field in V2_TABLE_FIELDS}
        dataset['Link'] = link_name
        datasets.append(dataset)

    datasets.sort(key=lambda row: row['Dataset'].lower())
    table_rows = []
    for dataset in datasets:
        row = {field: dataset.get(field, '') for field in V2_TABLE_FIELDS}
        row['Dataset'] = f"[{dataset['Dataset']}]({md_folder_path}/{dataset['Link']}.md)"
        table_rows.append(row)
    markdown_table = make_markdown_table(table_rows, V2_TABLE_FIELDS)

    with open(readme_file, 'r', encoding='utf-8') as file:
        content = file.read()

    # Update dataset count in the statistics section
    dataset_count = len(datasets)
    
    stats_start = content.find("<!-- STATS_START -->")
    stats_end = content.find("<!-- STATS_END -->")
    
    if stats_start != -1 and stats_end != -1:
        # Replace the content between the placeholders
        stats_content = f"**Total Datasets:** {dataset_count}"
        content = content[:stats_start + len("<!-- STATS_START -->")] + "\n" + stats_content + "\n" + content[stats_end:]
    else:
        # If no statistics section exists, add it before the table
        table_start = content.find("## Datasets Table")
        if table_start != -1:
            stats_section = f"\n## 📊 Dataset Statistics\n\n<!-- STATS_START -->\n**Total Datasets:** {dataset_count}\n<!-- STATS_END -->\n\n"
            content = content[:table_start] + stats_section + content[table_start:]

    table_start = content.find("<!-- TABLE_START -->")
    table_end = content.find("<!-- TABLE_END -->")
    if table_start == -1 or table_end == -1:
        raise ValueError("Markers <!-- TABLE_START --> or <!-- TABLE_END --> not found in the README file.")

    updated_content = (
        content[:table_start] +
        "<!-- TABLE_START -->\n" +
        markdown_table +
        "\n" +
        content[table_end:]
    )

    with open(readme_file, 'w', encoding='utf-8') as file:
        file.write(updated_content)

    print(f"Updated README with the new Markdown table and dataset count: {dataset_count}")

def json_to_markdown_and_html(filename, data):
    link_name = get_dataset_slug(filename)
    md_path = os.path.join(md_folder_path, f"{link_name}.md")
    html_path = os.path.join(html_folder_path, f"{link_name}.html")

    # Markdown
    markdown = f"# {data['Name']}\n\n**Summary:** {data.get('Summary', '')}\n\n"
    markdown += "| Parameter | Value |\n| --- | --- |\n"
    for key in V2_TABLE_FIELDS:
        markdown += f"| **{key}** | {get_v2_value(data, key)} |\n"
    markdown += "\n"

    if 'Description' in data:
        markdown += "## Description\n\n"
        for paragraph in data['Description'].split('\n\n'):
            markdown += paragraph.strip() + "\n\n"

    if 'References' in data:
        markdown += "## References\n\n" + '\n'.join([f"- [{r['Text']}]({r['Link']})" for r in data['References']]) + "\n\n"
    markdown += "[⬅️ Back to Index](../README.md)\n"

    with open(md_path, 'w', encoding='utf-8') as f:
        f.write(markdown)
    print(f"Markdown file created for {filename}")

    # HTML
    summary_html = data.get('Summary', '').replace('\n', '<br>')
    html = f"""<html lang="en"><head><meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{data['Name']}</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css" rel="stylesheet">
    <link href="../assets/css/styles.css" rel="stylesheet"></head><body>
    <div class="container mt-5"><h1 class="mb-4">{data['Name']}</h1>
    <p>{summary_html}</p><table class="table table-striped mt-4"><tbody>"""

    for key in V2_TABLE_FIELDS:
        html += f"<tr><td><strong>{key}</strong></td><td>{get_v2_value(data, key)}</td></tr>"
    html += "</tbody></table>"

    if 'Description' in data:
        html += "<h2>Description</h2>"
        for paragraph in data['Description'].split('\n\n'):
            html += f"<p>{paragraph.strip()}</p>"

    if 'References' in data:
        html += "<h2>References</h2><ul>" + ''.join([f"<li><a href='{r['Link']}'>{r['Text']}</a></li>" for r in data['References']]) + "</ul>"

    html += """<a href="../../index.html" class="btn btn-primary mt-4">Back to Index</a></div>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js"></script></body></html>"""

    with open(html_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"HTML file created for {filename}")

# Main execution
combined_data = load_combined_json_data()
remove_stale_generated_files(combined_data)
datasets_json = generate_json_index(combined_data)
inject_json_to_html(datasets_json, index_html_file)

for filename, data in combined_data.items():
    print(f"Processing dataset {filename}...")
    json_to_markdown_and_html(filename, data)

update_readme_with_data(combined_data, readme_file_path, md_folder_path)
update_csv_with_data(combined_data, csv_file_path)
