# runabq

runabq is a command tool that can execute multiple input data files of FEA software Abaqus in succession.
runabq can execute all the input data in the current directory with a simple command.


[![PyPI Version](https://img.shields.io/pypi/v/runabq.svg??style=flat)](https://pypi.org/project/runabq/)
![GitHub Actions](https://github.com/simulation-lab/runabq/workflows/GitHub%20Actions/badge.svg)
![CodeQL](https://github.com/simulation-lab/runabq/workflows/CodeQL/badge.svg)
[![MIT License](http://img.shields.io/badge/license-MIT-blue.svg?style=flat)](LICENSE)


## Installation

Anaconda, venv

```sh
$ pip install runabq
```



## Usage

Use the latest Abaqus version. That is, it executes the'abaqus' command internally.

```sh
$ runabq
```

Use the specify abaqus version.

```sh
$ runabq -v 2021
```

student edition

```sh
$ runabq -v 2021se
```

Use user subroutines and CPUs.

```sh
$ runabq user=sub.f cpus=5
```

Help

```
$ runabq --help
```

Enter code = "a" or blank to execute all the input files in the current directory. Default is "a".

```sh
$ runabq
files list:
     1: job1.inp
     2: job2.inp
     3: job3.inp
     a: all
     x: exit
code ? a
```

If you want to execute only a specific input file, enter numbers separated by ",".

```sh
$ runabq
files list:
     1: job1.inp
     2: job2.inp
     3: job3.inp
     4: test1.inp
     5: test2.inp
     a: all
     x: exit
code ? 1, 4
```

For consecutive numbers, enter the first and last numbers separated by ":".

```sh
$ runabq
files list:
     1: case1.inp
     2: case2.inp
     3: case3.inp
     4: job1.inp
     5: job2.inp
     a: all
     x: exit
code ? 1:3
```
