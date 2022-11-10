# Linux command and shell script

It is very important to be familiar with linux and shell script for a couple of reasons:

- Datacenters (AWS, AZURE, GCP) are designed with linux server, you need to know them well to troubleshoot and controlt them via command line

- Programming languate and framework would change over time but bash and linux stays 4ever (prob also true for SQL)
- U need to be fluent in linux and shell to quickly learn frameworks quickly 

**Table of contents:**

[toc]



# Introduction to Unix and Linux



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





# Introduction to Linux Commands





## Overview of Common Linux Shell Commands

Objective:

- what a shell is
- list shell command application
- common shell commans

### What is shell?

- user interface for running commands
- scripting and interactive language
- Default shell is Bash
  - Many other shells includes: `sh`, `zsh`,`tcsh`,`zsh`, and `fish`

> Tip: shell中 hypen用在单字前面`ls -l`，double hypheny用在完整的字前面 `bash --help`

### Applications

- getting information
- navigating and working with files and directories
- printing files and string contents
- compression and archiving
- **performing network operations**
- **monitoring performance and status**
- Running batch jobs (ETL operation)







## Commands: Information

Objectives:

- find user information
- determining OS info
- analyze disk usage
- describe and verify system health
- list running process
- Execute additional miscellaneous commands



Let's take a look at these commands

- `whoami`: return user name
- `id`:userid and group id
- `uname`: uname代表着 (Unix Name) reutrn OS information
  - `uname -v`
  - `uname -s -r`
- `ps`: ps stands for (process status). display runnging processes and their identification number ([PID](https://www.google.com/search?q=what%27s+PID+in+terminal&client=safari&rls=en&sxsrf=ALiCzsbJPL5sRIcyL0LToYdALabPwBkm0g%3A1668089528458&ei=uAZtY8jAG62iptQPyoGJyAo&ved=0ahUKEwjI_K_e5aP7AhUtkYkEHcpAAqkQ4dUDCA4&uact=5&oq=what%27s+PID+in+terminal&gs_lcp=Cgxnd3Mtd2l6LXNlcnAQAzIGCAAQFhAeMgUIABCGAzIFCAAQhgMyBQgAEIYDMgUIABCGAzIFCAAQhgM6CggAEEcQ1gQQsAM6CggAEIAEEAoQiwM6BwgAEIAEEAo6CAgAEJECEIsDOgUIABCRAkoECE0YAUoECEEYAEoECEYYAFDuA1i9EGC8EmgBcAF4AIABcIgB1AiSAQM5LjOYAQCgAQHIAQa4AQLAAQE&sclient=gws-wiz-serp))
- `top`: 代表着table of processes
- `df`: mounted file systems
  - `df -h`
- `man`: reference manual
  - `man echo`
- `echo` print in the world the linux
- `date`:today's date



> Tip: in linux manual, if you see something in the square bracket like `id -F [user]` , it means it is optional.



## Commands: File and Directory Nav

- `ls`
  - `ls -l`: l for long version, get everything from the child directories
- `find`: find files in directory tree
  - `find . -name "a.txt"`: 代表着找到所有current directory中`.`, 名字叫做a.md的文件
- `pwd`: stands for **print working direcotry**
- `cd`: change directory



## Commands: File and Directory Management

- `mkdir`: make an empty directory
- `rm`: rm remove files

- `rmdir`: remove directory 专门用来删除empty direcotry
- `touch`: create empy file, update file date (last modified)
- `cp`: copy file
  - 如果只是要复制一个file, 那么`cp [source] [destination]` with `cp README.md /dest`
  - 如果要复制一个direcotry 需要用`cp -r`  这里的`-r`代表着recursively
  - 有一个常用的需求就是把上一级的文件移动到current directory, 可以用`cp ../README.md .`
    - Source`../README.md`
    - Destination `.`
- `mv`: move a file or directory
- `chmod`: change or modify file permissions. 这是很重要的一点
  - 如果你在terminal中输入`ls -l README.md` the output would be `-rw-r--r-- 1 [user] [group] [date] [filename]`其中前几个characters代表三组权限
    - permission for user (user permission)
    - permission for members of the file's group (group permission)
    - Any1 not in the first two categories (other permission)
  - letter means:
    - `r`: read permission
    - `w`: write permissions
    - `x`: execute permission. If the files is a script or a program, it can be run.
    - `---` : means no permissions granted
    - `rwx` :means all permission granted
  - For more, please see [here](https://www.howtogeek.com/437958/how-to-use-the-chmod-command-on-linux/).



## Hands-ON lab: information, file and directory commands (40 mins)

略, 晚上做



## Commands: Viewing File Content

**Objectives:**

- View the contents of a file in useful ways
- Determine line, word, and character counts



- `cat`: `cat` is short for **catenate** which means to link together or form into a catenated series. See **concatenate**!!! `cat` print entire file contents to standard output
- `more`: print file contents page-by-page (current terminal page)
- `head`: print first N lines of file. default to 10.
  - `head -n 3 README.md` print first three
- `tail`: print last N lines of file (pandas.dataframe估计是借鉴着bash)

- `wc` : return count of **characters, words, lines** in file
  - `wc -l`: return only line count
  - `wc -w`: return only word count 



## Commands: customizing view of file contents

**Objective:**

- Create a line-by-line sorted view
- create a view with repeated lines excluede
- extract lines containing a specified pattern
- extract slices and fields from each line



这里你一可以create一个`pets.txt` with `touch pets.txt` then `nano pets.txt`输入以下内容

```markdown
dog
cat
cat
elephant
zebra
monkey
rhino
alligator
```

然后开始进行一些customized viewing, 这其实和sql的本质很像，进行一些row filtering, aggreagate stat stuff. 

- `sort`: sort lines in a file
  - `sort -r pets.txt` sort in reverse order
- `uniq`: filter out repeated lines
  - `uniq pets.txt`
- `grep`: `grep` stands for **global regular expression print** that returns lines in file matching pattern

学习正则，需要用以下的example `touch people.txt` 然后输入

```
Jensen Ackles
Andre 3000
Naveen Andrews
Jensen Atwood
Tyler Bachtel
Penn Badgley
Simon Baker
Christian Bale
Eric Balfour
Eric Bana
Alex Band
Antonio Banderas
Ike Barinholtz
Ben Barnes
```

- `grep` examples:
  - `grep ic people.txt` returns the line having `ic` 
  - `grep -i ic people.txt` returns the line having `ic` , `Ic`, `iC` or `IC` 
    - Note: `-i` stands for `case insensitive`
- `cut`: extracts a section from each line
  - `cut -c 2-9 people.txt`: return character, 2 to 9 digits (这里计算是从1开始)
  - Example: 你想找到last name for each line
    - `cut -d ' ' -f2 people.txt`: 
- `paste`: merge lines from different files (default delimiter is tab)
  - tab delimiter
    - `paste first.txt last.txt`
  - other delimiter `-d` option for delimiter
    - `paste -d "," first.txt last.txt`





## Commands: File Archiving and Compression

**Objective:**

- Distinguish file archiving from file compression
- Create archived files and unpack them
- Apply commands to compress, decompress, and extract fiels from archieves





**Archives:**

- Store rarely used information and preserce

- Archives are a collection of data files and directories as a single file

- Make the collection more portable and serve as a backup in case of loss or corruption

  Archive process的流程图如下 ：

```mermaid
flowchart LR
	tar --> bundle
	bundle --> compress
	compress --> done
```

**File compression:**

- Reduce file size by reducing information redundancy
- Preserves storage space, speeds up data transfer, and reduces bandwidth load

Compress process的流程图如下 ：

```mermaid
flowchart LR
	zip --> compress
	compress --> bundle
	bundle --> done
```



- `tar`: `tar` stands for tape archive. archive a set of files
  - `tar -cf notes.tar notes`
- `zip`: compress files and directories to an archive
- `unzip`: extract files from a compressed zip archive





## Commands: Network

> 这张要重点学习, 为了转行DE

Overview:

- Examine ur network configuration
- Evaluate the stability of a URL connection
- Identify and retrieve data from a URL





- `hostname`: print host name
  - defatule to username.local

- `ping`: send **ICMP**(一种传输协议) packets to URL and print response
- `ifconfig`: display or configure system network interfaces
  - `ifconfig eth0`: info about ethernet adapter
- `curl`: transfer data to and from URL(s) and support many protocals
  - `curl www.google.com` print the `html` of the landing page
  - `curl www.google.com -o google.txt` h 
- `wget`: (web get) download files from a URL
  - more focused than `curl` , supports recursive file downloads



## Hands-ON lab: compressing, networking commands (40 mins)

略







# Introduction to shell scripting

终于过了basic shell command,  要到写shell代码的时候了, 天道酬勤，我一定可以的. 

Learning objective for this sections are

- Describe `shebang` interpreter directive
- Use pipes and filters
- Create and work with shell environment variables
- Schedule cron jobs with `crontab` and understand `cron` syntax
- Perform command substitution
- Execute commands in concurrent mode





## Shell Scripting Basics

Objective:

- Outline what a script is 
- list use cases for scripting
- Describe the `shebang` interpretive directive
- Create and run a simple hello_world shell script





### What is a script

- sciprting languate are not compiled and interpreted at runtime
- Slower to run but develop fast



### What is a script used for

- widely used to automate processes
- ETL jobs, file back-ups and archiving, system admin
- Used for application integration, plug-in development, web apps, and many other tasks



### Shell scripts and the `shebang`

- Shell script: executable text file with an **interpreter direvtive**, also called `shebang` directive of the following form:
  - **#!interpreter [optional-arg]**
    - `interpreter`: path to an executable program
    - `optional-arg`: single argument string

Shell script directives:

```shell
#!/bin/sh
#!/bin/bash
```

Python (python is also a scripting language):

```python
#!/usr/bin/env python3
```





### `Helloworld` shell script

make a file

```bash
touch hello_world.sh
echo '#! /bin/bash' >> hello_world.sh
echo 'echo hello world' >> hello_world.sh
```



make it executable

```
ls -l hello_world.sh
chmod + x hello_world.sh
ls -l hello_world.sh
```

The three groups are user, group, all users in `-rw-rw-r--`

```
./hello_world.sh
```



## Hands-on Lab: getting started with shell scripting (30mins)

略















