# Calculating distances from uncertain parallax measurements

This is a Python program that plots measured stellar distances from simulated parallaxes. The plot demonstrates that one can not just use the standard distance = 1/parallax formula when parallax
measurements are uncertain or negative, which is true for most stars in Gaia's DR2 catalog. Instead, the parallaxes need to be inferred using statistical inference.

This is a recreation of Figure 3 in [Luri X et. al (2018)](https://arxiv.org/abs/1804.09376).


## Setup

Use the following steps to install Python environment and run the code.

* Extract the code.zip file into a directory and change the directory:

```
cd code
```

* Install [Miniconda](https://docs.conda.io/en/latest/miniconda.html).

* Create a Conda environment.

```
conda create --name asp3231assignment1 python=3.7
```

* Activate the environment:

```
conda activate asp3231assignment1
```

* Install Python libraries listed in `requirements.txt` file:

```
pip install -r requirements.txt
```

* Finally, run Jupyter and open the `q3.ipynb` notebook:

```
jupyter notebook q3.ipynb
```


## Cleaning up

When you finished running the code, stop Jupyter with <Ctrl-C> and remove the Conda environment:

```
conda deactivate
conda env remove -n asp3231assignment1
```

## License

This code is in [Public Domain](LICENSE).
