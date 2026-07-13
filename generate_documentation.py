import json
import os


JSON_FOLDER_PATH = "json"
MD_FOLDER_PATH = "markdown"
README_FILE_PATH = "README.md"

V2_TABLE_FIELDS = [
    "Dataset",
    "Domain",
    "Asset / Process",
    "Modality",
    "Task",
    "Annotation",
    "Source Type",
    "Access",
    "Size",
    "Year",
    "License",
]


def get_dataset_slug(filename):
    return filename.replace(".json", "").replace(" ", "_").replace(".", "_").lower()


def get_v2_value(data, field):
    if field == "Dataset":
        return data.get("Name", "")
    return data.get(field, "Information not available")


def format_markdown_cell(value):
    text = str(value if value is not None else "")
    return text.replace("\r\n", "\n").replace("\n", "<br>").replace("|", "\\|")


def make_markdown_table(rows, fields):
    header = "| " + " | ".join(fields) + " |"
    separator = "| " + " | ".join(["---"] * len(fields)) + " |"
    body = [
        "| " + " | ".join(format_markdown_cell(row.get(field, "")) for field in fields) + " |"
        for row in rows
    ]
    return "\n".join([header, separator] + body)


def load_combined_json_data():
    combined_data = {}
    for filename in sorted(os.listdir(JSON_FOLDER_PATH)):
        path = os.path.join(JSON_FOLDER_PATH, filename)
        if not os.path.isfile(path):
            continue
        if not filename.endswith(".json") or filename.lower() in {"template.json", "datasets.json"}:
            continue
        with open(path, "r", encoding="utf-8") as handle:
            try:
                combined_data[filename] = json.load(handle)
            except Exception as exc:
                print(f"Error loading {filename}: {exc}")
    return combined_data


def remove_stale_markdown_files(combined_data):
    expected_slugs = {get_dataset_slug(filename) for filename in combined_data}
    if not os.path.isdir(MD_FOLDER_PATH):
        return

    for filename in os.listdir(MD_FOLDER_PATH):
        if not filename.endswith(".md"):
            continue
        slug = filename[:-3]
        if slug not in expected_slugs:
            path = os.path.join(MD_FOLDER_PATH, filename)
            os.remove(path)
            print(f"Removed stale generated file {path}")


def update_readme_with_data(combined_data, readme_file, md_folder_path):
    datasets = []
    for filename, data in combined_data.items():
        link_name = get_dataset_slug(filename)
        dataset = {field: get_v2_value(data, field) for field in V2_TABLE_FIELDS}
        dataset["Link"] = link_name
        datasets.append(dataset)

    datasets.sort(key=lambda row: row["Dataset"].lower())
    table_rows = []
    for dataset in datasets:
        row = {field: dataset.get(field, "") for field in V2_TABLE_FIELDS}
        row["Dataset"] = f"[{dataset['Dataset']}]({md_folder_path}/{dataset['Link']}.md)"
        table_rows.append(row)
    markdown_table = make_markdown_table(table_rows, V2_TABLE_FIELDS)

    with open(readme_file, "r", encoding="utf-8") as handle:
        content = handle.read()

    dataset_count = len(datasets)
    stats_start = content.find("<!-- STATS_START -->")
    stats_end = content.find("<!-- STATS_END -->")
    if stats_start != -1 and stats_end != -1:
        stats_content = f"**Total Datasets:** {dataset_count}"
        content = (
            content[: stats_start + len("<!-- STATS_START -->")]
            + "\n"
            + stats_content
            + "\n"
            + content[stats_end:]
        )
    else:
        table_heading = content.find("## Datasets Table")
        if table_heading != -1:
            stats_section = (
                f"\n## Dataset Statistics\n\n"
                f"<!-- STATS_START -->\n"
                f"**Total Datasets:** {dataset_count}\n"
                f"<!-- STATS_END -->\n\n"
            )
            content = content[:table_heading] + stats_section + content[table_heading:]

    table_start = content.find("<!-- TABLE_START -->")
    table_end = content.find("<!-- TABLE_END -->")
    if table_start == -1 or table_end == -1:
        raise ValueError("Markers <!-- TABLE_START --> or <!-- TABLE_END --> not found in README.md")

    updated_content = (
        content[:table_start]
        + "<!-- TABLE_START -->\n"
        + markdown_table
        + "\n"
        + content[table_end:]
    )

    with open(readme_file, "w", encoding="utf-8") as handle:
        handle.write(updated_content)

    print(f"Updated README with the Markdown table and dataset count: {dataset_count}")


def json_to_markdown(filename, data):
    link_name = get_dataset_slug(filename)
    md_path = os.path.join(MD_FOLDER_PATH, f"{link_name}.md")

    markdown = f"# {data['Name']}\n\n**Summary:** {data.get('Summary', '')}\n\n"
    markdown += "| Parameter | Value |\n| --- | --- |\n"
    for key in V2_TABLE_FIELDS:
        markdown += f"| **{key}** | {get_v2_value(data, key)} |\n"
    markdown += "\n"

    if "Description" in data:
        markdown += "## Description\n\n"
        for paragraph in data["Description"].split("\n\n"):
            markdown += paragraph.strip() + "\n\n"

    if "References" in data:
        references = [f"- [{item['Text']}]({item['Link']})" for item in data["References"]]
        markdown += "## References\n\n" + "\n".join(references) + "\n\n"

    markdown += "[\u2b05\ufe0f Back to Index](../README.md)\n"

    with open(md_path, "w", encoding="utf-8") as handle:
        handle.write(markdown)
    print(f"Markdown file created for {filename}")


def main():
    os.makedirs(MD_FOLDER_PATH, exist_ok=True)
    combined_data = load_combined_json_data()
    remove_stale_markdown_files(combined_data)

    for filename, data in combined_data.items():
        print(f"Processing dataset {filename}...")
        json_to_markdown(filename, data)

    update_readme_with_data(combined_data, README_FILE_PATH, MD_FOLDER_PATH)


if __name__ == "__main__":
    main()
