# Log Analysis

Log Analysis is the first project in the Full-Stack Engineer Nanodegree in Udacity.

## Project Summary

The project summarizes and reports three questions from a large database of a News website/application. The purpose of this project is to strength the student's concepts of using Git, PSQL queries, and Python programming language. Each question is answered by one query. The query fetches the results and displays it as plain text in the terminal.

This project uses views to answer the third question to ensure the data's integrity in the original News Database.

The questions the SQL queries answers are the following:

1. What are the most popular three articles of all time?
2. Who are the most popular article authors of all time?
3. On which days did more than 1% of requests lead to errors?

## Requirements to Run

You should have the following to run the project:

[Vagrant](https://www.vagrantup.com/) - A virtual environment builder and manager.

[VirtualBox](https://www.virtualbox.com/) - An open source virtualization product by Oracle.

[Git](http://git-scm.com/) - An open source version control system (VCS)

[Python3](https://www.python.org/downloads/release/python-371/) - The code uses version 3.7.1 of Python

[Important Note] Up to date, VirtualBox Version 5.1 is the most stable with the Vagrant environment. Moreover, if you are running on a Windows Operating System, Vagrant Version 1.9.2 is the most stable.

## Running the Code
To run the code, follow the steps below:

1. Download Python3 from the link in the Requirements to Run section.

2. Download and install Vagrant and VirtualBox. If you are running a Windows Operating System, Vagrant Version 1.9.2 is the most stable.

3. Download the [VagrantFile](https://github.com/udacity/fullstack-nanodegree-vm/blob/master/vagrant/Vagrantfile)for running the preconfigured Vagrant settings.

4. Download the [database](https://d17h27t6h515a5.cloudfront.net/topher/2016/August/57b5f748_newsdata/newsdata.zip)

5. Open the Udacity Vagrant Folder in the bash terminal and cd into the Vagrant folder.

6. Open a bash terminal and run the command `vagrant up`. For Windows users, Git is the recommended terminal.

7. Once vagrant is installed successfully, run the command `vagrant ssh` to start up the virtual environment.

8. Once the command starts with vagrant, `cd` into the vagrant directory.

9. Unzip the database folder downloaded from the link provided in the Requirements to Run Section and place it in the vagrant directory.

10. Load the database by running the following command in the terminal: `psql -d news -f newsdata.sql`

11. Run the database with the following command: `psql -d news`

12. Run the [createViews.sql] file to create the needed views in the database to successfully run the project. Run the command: `psql -d news -f createViews.sql` in the terminal

13. Run the command `python reportingTool.py` to run the python program and fetch the query results.


## Views Created

These views were created to preserve the data integrity of the database.

First View Code:

```sql
CREATE VIEW stat_log AS
SELECT COUNT(*) AS stat, status, cast(time AS date) AS day
FROM log
WHERE status LIKE '%404%'
GROUP BY status, day
ORDER BY stat DESC
LIMIT 3;
```

Second View Code:

``` sql
CREATE VIEW visitors_in_total AS
SELECT count(*) AS visitors, cast(time AS date) AS errorTime
FROM log
GROUP BY errorTime;
```

Third View Code:

``` sql
CREATE VIEW countError AS
SELECT * FROM stat_log JOIN visitors_in_total
ON stat_log.day = visitors_in_total.errorTime;
```

##  References

The following list is the references used in working on this project:

[PSQL Strings](https://www.postgresql.org/docs/9.1/static/functions-string.html)

[PSQL Casting](http://www.postgresqltutorial.com/postgresql-cast/)

[Quotes](https://www.python.org/dev/peps/pep-0008/#string-quotes)

[Arrays](https://www.w3schools.com/python/python_arrays.asp)

[PSQL Function Formatting](https://www.postgresql.org/docs/9.1/static/functions-formatting.html)

[PSQL Round Function](https://www.w3resource.com/PostgreSQL/round-function.php)

[Functions](https://www.w3schools.com/python/python_functions.asp)

[Indentations](https://www.python.org/dev/peps/pep-0008/#indentation)

[Print Format](https://pyformat.info)
