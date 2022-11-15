# Designing Data-intensive Applications

> General purpose of the book is to give you an idea.  



[toc]



Some words

- published in 2014, but still good since AWS out there since 2008.

- reduce the risk of **vendor lock-in**

- High level of understanding of the big picture, and why we choose one over another



# Chapter 1. The Big Picture







# Chapter 2. The Battle of the Data Model

> The limits of my language mean the limits of my world.

Data model是软件设计中重要的一环，咋样fulfill上一张的那些软件开发的一些原则，比较neat的solution是一层一层的封装, layer of layer of abstraction, example 如下:



## 2.1 Rivals of the Relational Model

乱成贼子noSQL, 带着document-based database为武器，准备颠覆几十年的relational database的王朝.

| Property                      | SQL database | NoSQL database |
| ----------------------------- | ------------ | -------------- |
| Data model                    |              |                |
| Structure                     |              |                |
| Schema                        |              |                |
| Query language                |              |                |
| Scalability                   |              |                |
| ACID transactions             |              |                |
| Ability to add new properties |              |                |
| 一些历史                      |              |                |





### 2.1.1 Object-relational mismatch

> 一般来说,

更好的理解SQL vs noSQL, 我们来用twitter工程师真实遇到的一个问题作为例子.

<img src="/Users/yixiangzhang/Documents/DE_course/book_data-intensive/assets/figure2-1.png" alt="Screenshot 2022-11-15 at 17.14.13" style="zoom:67%;" />

s

![Screenshot 2022-11-15 at 17.27.55](/Users/yixiangzhang/Documents/DE_course/book_data-intensive/assets/figure2-2.png)





### 2.1.2 Many-to-one and many-to-many replationship



### 2.1.3 Historical interlude



### 2.1.4 Relational vs document database today

> 有点outdated since the book published in 2014.





## 2.2 Query Languages for Data









## 2.3 Graph-like Data Models











# Chapter 3. Storage and Retrieval

