# runabq

runabq is the execution script for abaqus jobs in current directory.
Runs the input files in the current directory continuously.


## Install

```sh
$ pip install runabq
```


## Example

When using the latest version.

```sh
$ runabq
```

Abaqus version 2018, all job

```sh
$ runabq -v 2020
```

User subroutine and cpus, etc.

```sh
$ runabq user=sub.f cpus=5
```

All input file in current directory.

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

Specify input file.

```sh
$ runabq
files list:
     1: job1.inp
     2: job2.inp
     3: job3.inp
     a: all
     x: exit
code = 1,3
```
