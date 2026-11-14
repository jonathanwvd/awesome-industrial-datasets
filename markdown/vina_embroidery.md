# Vina-Embroidery

Multi-view RGB images of embroidered textiles, normal and defective, with predefined anomaly detection splits and a YOLO subset of polygon labels for four defect classes.

- **Domain:** Manufacturing
- **Asset / Process:** Surfaces and textures
- **Modality:** Image
- **Task:** Anomaly detection; Anomaly localization; Object detection
- **Annotation:** Sample label; Instance mask; Class label
- **Access:** Mendeley Data
- **Size:** 1,080 images from 3 viewpoints, plus 954 annotated images
- **Year:** 2026
- **License:** CC BY

## Description

Vina-Embroidery is an image set for inspecting embroidered textiles, published on Mendeley Data by Le Thanh. It is built for multi-view anomaly detection and defect localization in textile manufacturing.

The main set has 1,080 high-resolution RGB images, 492 normal and 588 abnormal, taken from three viewpoints: straight above at 90 degrees, and off-axis at 45 and 60 degrees, which bring out surface texture and shadow cues. A manifest table gives, for every image, its path, viewing angle, label, sample, defect type and group.

For anomaly detection, predefined split files cover three viewpoint configurations (straight only, straight plus 45 degrees, straight plus 60 degrees). A separate localization subset in YOLO format (the record title calls the labels bounding boxes) holds 954 images and 1,883 polygon annotations over four defect classes: surface gloss defect, excess thread, embroidery defect and broken thread. The current record is version 2, released in 2026 under CC BY 4.0.

## References

- [Mendeley Data](https://data.mendeley.com/datasets/sp99tbxchp)
- [Industrial Atlas page](https://www.indatlas.com/datasets/vina-embroidery/)

[⬅️ Back to Index](../README.md)
