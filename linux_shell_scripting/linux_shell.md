# Linux command and shell script

It is very important to be familiar with linux and shell script for a couple of reasons:

- Data centers are designed with linux server, you need to know them well to troubleshoot and controlt them via command line

- Programming languate and framework would change over time but bash and linux stays 4ever (prob also true for SQL)
- U need to be fluent in linux and shell to quickly learn other skills

**Table of contents:**

[toc]



# Introduction to Linux and Unix



## Intro to Linux and Unix

Outline:

- what is an OS
- what is unix and linux





- `OS`: a bridge between software and hardware

- `Unix` is a family of operation systems
  - Example: the most famous one is Apple macOS
  - 1960s created in BELL lab, 1980s Unix rewritten in C
- `Linux` is a family of Unix-like OSs
  - Linux was developed as an effort to create a free, open source Unix OS.
  - Linux features:
    - Free and open source
    - secure
    - multi-user
    - multitasking
    - portability
  - 1980s GNU developed, 1991 Linux Kernel,  1992 Linux OS born bia GNU + Linux Kernel, 1996 Tux the penguin



Common cases for Linux today:

- Android
- supercumputers
- data centers and cloud servers
- PCs



## Overview of Linux Architecture

Objectives:

- list the layers in a Linux
- Describe the function of each layer in a linux system
- describe the linux file system



### Linux layers

linux consists of 5 layers illustrated in the figure below 

<img src="https://upload.wikimedia.org/wikipedia/commons/9/9f/Linux_kernel_and_Computer_layers.png" style="zoom:20%;" />



Linux has 5 layers shown below,

- `user`: the person 
- `application`: any software that lets you perform a task
  - system tools
  - programming languages
  - shells
  - users apps(game, browser)
- `OS`: controls the jobs and programs vital to health and stability
  - Also assigns software to users
  - help detect errors and prevent failures
  - performs file management system
- `kernel`: lowest-level software in system and starts on boot remains in memory. For more info, [check here](https://www.youtube.com/watch?v=JDfo2Lc7iLU).
  - Key jobs:
    - memory management
    - process
    - device driver
- `hardware`: consists of all physical electronic devices on ur PC
  - Such as
    - CPU
    - RAM
    - Storage
    - Screen
    - 外接设备比如USB



### linux tree-like filesystem

- `filesystem`: collection of files in your system
- begins at root directory `/`
  - 这门课cover的五个如下
    - `/bin`: 
    - `/usr`: contains user program
    - `/home`: personal files
    - `/media`: 
    - `/boot`

 

## Linux distribution

**Objective**

- Describe what a linux distribution is
- Differentiate between common linux distribution





### What is a linux distribution

- a specifc flavor of linux OS also know as distro for short.
- uses the linux kernel
- hundreads of linux distros tailored for different audiences or tasks



### Linux distro differences

- system utilities
- GUI
- A specific set of shell commands
- different support
  - community vs enterprise
  - LTS vs rolling release
- Examples
  - `Debian` first release in 1993 as a stable, fully open source and supports many computer architectures
  - `ubuntu` first release in 2004, it is a debian-based and managed by Canonical
    - three distributions:
      - ubuntu desktop
      - Ubuntu server
      - Ubuntu Core
  - `Red Hat linux`: a core linux distro, stable reliable and fully open source. Managed by Red Hat
  - `Fedora` supports many architectures, sponsored by `Red Hat`
  - `SUSE Linux Enterprise (SLE)`: supported by german company
  - `Arch Linux`: do-it-yourself approach, highly configurable. You need to have strong understanding of Linux and system tools



**Summary:**

- linux distro differs by UIs, their shell applications and how the OS is supported and built
- the design of a distro is crated toward its specific audience



## Linux Terminal Overview

**Objective:**

- Describe what the linux is
- Describe what a Linux terminal is
- Explain how a Linux terminal and shell work together
- Use a Linux terminal to navigate directories



### Overview of the Linux Shell

- The shell is an **OS-level application** that interprets commands 本质上shell是一个application (application layer for linux)
  - moving and copying files
  - Writing to and reading from files
  - Extracting and filtering data
  - Searching for data
-  Shells 有许多versions (解释了VS code下面的zsh, bash啥意思):
  - Bash
  - Zsh



### Overview of a Linux terminal

- An application you can use to interact with the Linux shell
- enters commands and receive info



### Paths in the Linux filesystem

- `a/b` the file or directory named `b` inside the directory name `a`

- Note: mac is a Unix-based OS so it might be a bit different from other linux distro
- Special paths :
  - `~`: home directory
  - `/`: root directory
  - `.`: current directory
  - `..`: parent directory of the current directory



## Creating and Editing Text Files

Objective:

- List popular text editors for linux
- Describe a popular GUI-based text editor
- Use command-line editors to work with a file



### Popular text editros

There are two types:

- `Command-line text editors`:
  - GNU nano
  - vi
  - vim
- `GUI-based text editors`
  - gedit

- Hycrid:
  - emacs





### Features of `gedit`

- `gedit` is a general-purpose editor (一般在大多数linux distro都预安装了)
  - Intergrated file browser
  - undo and redo
  - search and replace (it supports regex!! I hated regex)
  - extensibility with extra stuff
  - syntax coloring
- is there an alternative gedit for mac user?



### Feature of GNU nano

- Command-line text editor
  - similar to gedit but in command line



### Features in vim

- `Vim` is a traditional and very powerful command-line editor 
- Two basic modes:
  - `insert` mode and `command` mode





Summary:

- 有许多edior, 主要分command-line edior 和 GUI edior
- popular ones include vim, nano and gedit.



## Installing software and Updates

Objective:

- Describe packages and packages managers
- Differentiate between packages for `deb-` and `RPM-based` distros
- Use a package manager to install updates
- Use a package manager to install software



### Packages and package managers

- Packages
  - **Packages is just archived files**
  - For installing new software or updating existing software

- Package managers:
  - manage the download and installation of packages
  - available for different linux distros
  - can be GUI-based or command line tools

### DEB and RPM packages

- package for linux OS
- `.deb` files
  - for debian-based distribtion
- `.rpm` files
  - for read hat package manage
- `deb` and `rpm` are equivalent with `aline` such as:
  - rpm to deb `alien <package-name>.rpm`
  - deb to rpm `alien -r <package-name>.deb`
  - `-r`???



### Package managers

- Benefits:
  - automatically resolve dependcies
  - notify you when updates are available
- Linux distro package managers includes **Update Manager** for deb-based linux and **packagekit**



#### Debian-based `Update Manager`

- It has 
  - a GUI tool (ubuntu里有,更新系统的)
  - command line: `apt`
    - `sudo apt update` to find available package for your distro and update
      - list each availbe package
      - build dependcies
      - let your choose



#### RPM-based `PackageKit`

-  GUI tool: `PackageKit`
- command line: `yum`
  - `yum`: stands for yellowdog updater
  - `sudo yun update`:



### Other software package managers

- let's say for python: `pip` and `conda`
- installing the pandas library
- `pip install pandas`: 一般以下四部
  - Search for latest `pandas`
  - download `pandas`
  - check for dependencies and update
  - install `pandas`
  - display the new software version numver



## Hands-on lab with Linux (1-hour)





## Summary & Highlights

- The linux system consists of five key layers: user, application, OS, kernel, and software
- **kernel is the lowest-level software** and it enables application to interact with ur hardware
- The **shell is an OS-level application** for running commands, terminal is the UI for the shell.







