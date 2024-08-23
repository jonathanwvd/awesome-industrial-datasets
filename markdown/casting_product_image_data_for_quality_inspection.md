# Casting Product Image Data for Quality Inspection

**Summary:** Industrial data,casting manufacturing product, quality inspection, automation.

| Parameter | Value |
| --- | --- |
| **Name** | Casting Product Image Data for Quality Inspection |
| **Labeled** | Yes |
| **Time Series** | No |
| **Simulation** | No |
| **Missing Values** | No |
| **Dataset Characteristics** | Image |
| **Feature Type** | Image Data |
| **Associated Tasks** | Classification |
| **Number of Instances** | 7348 |
| **Number of Features** | INA |
| **Date Donated** | INA |
| **Source** | Kaggle |

## Dataset Information

Casting is a manufacturing process in which a liquid material is usually poured into a mould, which contains a hollow cavity of the desired shape, and then allowed to solidify. The reason for collecting this data is casting defects! Casting defect is an undesired irregularity in a metal casting process. There are many types of defects in casting like blow holes, pinholes, burr, shrinkage defects, mould material defects, pouring metal defects, metallurgical defects, etc. Defects are an unwanted thing in the casting industry. To remove these defective products, all industries have their quality inspection department. However, the main problem is that this inspection process is carried out manually. It is a very time-consuming process and, due to human accuracy, it is not 100% accurate. This can cause the rejection of the whole order, creating a big loss for the company. We decided to make the inspection process automatic, and for this, we need to develop a deep learning classification model for this problem.

## Contain

These all photos are top view of submersible pump impeller (google search for better understanding). The dataset contains a total of 7348 image data. These all are the size of (300*300) pixels grey-scaled images. In all images, augmentation has already been applied.

Also uploaded images size of 512x512 grayscale. This dataset is without augmentation. This contains 519 ok_front and 781 def_front impeller images.

For capturing these images requires stable lighting, for this, we made a special arrangement.

There are mainly two categories:
1) Defective
2) Ok

For making a classification model we have already split the data for training and testing into two folders. Both train and test folders contain def_front and ok_front subfolders.

Train: def_front have 3758 and ok_front have 2875 images
Test: def_front have 453 and ok_front have 262 images.

## Tags

Quality inspection, Metal casting, Image classification, Defect detection, Manufacturing process

## References

- [Kaggle Dataset](https://www.kaggle.com/datasets/ravirajsinh45/real-life-industrial-dataset-of-casting-product)

[⬅️ Back to Index](../README.md)
