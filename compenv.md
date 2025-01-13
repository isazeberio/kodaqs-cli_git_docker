---
title: Computational Environment
author: Chung-hong Chan
---

# Introduction

Although sharing of data and code is the essential first step for enabling computational reproducibility, the shared code must be able to run. In this unit, we will talk about the computational environment (or runtime environment). In Unit 4 and Unit 5, we will demonstrate several strategies to preserve and recreate a computational environment.

# Computational Environment

A program must be run in a compatible computational environment. When one shares code and data, it is important to document the computational environment (runtime environment) where the code is intended to run. Any deviation in the computational environment can either prevent the execution or produce different outputs.

A computational environment can be broadly broken down into hardware and software. We will skip the discussion on hardware because code written in popular programming languages (Python, R etc.) runs on most hardware environments [1].

## Software Layers

Using Schoch et al. (2024)'s definition, a computational environment can be divided into 4 layers

1. Operating System (e.g. Windows 10, Mac OS X 14.7.1, Ubuntu Linux 22.04)
2. System components (e.g. `libxml2`)
3. The exact version of the programming language (e.g. Python 3.10.0, R 3.6.3)
4. What and which version of the software libraries (e.g. `dplyr` 0.8.5)

As software might have some backward compatibility, it is likely that a slight variation in any of these 4 layers might not generate any issue. For example, a program written for Python 3.10.0 should run fine on Python 3.13.1, unless some deprecated features were used. But it is not a guarantee and software update can break existing code.

Therefore, when sharing code and data, it is essential also to document the computational environment for the code to run. An even better approach is to provide a way to recreate such a computational environment.

## Understanding your computational environment

### R

You can get the information about the current running R running session using this command: `sessionInfo()` (or from your shell: `Rscript -e "sessionInfo()"`). It lists out information about the OS, R version, and loaded R packages.

This is the output of my `sessionInfo()`

```
R version 4.4.2 (2024-10-31)
Platform: x86_64-pc-linux-gnu
Running under: Ubuntu 22.04.5 LTS

Matrix products: default
BLAS:   /usr/lib/x86_64-linux-gnu/openblas-pthread/libblas.so.3 
LAPACK: /usr/lib/x86_64-linux-gnu/openblas-pthread/libopenblasp-r0.3.20.so;  LAPACK version 3.10.0

locale:
 [1] LC_CTYPE=en_US.UTF-8       LC_NUMERIC=C              
 [3] LC_TIME=en_US.UTF-8        LC_COLLATE=en_US.UTF-8    
 [5] LC_MONETARY=en_US.UTF-8    LC_MESSAGES=en_US.UTF-8   
 [7] LC_PAPER=en_US.UTF-8       LC_NAME=C                 
 [9] LC_ADDRESS=C               LC_TELEPHONE=C            
[11] LC_MEASUREMENT=en_US.UTF-8 LC_IDENTIFICATION=C       

time zone: Europe/Berlin
tzcode source: system (glibc)

attached base packages:
[1] stats     graphics  grDevices utils     datasets  methods   base     

loaded via a namespace (and not attached):
[1] compiler_4.4.2
```

It says I am running R 4.4.2 on Ubuntu Linux 22.04.5. Several R packages are "attached" (or loaded). But it doesn't say the exact version of these packages. The R package [sessioninfo](https://doi.org/10.32614/CRAN.package.sessioninfo) provides better information (via `sessioninfo::session_info()`).

To list out all installed R packages, use `library()`. To get also the version information: `installed.packages()`.

### Python

You can get the information about the OS and Python version by reading the first line of output after launching `python` (or `ipython`) from your shell. This is an example output from me:

```
Python 3.10.12 (main, Nov  6 2024, 20:22:13) [GCC 11.4.0] on linux
Type "help", "copyright", "credits" or "license" for more information.
>>> 
```

It says I am running Python 3.10.12 on Linux. The Python package [watermark](https://pypi.org/project/watermark/), combined with `ipython`, is useful to display the version of all loaded packages.

```python
%load_ext watermark
import numpy
%watermark --iversions
```

To list out all installed Python packages via pip, run `pip list` (from your shell).

### Activity

Understand and document your computational environment via the commands introduced above.

# Summary

We discussed the four software layers of a computational environment. Also, several commands were introduced to get information on these four layers.

# Appendix

Installing ipython

```sh
pip install ipython
```

Installing watermark

```sh
pip install watermark
```

Installing sessioninfo

```sh
Rscript -e "install.packages('sessioninfo')"
```

# Footnotes

[1]: One notable exception is deep learning, for which GPUs are usually needed.
