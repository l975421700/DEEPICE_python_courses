# Finse_data_analysis

This repository is prepared for FINSE Winter school from 20/03/2022 to 26/03/2022.
It is an introduction to climate data analysis with python.


## Prerequisite

Due to a large diversity of student background, we do not assume any previous experiences of students on these materials.
But we expect some extra reading if you are unfamiliar with some stuff.

## Downloading this Github repository

While you can download this repository as a ZIP file, we suggest you clone this repository.
The instructions are detailed below.

You need [git](https://git-scm.com/) installed on your computer. You can check whether it is installed with following command in terminal (MacOS) or console (windows).

    git --version

Create a folder 'finse_school' to store this repository and the associated data. If you do not undeerstand any of the following command, you can check with "man 'command'", e.g. "man mkdir".

    mkdir finse_school
    cd finse_school
    git clone https://github.com/l975421700/Finse_data_analysis


For addtional preparation before the school, please go through the files in the folder 'preparation' in this repository.


## Python environment management with conda

To ensure students have a standard platform for data analysis, we suggest using conda from miniconda to create a virtual environment, where you can install python, python packages, and other software packages. This is also a good working practice to have your own python environments on laptops/remote servers.

The advantages of using conda to manage different python virtual environments for different projects are briefly summarized below:

    A virtual environment helps to keep dependencies required by different projects separate by creating isolated python virtual environments for them.

    With conda, you can not only install python packages, but also many other programming packages, like the Climate Data Operators cdo.

    You can install any latest packages for your projects, and those can have extended functions and bug fixes.

    If you have only one base python environment, it is likely that after you upgrade one package, many of your codes will not run anymore due to the poor backward compatibility of packages.

## Installing miniconda

Download and install miniconda from https://docs.conda.io/en/latest/miniconda.html.

### For Windows

Download the installer

https://repo.anaconda.com/miniconda/Miniconda3-latest-Windows-x86_64.exe

Install for all users when prompted.

### For Linux

Download the installer:

https://repo.anaconda.com/miniconda/Miniconda3-py39_4.11.0-Linux-x86_64.sh

In your terminal window, run:

    bash Miniconda3-py39_4.11.0-Linux-x86_64.sh

Read and follow the prompts.


## Activate conda from miniconda

### For Windows

You can search for the app "Anaconda Prompt (Miniconda3)" and open it.

### For MacOS

Find the path to the installed miniconda3, e.g. "/Users/${your_username}/opt/miniconda3/". Then activate it:

$ source ${your_path_to_miniconda3}/bin/activate

e.g. $ source /Users/gao/opt/miniconda3/bin/activate

### For Linux and remote servers (e.g. HPC)

In the terminal type

    conda activate

you should see (base) appear at the start of the terminal output

## Create a virtual environment using conda

Although python is already installed in the "base" environment of miniconda3, we will create a new python environment for this exercise. After you activate conda, you can use following commands to get more information about it:

    conda --help
    conda info

### Create a virtual Environment named "training" and activate it:

    conda create --name training
    conda activate training

### Install python and python packages

Install python in the virtual Environment "training". It is recommended to use 'conda-forge' channel to ensure consistency across packages.

    conda install -c conda-forge python=3.10.0

Then install all required packages in this exercise:

    conda install -c conda-forge numpy
    conda install -c conda-forge matplotlib
    conda install -c conda-forge cartopy
    conda install -c conda-forge netcdf4
    conda install -c conda-forge jupyter
    conda install -c conda-forge jupyterlab
    conda install -c conda-forge xarray
    conda install -c conda-forge dask

If you are using MacOS or Linux, you can consider installing mamba, which is faster than conda when installing packages. But it does not seem to work easily with Windows during our test.

## Other useful command

List available conda environments

    conda env list

List installed packages in current environment

    conda list

Don't run, unless you wanna remove the conda environment

    conda env remove -n training

Update conda

    conda update -n base -c defaults conda

Remove unused packages and caches.

    conda clean -t -i

## Launch python

Firstly, activate the virtual environment 'training'.
check where python is on your system.

### Windows

Check all python interpreter paths:

    where python

It will output several paths, and the first should be something like this: "C:\Users\gao.conda\envs\training\python.exe".

Check the version of python:

    python -V

You should see "Python 3.10.2"

### MacOS or Linux

Check current python interpreter path:

    which python

Check the version of python:

    python -V

You should see "Python 3.10.2"

## Use python

There are many ways to use python, we will only list some of them:
### 1, In terminal

Enter python with:

    python

or

    ipython

You will see ">>>", following which you can type in python scripts. And exit with:

    exit()

### 2, Using one of the Integrated Development and Learning Environment (IDLE):

    Visual Studio Code

pros: it works very good with supercomputers or remote servers. It can also be used for other programming languages. (my personal choice)

cons: deep initial learning curve.

    Spyder

pros: easy to use, quite popular.

cons: did not work well with supercomputer or remote servers (tested one year ago).

    Atom

Similar to Visual Studio Code, not tested.

    PyCharm

The Python IDE for Professional Developers, not tested.

### 3, Using JupyterLab

It is very good for illustration and thus adopted for this training school. Additional pros and cons are listed below:

Pros

    Jupyter supports over 40 programming languages, including Python, R, Julia, and Scala.
    It is convenient to share reproducible notebook.
    Your code can produce rich, interactive output: markdown, HTML, images, videos, LaTeX, and custom MIME types.
    As it can produce rich text, we use it for our documentation.

Cons

    Jupyter is desinged based on ipython. It can be slightly slower than ipython in some conditions.

For more information please refer to the website of Jupyter.

Ensure that you activate the virtual environment 'training'. Launch a jypyter lab session in the folder 'finse_school': (Note the dot following 'jupyter lab' means current directory and is necessary.)

    cd ${your_path_to_finse_school}

You might need to use '𝑝𝑢𝑠ℎ𝑑

{your_path_to_finse_school}' on Windows.

    $ jupyter lab .

## Problem Solving

In the event of a module not found/dll error in windows when opening one of the jupyter notebooks, shutdown jupyter in the anaconda prompt and run the following

    conda install -c conda-forge python=3.10.2

install the update and restart jupyter labs





