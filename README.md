# LOG ANALYSIS  
### [APR 2018]
A project completed under Udacity [Udacity: Full Stack Nanodegree].This Project builds a report on a news database using python 2.x or python3.x
and postgresql database system.

## What does Report Include?
1. What are the most popular three articles of all time?
  Which articles have been accessed the most?
  Present this information as a sorted list with the most popular article at the top

2. Who are the most popular article authors of all time?
  That is, when you sum up all of the articles each author has written, which authors get the most page views?
  Present this as a sorted list with the most popular author at the top.

3. On which days did more than 1% of requests lead to errors?
  The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser.

### How To Install
1.Install Vagrant from here [Vagrant](https://www.vagrantup.com/) and [VirtualBox](https://www.virtualbox.org/)
2.Download or clone from github [fullstack-nandegree-vm repository](https://github.com/udacity/fullstack-nanodegree-vm)
3.Get the newsdata.sql in our vagrant directory and we are ready to go.

### How to run
1. Change directory to vagrant directory, look up all files using command **ls**
2. Now, **vagrant up** command to run the vagrant on vm
3. **vagrant ssh** command to login into vm
4. Again change directory to vagrant.
5. use command **psql -d news -f newsdata.sql** to load news database
6. use command **ls** to check files present,then **python log.py** or **python3 log.py**     to run the program

### These PSQL queries are used to create the Views
- These views need to be created before executing python file
```sql
CREATE OR REPLACE VIEW articles_views AS
SELECT articles.title as "TITLE", count(*) AS "VIEWS"
FROM log JOIN articles
on log.path = concat('/article/', articles.slug)
GROUP BY "TITLE", log.path
ORDER BY "VIEWS" DESC;
```

```sql
CREATE OR REPLACE VIEW author AS
SELECT authors.name as "AUTHOR", count(*) AS "VIEWS"
FROM log, articles, authors
WHERE log.path = concat('/article/', articles.slug)
AND articles.author = authors.id
GROUP BY "AUTHOR"
ORDER BY "VIEWS" DESC;
```

#####  PrettyTable is used : PrettyTable is a simple Python library designed to make it quick and easy to represent tabular data in visually appealing ASCII tables. It was inspired by the ASCII tables used in the PostgreSQL shell psql. PrettyTable allows for selection of which columns are to be printed, independent alignment of columns (left or right justified or centred) and printing of “sub-tables” by specifying a row range. prettytable.py is the file of prettyTable library.

##### This is not neccessary for this project, Only used as a design and I learned to use it seperately. 

## Thank you!

