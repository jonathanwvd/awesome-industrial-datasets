# Severstal Steel Defect Detection

**Summary:** In this competition you will be predicting the location and type of defects found in steel manufacturing. Images are named with a unique ImageId. You must segment and classify the defects in the test set.

| Parameter | Value |
| --- | --- |
| **Dataset** | Severstal Steel Defect Detection |
| **Domain** | Manufacturing & Production |
| **Asset / Process** | Steel / Metal Surfaces |
| **Modality** | Image |
| **Task** | Defect Detection; Defect Segmentation; Classification; Quality Prediction |
| **Annotation** | Sample Label; Class Label |
| **Source Type** | Real Production / Field |
| **Access** | Kaggle; Competition; Login Required |
| **Size** | 18,076 files |
| **Year** | 2019 |
| **License** | Competition Terms |

## Description

In this competition, the goal is to predict the location and type of defects found in steel manufacturing. Each image might have no defects, a defect of a single class, or defects of multiple classes. For each image, you must segment defects of each class (ClassId = [1, 2, 3, 4]). The segment for each defect class will be encoded into a single row, even if there are several non-contiguous defect locations on an image.

The dataset consists of folders of training images (train_images/) and test images (test_images/) which participants are to segment and classify. Annotations for training images are provided in train.csv, which includes segments for defects with ClassId values from 1 to 4. Additionally, there is a sample submission file that shows the correct format.

Submissions to this competition must be made through Kernels, which will rerun automatically against the entire Public and Private test sets after submission. Participants need to accept the competition rules to access the data. The dataset includes 18,076 files totaling approximately 1.7 GB in size, with image files and CSV annotations.

## References

- [Severstal Steel Defect Detection - Kaggle](https://www.kaggle.com/c/severstal-steel-defect-detection/data)
- [Competition Rules](https://www.kaggle.com/c/severstal-steel-defect-detection/rules)
- [Evaluation Details](https://www.kaggle.com/c/severstal-steel-defect-detection/overview/evaluation)
- [Kernels Requirement Page](https://www.kaggle.com/c/severstal-steel-defect-detection/overview/kernels-requirements)

[⬅️ Back to Index](../README.md)
