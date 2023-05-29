# Gait Stride Length Estimation - Embedded Machine Learning

This repo is related to the  Machine Learning at the Extreme Edge ([ML@E2dge](https://mlate2dge.github.io)) project. It contains mainly a collection of (template) Jupyter Notebooks and Python scripts. 

**!!IMPORTANT!! This repo is still under construction.**

## Machine Learning Workflow

In the machine-learning workflow,  open-source software (e.g. Python, scikit-learn, TensorFlow/Keras) and MLOps (Machine Learning Operations) frameworks [Edge Impulse Studio](https://www.edgeimpulse.com/) and [Weights and Biases](https://wandb.ai/) are used.

![Machine Learning Workflow](./img/workflow.png)

## Project structure

[Cookiecutter Data Science](https://github.com/drivendata/cookiecutter-data-science)

## Datasets

- <a href="https://www.mdpi.com/2306-5729/6/9/95">TRIPOD — A Treadmill Walking Dataset with IMU, Pressure-Distribution and Photoelectric Data for Gait Analysis.</a> Justin Trautmann; Lin Zhou; Clemens Markus Brahms; Can Tunca; Cem Ersoy; Urs Granacher and Bert Arnrich.

- <a href="https://zenodo.org/record/7415759">DUO-GAIT: A Gait Dataset for Walking under Dual-Task and Fatigue Conditions with Inertial Measurement Units.</a> Zhou, Lin; Fischer; Eric; Brahms, Markus Clemens; Granacher, Urs; Arnrich, Bert

- Xsens - GAITRite dataset (private dataset)

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
