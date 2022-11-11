# Introduction to Relational Databases (RDBMS)

This course is a brief intro to RDBMS.

**Table of contents:**





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

outline:

- how a E-R translates into a relational diagram



### Example: Entity Book

- Entity = table
- attribute = column





















