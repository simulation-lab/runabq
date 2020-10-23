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

Specify the abaqus version.

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
     4: test1.inp
     5: test2.inp
     a: all
     x: exit
code = 1, 4
```

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
