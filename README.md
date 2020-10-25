# runabq

runabq is the execution script for abaqus jobs in current directory.
Runs the input files in the current directory continuously.


## Installation

To use the runabq package in a virtual environment, do the following.
This is the case when the name of the virtual environment is abq.

Anaconda

```sh
$ conda create -n abq python
$ conda activate abq

$ git clone https://github.com/simulation-lab/runabq.git
$ cd runabq
$ pip install -e .
```

venv

```sh
$ python3 -m venv abq
$ . abq/Scripts/activate

$ git clone https://github.com/simulation-lab/runabq.git
$ cd runabq
$ pip install -e .
```


## Usage

If there is a lot of Abaqus input data you want to execute in the current directory, execute the following command.
Use the latest Abaqus version. That is, it executes the'abaqus' command internally.

```sh
$ runabq
```

Use the specify abaqus version.

```sh
$ runabq -v 2020
```

Use user subroutines and CPUs.

```sh
$ runabq user=sub.f cpus=5
```

Help

```
$ runabq --help
```

Enter code = "a" to execute all the input files in the current directory.

```sh
$ runabq
files list:
     1: job1.inp
     2: job2.inp
     3: job3.inp
     a: all
     x: exit
code = a
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
code = 1, 4
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
code = 1:3
```
