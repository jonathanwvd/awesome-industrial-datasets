# Contribution Guidelines

Thank you for considering contributing to our repository.

## How to Contribute
You can contribute in several ways:
- **Suggest or share datasets**: Add new datasets by creating a JSON description and placing it in the `json` folder.
- **Improve documentation**: Help fix typos or enhance explanations.
- **Enhance formatting**: Ensure consistency in document formatting across the repository.

## Making a Pull Request
Please follow these guidelines for your pull requests:
- **Check for duplicates**: Ensure your contribution is unique and not already included.
- **Individual pull requests**: Submit separate pull requests for different suggestions.
- **Follow the format**: Use our JSON template for datasets and maintain readability and structure in documentation.

## Adding Your Dataset
To add a new dataset, create a JSON file that accurately describes the dataset according to our template. Place this file in the `json` folder. This structured approach helps maintain uniformity and ease of access for all users.

For guidance on how to format your JSON, refer to the template in `json/template.json`.

## Generating Documentation
To generate the documentation (Markdown and HTML files) and update the README, follow these steps:

1. Ensure your JSON files are correctly placed in the `json` folder.
2. Run the `generate_documentation.py` script located in the root of the repository. This script will:
   - Generate Markdown files in the `markdown` folder.
   - Generate HTML files in the `html` folder.
   - Update the `README.md` file with the latest datasets table.
