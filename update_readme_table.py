import pandas as pd

def csv_to_markdown(csv_file, readme_file):
    # Load the CSV file using the specified delimiter
    df = pd.read_csv(csv_file, delimiter=';')
    
    # Combine the 'Dataset Name' and 'Link' into a clickable Markdown link
    df['Dataset Name'] = df.apply(lambda x: f"[{x['Dataset Name']}]({x['Link']})", axis=1)
    
    # Drop the 'Link' column as it's no longer needed
    df.drop('Link', axis=1, inplace=True)
    
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

# Specify paths to your CSV and README files
csv_file_path = 'datasets_table.csv'
readme_file_path = 'README.md'

# Update the README with the markdown table
csv_to_markdown(csv_file_path, readme_file_path)
