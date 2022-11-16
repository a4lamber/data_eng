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

| Property                      | SQL database                                                 | NoSQL database                                              |
| ----------------------------- | ------------------------------------------------------------ | ----------------------------------------------------------- |
| Data model                    | relational                                                   | Non-realational                                             |
| Structure                     | Table-based, with columns and rows                           | Document based, key-value pairs, graph or wide-column       |
| Schema                        | Predifined and strict schemma; datatype is same across each column; | A dynamic schema or schemaless; 数据不需要是相同的data type |
| Query language                | SQL                                                          | dependent on database                                       |
| Scalability                   | vertical scaling                                             | horizontal scaling                                          |
| ACID transactions             | Supported                                                    | suppored, depending on the specific NoSQL database          |
| Ability to add new properties | Need to alter the schema first                               | Possible without disturbing anything                        |
| 一些历史                      | ~1970 IBM engineer proposed it and popularize over next 30 years due to LAMP |                                                             |





### 2.1.1 Object-relational mismatch

> 一般来说,

更好的理解SQL vs noSQL, 我们来用linkedin工程师真实遇到的一个问题作为例子. 你可以从query和储存两个方面来assess能力

|       | SQL                                                          | JSON                                            |
| ----- | ------------------------------------------------------------ | ----------------------------------------------- |
| 储存  | 建立schema麻烦，而且以后增加新的section, 需要新添加和修改你的ERD | tree-like structure, 只需要重新append一下就好了 |
| query | multiple table join!!                                        | just one simple query                           |



<img src="/Users/yixiangzhang/Documents/DE_course/book_data-intensive/assets/figure2-1.png" alt="Screenshot 2022-11-15 at 17.14.13" style="zoom:67%;" />



![Screenshot 2022-11-15 at 17.27.55](/Users/yixiangzhang/Documents/DE_course/book_data-intensive/assets/figure2-2.png)



同时，你们注意到了region_id, industry_id都是用id而不是用地区名这种string了嘛? 很多申请网站都用dropdown men或者auto completer的设计，可以解决很多问题

- 格式统一，规避spelling and style errors
- 防止重复城市名(waterloo in canada, in states and in UK)
- etc

把entities改成id的这个流程叫做`normalization`, 实际上和machine learning中处理categorical variables的方法是一样的.

### 2.1.2 Many-to-one and many-to-many replationship

![Screenshot 2022-11-15 at 17.51.04](/Users/yixiangzhang/Documents/DE_course/book_data-intensive/assets/figure2-3.png)

### 2.1.3 Historical interlude



### 2.1.4 Relational vs document database today

> 有点outdated since the book published in 2014.





## 2.2 Query Languages for Data



| Property | Declarative query language                             | Impreative language                                          |
| -------- | ------------------------------------------------------ | ------------------------------------------------------------ |
| 本质     | 描述你想要的数据, 背后具体怎么indexing etc, 不用你操心 | 指令计算机进行一系列操作, declare variables, iteration,输出结果 |
| 例子     | SQL                                                    | python, java                                                 |
|          |                                                        |                                                              |

### 2.2.1 `MapReduce` Query

Mapreduce 是一种programming model for processing large amount of data in bulk across many machines, popularized by Google.

它介于impreative和declarative language中间, 它是基于很多languages中都有的built-in functions, `map` (or collect) and `reduce` (fold or inject).

举一个例子，如果你是一个海洋学家，你在海上每看到一只动物你就记录下来你看到的信息以及看到的时间，现在你需要query 你每个月能看到多少种Lamniformes鲨鱼

```sql
SELECT
		DATE_TRUNC('month',observation_timestamp) AS observation_month,
		SUM(num_animals) AS total_animals
FROM
		observations
WHERE family = 'Lamniformes'
GROUP BY observation_month;
```









## 2.3 Graph-like Data Models

 比较一下document model, 如果你的应用场景主要是one-to-many relationships (tree-structured data) or no relationships between records, the document model is appropriate.

如果你的数据里many-to-many relationship很常见的话，你需要用graph来model你的data了.

下面是一张采用的data model和数据的level of connectiveness之间的关系



![Screenshot 2022-11-16 at 14.16.10](/Users/yixiangzhang/Documents/DE_course/book_data-intensive/assets/figure2-5.png)







# Chapter 3. Storage and Retrieval









