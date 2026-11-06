# GC10-DET

**Summary:** Grayscale images of ten surface defect types on steel sheet, collected in real industry and labelled with box-level ground truth for defect detection.

| Parameter | Value |
| --- | --- |
| **Domain** | Manufacturing |
| **Asset / Process** | Steel and metal surfaces |
| **Modality** | Image |
| **Task** | Defect detection; Classification |
| **Annotation** | Bounding box; Class label |
| **Source Type** | Real production |
| **Access** | Direct download |
| **Size** | 3,570 grayscale images |
| **Year** | 2020 |
| **License** | — |

## Description

GC10-DET is a metallic surface defect dataset released with the paper "Deep Metallic Surface Defect Detection: The New Benchmark and Detection Network". The images were collected in a real industrial setting and show defects on the surface of steel sheet.

The collection holds 3,570 grayscale images covering ten defect types: punching, weld line, crescent gap, water spot, oil spot, silk spot, inclusion, rolled pit, crease and waist folding. Defects are labelled with box-level ground truth and their defect type.

In the paper the authors compare SSD, Faster R-CNN, YOLO-V2 and YOLO-V3 with their own end-to-end defect detection network (EDDN) on these images, reporting recall, average precision and mean average precision per defect category. The images are distributed through a Baidu cloud link published in the GitHub repository.

## References

- [GitHub repository](https://github.com/lvxiaoming2019/GC10-DET-Metallic-Surface-Defect-Datasets)
- [pmc.ncbi.nlm.nih.gov](https://pmc.ncbi.nlm.nih.gov/articles/PMC7146379/)
- [Industrial Atlas page](https://www.indatlas.com/datasets/gc10-det/)

[⬅️ Back to Index](../README.md)
