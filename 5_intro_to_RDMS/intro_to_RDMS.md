# Introduction to Relational Databases (RDBMS)

This course is a brief intro to RDBMS.

**Table of contents:**

[toc]



# Chapter 1 Fundamental RDBMS concepts





## Review of Data Fundamentals



- types of data
  - Structure: data that follows a rigid format and 
  - Semi-structured: mix of data that has consistent 
  - Unstructured: data that is complex and mostly qualitube information

- data sources
  - relational databases
  - Web scraping
  - Sensor devices 
  - flat files with xml
- **file formats**
  - delimited text files
    - csv, tsv
  - spreadsheets
  - language 
    - Xml, json
    - transfer data
    - platform independent
- **data repositories**
  - it depends on your data time
  - **Online transcation processing system OLTP**
    - designed to store high volume day-to-day operational data
  - Online Analytical Processing systems OLAP
    - optimized for conducting complex data analystics
    - Include relation and non-relations
- relational databases
  - Designed in a way to minimize the duplicaiton of data
  - Example: SQL server, ibm DB2, oracle, mysql



- summary
  - data is information like facts, observation, perceptions, numbers, characters, and images
  - data can be structured, semi-structured



## Information and data models

Outline:

- Differnece between an information model and a data model
- Explain the advantage of the relational model
- Describe the difference between an entity and an attribute



- `Information model`: concept/abstract model for designers and operators
- `data model`:  concrete detaileed model for implementers. It is the blueprint of the system.



- hierachcal model vs relational model
- entity-relationship model 
  - used as a tool to deisgn relational databases
  - building blocks: entities and attributes
  - Example: book is an entity, attributes are its properties (实际上和OOP的概念很相似)

```python
class book()
    def __init__:
    		self.
# year, price, ISBN, pages, Aisle, Description, title, edition
```





> Each entity becomes a table in the database

​	

- [ ] is there a systemtic engineering methodology to design the ERD or OOP to minimize the level of duplication? 



## ERD & Types of Relationship

Outline:

- descibve the building block of a relatin
- explain the symbols used in a relation shipt
- descirnb 1-1, 1-many, many-many 



### Building blocks

- Entities - rectangle
- relationsjhip sets: diamond
- Crows foot notations (in this video)
  - `<` and `>` and `|`



### E-R Diagram (review)





### One-to-one Relationship 





## Mapping Entiteies to tables

**outline:**

- how a E-R translates into a relational diagram



### Example: Entity Book

- Entity = table
- attribute = column









## Data types

Outline:

- explain what data types are
- explain how data types are used in a database 
- identify some common data types



- Character string
  - fixed length `char(10)`
  - variable length varchar(20)
- numeric
  - interger
    - int
    - smallint
    - bigint
  - decimal
    - decimal
    - numceric
    - float
    - single
    - double
- date/time
  - date
    - 2021-12-31
  - time
    - 02.11.35
  - timestamp 
- boolearn
  - 1 bit of information
- binary string
  - a sequence of bytes
- large object **(lob)**
  - Pointer is held in the table while `lob` stays outside since it's too big
- xml



### Advantage of using data types

- Pros:
  - Data integrity (防止非法data entry)
  - Data sorting
  - Range selection
  - Data calculations
  - Use of standard functions





**Summary:**

- data types define the type of data can be stored in a column (保护data integrity)
- it has many other advantages for subsequent operations





## Relational Model

> 这一章其实不错，用linear algebra中的一些矩阵的概念，从数学上来定义这个database的ERD

**Outline:**

- define relational terms (relation, degree, cardinality)





- first proposed in 1970 by E.F. Codd at IBM,  based on mathematical models and terms, click here for the [paper](https://www.seas.upenn.edu/~zives/03f/cis550/codd.pdf)
- 这个数学模型有两个building blocks:
  - `relation`: fancy math term for relation
  - `sets`: 
- `Set`:
  - unordered collection of distinct elements
  - items of the same type
  - no order and no duplicate
- `relational database`: a set of relations
- `relation` = mathematical term for table
- relation分成两个parts `relation schema` and `relation instance`
  - `Relation schema`: specified name of a relation, name and type of each column (attributes)
  - `Relation instance`: a table made up of rows and columns
  - Column = attricutes = field
  - Row = tuple
  - Degree = the numer of attributes (columns) in a relation
  - Cardinality = the numcer of tuples (rows)

![](https://i.stack.imgur.com/2Fcer.gif)

Summary

- relational model is based on the `mathmatical concept of relation`
- Relation:
  - mathematical term for table
  - relation schema specifies relation name and attributes
  - relation instance is a table made up of the attributes and tuples
- degree refers to the number of attributes
- cardinality refers to the nuvmer of tuples



# Chapter 2 Introducing Relational Databases Products

This chapter mainly covers the popular databases out there in the industry like `DB2`, `MySQL`,`PostgreSQL` etc









































