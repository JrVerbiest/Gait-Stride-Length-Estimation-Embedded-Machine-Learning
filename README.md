# Gait Stride Length Estimation - Embedded Machine Learning

**Work in progress.**

## Dataset

<a href="https://www.mdpi.com/2306-5729/6/9/95">TRIPOD — A Treadmill Walking Dataset with IMU, Pressure-Distribution and Photoelectric Data for Gait Analysis. Justin Trautmann, Lin Zhou, Clemens Markus Brahms, Can Tunca, Cem Ersoy, Urs Granacher and Bert Arnrich.</a>

**Abstract**

Inertial measurement units (IMUs) enable easy to operate and low-cost data recording for gait analysis. When combined with treadmill walking, a large number of steps can be collected in a controlled environment without the need of a dedicated gait analysis laboratory. In order to evaluate existing and novel IMU-based gait analysis algorithms for treadmill walking, a reference dataset that includes IMU data as well as reliable ground truth measurements for multiple participants and walking speeds is needed. This article provides a reference dataset consisting of 15 healthy young adults who walked on a treadmill at three different speeds. Data were acquired using seven IMUs placed on the lower body, two different reference systems (Zebris FDMT-HQ and OptoGait), and two RGB cameras. Additionally, in order to validate an existing IMU-based gait analysis algorithm using the dataset, an adaptable modular data analysis pipeline was built. Our results show agreement between the pressure-sensitive Zebris and the photoelectric OptoGait system (r = 0.99), demonstrating the quality of our reference data. As a use case, the performance of an algorithm originally designed for overground walking was tested on treadmill data using the data pipeline. The accuracy of stride length and stride time estimations was comparable to that reported in other studies with overground data, indicating that the algorithm is equally applicable to treadmill data. The Python source code of the data pipeline is publicly available, and the dataset will be provided by the authors upon request, enabling future evaluations of IMU gait analysis algorithms without the need of recording new data.

## Workflow

![Machine Learning Workflow](./img/workflow.png)

## Project structure

[Cookiecutter Data Science](https://github.com/drivendata/cookiecutter-data-science)

## Environment Setup

- Create environment: 

```
$ conda env create -f conda.yaml
```

- Activate environment:./pr 

```
$ conda activate gsl_model
```

- Update environment:

```
$ conda env update --name gsl_model --file conda.yaml
```
