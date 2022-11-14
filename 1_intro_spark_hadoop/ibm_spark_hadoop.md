# Intro to big data and Hadoop



## What is big data





## Impact of Big data

Objective:

- a
- IoT (internet of things)





### IoT - Internet of things

- An internet-enabled connected network of smart devices



### Major components of IoT

这个workflow就像T-box数据传输的轨迹一样

<img src="/Users/yixiangzhang/Documents/DE_course/1_intro_spark_hadoop/img/iot_schematics.png" alt="Screenshot 2022-11-12 at 22.47.13" style="zoom:80%;" />



## Parallel processing, scaling and data parallelism



- linear process vs parallel processing
- horizontal scaling (computer cluster)
- `fault tolerance`
  - 99.9% fault tolerance with Hadoop



## Big Data Tool and Ecosystem

- Identify key tooling categories within the big data eco-system
- Describe the role of each tooling category in the big data life cycle
- List major tools and vendors within each big data tooling category





- Data technologies
  - capture, process and share data
  - Hadoop, HDFS, Spark
  - MapResuce, Cloudera, Databricks

- Analytics and visualization
  - analyzed
  - Tableau, PowerBI
- Cloud providers
  - AWS, IBM, GCP and oracle
- NoSQL database
  - Store and process 
  - Mango DB, couchDB, Redis
- Programming tools
  - R, Python, SQL, Scala, Julia



## Open source and big data

- Explain the role of open source in big data





Open source license types:

- public domain
- permissive
- copyleft
- lesser genereal public license





### Hadoop brief intro

- hadoop plays a major role in open source big data projects
  - Hadoop MapReduce (被spark淘汰了)
  - Hadoop File System (HDFS)
  - Yet Another Resource Negoitiator (YARN)



## Hadoop 生态系统

还是很迷惑这个data eco-system, 搜了一下

- [Big data and Hadoop eco-system](https://www.youtube.com/watch?v=bAyrObl7TYE)
  - very concise version of big data and introduction to hadoop system
  - 实际上hadoop eco-system分成几个阶段
    - (Hadoop distributed file system) HDFS 分开来储存大数据
    - Hadoop mapreduce (parallel processing) 处理数据
    - 干净的数据
- [Hadoop in 5 mins](https://www.youtube.com/watch?v=aReuLtY0YMI)
  - problem: 没法efficiently储存big data
  - Storage unit: HDFS
    - split data in each data node
    - 用replication method来让其fault tolerance
  - Process unit: Mapreduce
  - Yarn
    - Resource manager
    - node manager
    - application master
    - container
  - Other family such as: Hive, pig, apache spark, flume

<img src="/Users/yixiangzhang/Documents/DE_course/1_intro_spark_hadoop/img/mapreduce.png" alt="Screenshot 2022-11-12 at 23.18.52" style="zoom: 67%;" />



- [Hadoop Ecosystem](https://www.youtube.com/watch?v=p0TdBqIt3fg) 这个讲的很具体，接下来根据这个视频理解下生态,



### Hadoop Overview

近些年来Hadoop生态越来越复杂，工具越来越多, 有部分功能是重合的.

- ![Screenshot 2022-11-12 at 23.23.03](/Users/yixiangzhang/Documents/DE_course/1_intro_spark_hadoop/img/hadoop_ecosys.png)



### 存储单元HDFS

- Hadoop HDFS
  - Namenode (master), datanode (slave)
  - ![Screenshot 2022-11-12 at 23.26.23](/Users/yixiangzhang/Desktop/Screenshot 2022-11-12 at 23.26.23.png)





### YARN

- YARN stands for Yet Another Resource Negoitator

<img src="/Users/yixiangzhang/Documents/DE_course/1_intro_spark_hadoop/img/yarn.png" alt="Screenshot 2022-11-12 at 23.26.23" style="zoom:67%;" />





### Mapreduce

- 功能为processes large volumes of data in a parallelly distributed manner, 这个处理的逻辑是不变的，虽然mapreduce这个tool在逐渐phase away.
- 具体流程firstly, maps out big data,shuffule and sort (比如shuffle all words togethers, from **apple banana apple orange banana** to **apple apple banana banana orange**). Hadoop 是直接写进hardware的 (slower), 详情见[map reduce documentation](https://hadoop.apache.org/docs/r1.2.1/mapred_tutorial.html).
- 和Apache Spark的功能几乎一致，但是spark写进ram里，而不是硬盘
  - Pulls it into RAM
  - writes into harddrive
  - reads it off hard drive
  - shuffles it around
  - writes it back to hard drive
  - pulls it off the hard drive and does the processing

![Screenshot 2022-11-14 at 08.38.34](/Users/yixiangzhang/Desktop/Screenshot 2022-11-14 at 08.38.34.png)



### Data ingestion

> scoop and flume are specific to hadoop. 通过api获得数据

#### Sqoop

- 

![Screenshot 2022-11-14 at 08.41.38](/Users/yixiangzhang/Documents/DE_course/1_intro_spark_hadoop/img/sqoop.png)

#### Flume

![Screenshot 2022-11-14 at 08.42.52](/Users/yixiangzhang/Documents/DE_course/1_intro_spark_hadoop/img/flume.png)



### Scripting

#### Pig 

<img src="/Users/yixiangzhang/Desktop/Screenshot 2022-11-14 at 08.45.28.png" alt="Screenshot 2022-11-14 at 08.45.28" style="zoom:67%;" />

#### Hive

![Screenshot 2022-11-14 at 08.47.06](/Users/yixiangzhang/Documents/DE_course/1_intro_spark_hadoop/img/hive.png)



### Spark

| -                   | Spark                                         | MapReduce                 |
| ------------------- | --------------------------------------------- | ------------------------- |
| language written in | scale                                         | java                      |
| Process             | 全在RAM中运行 (in memory computation of data) | 在RAM和hard drive来回读写 |
|                     |                                               |                           |
|                     |                                               |                           |
|                     |                                               |                           |



![Screenshot 2022-11-14 at 08.54.15](/Users/yixiangzhang/Documents/DE_course/1_intro_spark_hadoop/img/spark.png)

### Machine Learning (mahout)

- 正在phasing out and replaced with spark and python

  ![Screenshot 2022-11-14 at 09.01.11](/Users/yixiangzhang/Documents/DE_course/1_intro_spark_hadoop/img/mahout.png)

### Monitoring and management (Apache Ambari)

- AKA security <img src="/Users/yixiangzhang/Documents/DE_course/1_intro_spark_hadoop/img/ambari.png" alt="Screenshot 2022-11-14 at 09.02.28" style="zoom:67%;" />guard; traffic cop



### Streaming (kafka, storm)



![Screenshot 2022-11-14 at 09.05.00](/Users/yixiangzhang/Documents/DE_course/1_intro_spark_hadoop/img/kafka.png)



![Screenshot 2022-11-14 at 09.07.46](/Users/yixiangzhang/Documents/DE_course/1_intro_spark_hadoop/img/storm.png)



### Security

#### Ranger

![Screenshot 2022-11-14 at 09.09.03](/Users/yixiangzhang/Documents/DE_course/1_intro_spark_hadoop/img/ranger.png)

#### Knox

![Screenshot 2022-11-14 at 09.10.07](/Users/yixiangzhang/Documents/DE_course/1_intro_spark_hadoop/img/knox.png)

### Workflow system

#### OOZIE

- 和airflow很像，workflow scheduler system to manage Hadoop jobs
- triggered by time and data availability 



![Screenshot 2022-11-14 at 09.11.59](/Users/yixiangzhang/Documents/DE_course/1_intro_spark_hadoop/img/Oozie.png)





