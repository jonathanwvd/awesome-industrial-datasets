# Contributing

Thank you for helping improve Awesome Industrial Datasets. This list is curated:
an entry is added only when it fits the scope below and its details can be
checked against the original source.

## Scope

A dataset fits this list when it:

- comes from industrial assets, processes, or operations (manufacturing,
  process industries, energy, maintenance, inspection, robotics, utilities,
  industrial control systems, and similar), or from a lab, testbed, or
  simulator that represents them;
- is useful for machine learning, analytics, or benchmarking;
- has an official page, repository, archive, or paper that describes it;
- can be obtained publicly, even if a form or login is required.

The following are out of scope:

- product catalogs, price lists, or retail and marketplace listings;
- pages or corpora generated mainly for search engines or marketing;
- directories or product pages that only point to data hosted elsewhere
  (suggest the original source instead);
- datasets without a verifiable source or access path.

Tools that help people use datasets already on the list (loaders, converters,
benchmarks) can be suggested for the Tools section of the README.

If you are affiliated with the dataset or tool you suggest, please say so.
Affiliation does not rule out an entry, but it helps the review.

## How to suggest a dataset

Open an issue with the **Suggest a dataset** template. Please include the
official page, the industrial use case, and any known license, access,
size, year, and annotation details.

## Pull requests

Pull requests that add or edit a dataset should:

1. Add or edit one file in `json/` only. Use the fields and controlled values
   from [DATASET_TAXONOMY.md](DATASET_TAXONOMY.md).
2. Write the summary and description in English, based on the official
   source. Do not guess values; use `Information not available` when the
   source does not state them.
3. Run `python generate_documentation.py` and commit the regenerated
   `README.md` and `markdown/` files.

Do not edit the table in `README.md` or the files in `markdown/` by hand;
they are generated from `json/`.
