#!/usr/bin/env python3

# import needed packages
import psycopg2

# sql statements
q1 = ("SELECT title, COUNT(*) AS viewNum \n"
      "FROM articles AS a JOIN log AS l \n"
      "ON a.slug = substring(l.path, 10) \n"
      "GROUP BY title \n"
      "ORDER BY viewNum DESC \n"
      "LIMIT 3")

q2 = ("SELECT au.name, COUNT(*) as viewNum \n"
      "FROM articles AS a JOIN authors AS au \n"
      "ON a.author = au.id \n"
      "JOIN log AS l ON a.slug = substring(l.path, 10) \n"
      "WHERE l.status LIKE '200 OK' \n"
      "GROUP BY au.name \n"
      "ORDER BY viewNum DESC;")

q3 = ("SELECT ROUND((stat*100.0)/visitors, 3) AS results, \n"
      "to_char(errorTime, 'MON DD, YYYY') \n"
      "FROM countError \n"
      "ORDER BY results DESC \n"
      "LIMIT 1;")

# connect to database & feed query as parameter


def get_Results(sql_Query):
    db = psycopg2.connect("dbname=news")
    cursor = db.cursor()
    cursor.execute(sql_Query)
    results = cursor.fetchall()
    db.close()
    return results


# assign each fed query into a variable and feed it to the function
query1 = get_Results(q1)
query2 = get_Results(q2)
query3 = get_Results(q3)

# print querys out


def results_to_print(queryList):
    for x in range(len(queryList)):
        head = queryList[x][0]
        result = queryList[x][1]
        print("%s - %d" % (head, result) + " views")
    print("\n")


# display query
print("\n")
print("1. What are the most popular three articles of all time?")
print("\n")
results_to_print(query1)
print("\n")
print("2. Who are the most popular article authors of all time?")
print("\n")
results_to_print(query2)
print("\n")
print("3. On which days did more than 1% of requests lead to errors?")
print("\t" + query3[0][1] + " - " + str(query3[0][0]) + "%")
print("\n")
