# Linux command and shell script

It is very important to be familiar with linux and shell script for a couple of reasons:

- Datacenters (AWS, AZURE, GCP) are designed with linux server, you need to know them well to troubleshoot and controlt them via command line

- Programming languate and framework would change over time but bash and linux stays 4ever (prob also true for SQL)
- U need to be fluent in linux and shell to quickly learn frameworks quickly 

**Table of contents:**

[toc]



# Introduction to Unix and Linux



## Intro to Linux and Unix

**Outline:**

- what is an OS
- what is unix and linux





- `OS`: a bridge between software and hardware

- `Unix` is a family of operation systems
  - Example: the most famous one is Apple macOS
  - 1960s created in BELL lab, 1980s Unix rewritten in C
- `Linux` is a family of Unix-like OSs
  - Linux was developed as an effort to create a free, open-source Unix OS.
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

**keywords:** `linux layers`,`linux filesystem`





### Linux layers

linux consists of 5 layers illustrated in the figure below 

<img src="https://upload.wikimedia.org/wikipedia/commons/9/9f/Linux_kernel_and_Computer_layers.png" style="zoom:20%;" />



Linux has 5 layers shown below,

- `user`: the person 
- `application`: any software that lets you perform a task
  - system tools
  - programming languages
  - shells (没错，shell也是application的一种)
  - users apps (games, browser)
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

- Hybrid of GUI and command-line:
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





**Summary:**

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



## **Lab**: getting started with terminal



- `ls /`: return only the directory



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

**Objectives:**

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
  - `ls /` only returns directory. No files returned
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
  - 用空格键切换下一页

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

- `uniq`: prints input with consecutive repeated lines collapsed into a single, unique. 这个比较tricky, 因为他不会return unique value in the file. 它主要做以下的事情:

  ```bash
  # pets.txt
  cat
  cat
  dog
  dog
  hello
  dog
  
  # uniq pets.txt
  cat
  dog
  hello
  dog
  ```

  - `uniq pets.txt`并不能输出unique value in here
  - 想输出unique values的小技巧是用之后学到的pipe operator `|`, by doing `sort pets.txt | uniq`

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
- `paste`: merge lines from different files (default delimiter is tab) 实际上是做个horizontal concatenation
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

**Overview:**

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



## **lab**: compressing, networking commands (40 mins)

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





## Filters, pipes and variables

Objectvive:

- wha'ts pipes and filters
- explains and set shell and environment variables



### Pipes and filters

filters are shell commands:

- Filter command的定义是a command which can accept input from standard input and send output to standard output.

  - Takes input from standatrd input (`stdin` in this case keyboard)

  - send output to standard ouptu (`stdout` in this case terminal)

  - transform input data to output data

- 常见的filter command 包括: wc, cat, more, head, sort
- Filters can be chained together with pipe command 





pipe command `|`

- for chaining **filter commands**

- Example: `command1 | command2`
- output of command 1 is the input of command 2
- Example: `ls | sort -r` returns reverse sorted list of contents



### shell variables

- scope of shell variable is limited to shell

- `set` - list all shell variable

  

  定义一个shell variable 只需要`=` 但不要加上空格，accessing a shell variable则需要`$`

```bash
GREETINGS='HELLO'
echo $GREETINGS
```

当然你要移除shell variable用`unset GREETINGS`





### Environment variables

- Extend scopt from shell variable to environment variable with `export var_name`
  - 那也就解释了在Apahe Airflow里，你需要`export AIRFLOW=.` 将environment variable `AIRFLOW` 设置成当前
  - `env`: list all environment variables
    - `conda env list`: list it !
    - `env >> environment_variable.txt`: 将所有environment variable塞进`.txt`文件里
    - `env | grep 'air'`: 用pipe feature to chain command `env` and `grep` to grab environment variable with `air` in it. 

### Summary:

- 关于environment variable和shell variable的概念和差异，其实很像global and local variable之间的差异，但还是要找一些资源细致的阅读一下
- filters are shell commands
- The pipe operator `|` allows you to chain filter commands
- Shell variables can be assigned values with `=` and listed using `set`
- Environment variables are shell variables with extended scope to all child processes; create with `export`, list with `env`



## Exercise: pipe for bitcoin

too much reg-ex







## Useful features of bash

- metacharacters
- Quoting
- I/O redirection
- Command substitution
- Command line arguments
- Batch vs. concurrent modes of execution



- metacharacters:
  - `#`  comment out
  - `;` command separator
  - `*` filename expansion wildcard
    - `ls ./*.txt` returns all `.txt` files in the current directory`.`
  - `?`: single character wildcard in filename expansion
    - `ls /bin/?ash` returns `/bin/bash` and `/bin/dash`

这个wildcard concept在SQL中也有，

| -                             | SQL  | Bash |
| :---------------------------- | ---- | ---- |
| Single character              | _    | ?    |
| Arbitary number of characters | %    | *    |



- Quoting
  - `\` escape special character interpretation
    - `echo "\$1 each"` skips the `$`. 这个概念其实和latex中`\%` 才能输入百分号一样`%`，不然就会被默认为`%`是metacharacter
    - similarly, in markdown \ also works with ` to skip the code setting 
  - ` " "` interpret literally, but evaluate metacharacters
  - `' '` interpret literally



- I/0 redirection
  - refers to a set of features used for redirecting
  - `>`: redirect output to file
  - `>>` append output to file
  - `2>` redirect standard error to file
    - 比如说你没有装某个command, let's say `conda` 然后会给你报错，说`conda:command not found` 这时候你可以redirect standard error to a `.txt` 文件，进行报错内容的收集
    - `garbage 2 > err.txt` ? not availve on mac darwin?
  - `2>>` append standard error to file
  - `<` redirect file contents to standard input



- Command substitution
  - Replaces command with its output
  - $(command) or \`command\`
    - here=$(pwd)
  - 这个概念`command substitution`我不是很comfortable





- Command line arguments
  - a way to pass arguments to a shell script



### Batch vs concurrent modes

- batch mode: runs sequentially
  - `command1;command2`
- concurrent mode: runs in parallel
  - `command1 & command2`

> Tips: `ctrl + L` clears the whole screen 

## **Lab**: bash scripting (30mins)



### Exercise 2 quote

- backslash `\` removes the meaning of the special character that follows it.
  - `echo The symbol for multiplication is \*`
- single quote remove special  meanings of all special characters within them (except another single quote) 
  - `echo 'Following are some special characters in shell - < > ; " ( ) \ [ ]  '`
- double quote remove special meanings of all special characters within them except another **double quote**, **variable substitution** and **command substitution**

```bash
# this just returns as is
echo 'Current user name: $USERNAME'

# this return variable substitution
echo "Current user name: $USERNAME"
# this return command substitution
echo "My current directory is $(pwd)"

```



### Exercise 3 working with variable

`bash` 和`fish`有些许不同，我们接下来完成流程

1. 查看所有shell variable
2. 设置一个shell variable
3. 查看所有shell variable
4. 查看所有environmental variable
5. 升级为environment variable
6. 查看所有environmental variable
7. 删除这个variable

### Exercise 5 I/O redirection

| Symbol | Meaning                               |
| ------ | ------------------------------------- |
| <      | input direction                       |
| >      | output direction **(overwrite)**      |
| >>     | Append output **(append to the end)** |
| 2>     | Error redirection                     |





### Exercise 7: Command line arguments

Command line arguments are a very convenient way to pass inputs to a scirpt.

#### Exercise 7.1 create a simple bash that handles two arguments





#### Exercise 7.2 Find the total disk space usage





### Practice questions

- [ ] 记得有空做一下这五题practice





## Scheduling job with `cron`

objective:

- schedule crob jobs with crontab
- understand cron syntax
- view and remobe cron jobs



### Job scheduling

- schedule jobs to run automatically at certain times
  - Example: load script at midnight every night backup script to run every sunday at 2 am (isn't this how reminder work?"





- cron is a service that runs jobs
- crond (daemon) interprets 'crontab files' and submits jobs on cron
- A crontab (cron table) is a table of jobs and schedule data
- Crontab command invokes text editor to edit a crontab file



- `crontab -e` 打开cron table
- `m h dom mon dow command`
  - `m` for minute, h for hour, dom for day of month, mon for month, `dow` for day of week (0 for sunday, 1 for Monday)
  - Example: `30 15 * * 0 date >> sundays.txt`
    - `*` use of wildcard character for arbitary # of chars
    - any # of space is allowed 

```bash
# m   h  dom  mon dow   command
  30 15    *    *   0    date >> path/sundays.txt

  0   0    *    *   *    /cron_scripts/load_date.sh

  0   2    *    *   0    /cronscripts/backup_data.sh

# every sunday at 15:30pm append the current date to sunday.txt
# every midnight execute load_date.sh
# every sunday on 2:00am , save the job (word自动保存feature)
```

- `crontab -l` lists all cron jobs in the cron table





## Hands-on lab scheduling with `crontab`(20 mins)

略



## Q & A session

- what's the difference between environment and shell variable?
- `''` and `""` , what's the difference and could you give an example?
- command substitution `$(pwd)` and variable substitution `$PATH`



# Final Project and Final Exam

Objectives:

- develop a shell script using several linux commands, environment variables, pipes and filters
- Specify your shell script to run at specific time intervals using `crontab`
- Evaluate ur peer's sheel scripts and output using the provided rubric and grading scheme













