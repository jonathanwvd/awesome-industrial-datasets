# MaintNorm

12,000 short English texts from maintenance work orders of three Australian mining organisations, annotated for lexical normalisation and entity masking.

- **Domain:** Mining and mineral processing
- **Modality:** Text and documents
- **Task:** Other
- **Annotation:** Text and QA label
- **Source Type:** Real production
- **Access:** Hugging Face
- **Size:** 12,000 texts
- **Year:** 2024
- **License:** MIT

## Description

MaintNorm is a corpus of short texts taken from maintenance work orders at three major mining organisations in Australia. It accompanies a paper by Tyler Bikaun, Melinda Hodkiewicz and Wei Liu at the Ninth Workshop on Noisy and User-generated Text (W-NUT 2024), published by the Association for Computational Linguistics.

The 12,000 English texts are annotated for two tasks: lexical normalisation and token-level entity tagging. Files list one token per line, each paired with its normalised or masked form. Four mask tokens stand for asset identifiers, organisation-specific information such as proprietary systems and third-party contractors, numbers, and dates in numeric or phrase form. The texts are grouped by source as company_a, company_b and company_c, plus a combined set.

The corpus is released under the MIT license.

## References

- [Hugging Face dataset](https://huggingface.co/datasets/nlp-tlp/MaintNorm)
- [Industrial Atlas page](https://www.indatlas.com/datasets/maintnorm/)

[⬅️ Back to Index](../README.md)
