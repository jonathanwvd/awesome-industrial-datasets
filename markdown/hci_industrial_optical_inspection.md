# HCI Industrial Optical Inspection

**Summary:** HCI Heidelberg weakly supervised industrial optical inspection dataset with image-level labels for training; provides industrial texture images of defective and non-defective surfaces for weakly supervised defect detection research.

| Parameter | Value |
| --- | --- |
| **Dataset** | HCI Industrial Optical Inspection |
| **Domain** | Materials & Metrology; Manufacturing & Production |
| **Asset / Process** | Surface Defects |
| **Modality** | Image |
| **Task** | Anomaly Detection; Anomaly Localization; Defect Detection; Defect Segmentation |
| **Annotation** | Pixel Mask; Fault Type Label; Sample Label; Class Label |
| **Source Type** | Real Lab / Testbed |
| **Access** | Official Portal |
| **Size** | Multiple industrial texture classes; training images with image-level labels (weak supervision) and test images with pixel-level ground truth |
| **Year** | 2015 |
| **License** | Information not available |

## Description

The HCI Industrial Optical Inspection dataset was created by researchers at the Heidelberg Collaboratory for Image Processing (HCI) at the Interdisciplinary Center for Scientific Computing (IWR), Heidelberg University. It was designed to benchmark weakly supervised learning approaches for industrial surface defect detection.

In weakly supervised settings, only image-level labels (defective vs. non-defective) are available during training, without pixel-level defect annotations. The test set is annotated at the pixel level for evaluation of defect localization. This setup simulates realistic industrial inspection scenarios where per-pixel annotation of defects is expensive.

The dataset contains images of industrial textured surfaces across multiple categories, with varying defect types. It has been used to study semi-supervised and weakly supervised learning methods for quality inspection, including convolutional neural network-based approaches that leverage limited annotation.

## References

- [HCI Industrial Optical Inspection (Heidelberg University)](https://hci.iwr.uni-heidelberg.de/content/weakly-supervised-learning-industrial-optical-inspection)

[⬅️ Back to Index](../README.md)
