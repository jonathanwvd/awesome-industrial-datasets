import json
import os

def setup_environment(output_folder):
    # Create necessary directories
    os.makedirs(output_folder, exist_ok=True)
    dataset_page_folder = os.path.join(output_folder, "dataset_pages")
    os.makedirs(dataset_page_folder, exist_ok=True)
    return dataset_page_folder

def create_index_html(datasets, output_folder):
    # Generate the index.html content with a search box
    index_content = """
    <html>
    <head>
        <title>Dataset Index</title>
        <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.0/jquery.min.js"></script>
        <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery.tablesorter/2.31.3/js/jquery.tablesorter.min.js"></script>
        <script>
        $(document).ready(function() {
            $("table").tablesorter();
            $('#searchInput').on('keyup', function() {
                var value = $(this).val().toLowerCase();
                $("table tbody tr").filter(function() {
                    $(this).toggle($(this).text().toLowerCase().indexOf(value) > -1)
                });
            });
        });
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
    with open(os.path.join(output_folder, 'index.html'), 'w') as f:
        f.write(index_content)


def generate_dataset_pages(json_folder, dataset_page_folder):
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
            create_dataset_html(data, dataset_page_folder, dataset_filename, dataset_name)
            datasets += f"<tr><td><a href='dataset_pages/{dataset_filename}'>{dataset_name}</a></td><td>{labeled}</td><td>{time_series}</td><td>{simulation}</td><td>{additional_tags}</td></tr>"
    return datasets


def read_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as jsonfile:
        return json.load(jsonfile)

def create_dataset_html(data, dataset_page_folder, dataset_filename, dataset_name):
    dataset_path = os.path.join(dataset_page_folder, dataset_filename)
    with open(dataset_path, 'w') as df:
        # Prepare the content with line breaks replaced
        description = data.get('Description', '').replace('\n', '<br>')
        df.write(f"""
        <html>
        <head>
            <title>{dataset_name}</title>
            <link href="https://stackpath.bootstrapcdn.com/bootstrap/4.3.1/css/bootstrap.min.css" rel="stylesheet">
        </head>
        <body>
        <div class="container">
            <h1 class="mt-5">{dataset_name}</h1>
            <p>{description}</p>
            <table class="table table-striped mt-3">
        """)
        for item in data['table']:
            value = item['Value'].replace('\n', '<br>')
            df.write(f"<tr><td>{item['Parameter']}</td><td>{value}</td></tr>")
        if 'sections' in data:
            for section in data['sections']:
                section_content = section['content'].replace('\n', '<br>')
                df.write(f"<h2>{section['title']}</h2><p>{section_content}</p>")
        if 'references' in data:
            df.write("<h2>References</h2>")
            for ref in data['references']:
                df.write(f"<p><a href='{ref['link']}'>{ref['text']}</a></p>")
        df.write("</table><a href='../index.html' class='btn btn-primary'>Back to Index</a></div></body></html>")



# Main script setup
json_folder_path = 'dataset_docs'
html_output_folder = 'dataset_docs/html_docs'
dataset_page_folder = setup_environment(html_output_folder)
datasets = generate_dataset_pages(json_folder_path, dataset_page_folder)
create_index_html(datasets, html_output_folder)
