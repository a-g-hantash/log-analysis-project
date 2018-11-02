#!/usr/bin/env python3
"""The first project of the Udacity Full-Stack Engineer Nanodegree.

A reporting tool that fetches SQL queries from a large database.
"""
# import needed packages
import psycopg2

# sql statements
q1 = """
      SELECT title, COUNT(*) AS viewNum
      FROM articles AS a JOIN log AS l
      ON '/article/' || a.slug = l.path
      GROUP BY title
      ORDER BY viewNum DESC
      LIMIT 3
      """

q2 = """
      SELECT au.name, COUNT(*) AS viewNum
      FROM articles AS a JOIN authors AS au
      ON a.author = au.id
      JOIN log AS l
      ON '/article/' || a.slug = l.path
      WHERE l.status LIKE '200 OK'
      GROUP BY au.name
      ORDER BY viewNum DESC;
      """

q3 = """
      SELECT  to_char(errorTime, 'MON DD, YYYY'),
      ROUND((stat*100.00)/visitors, 3) AS results
      FROM countError
      WHERE ROUND((stat*100.00)/visitors,3) > 1.00
      ORDER BY results DESC;
      """

# connect to database & feed query as parameter


def get_Results(sql_Query):
    """Connect to database and fetch results."""
    try:
        db = psycopg2.connect("dbname=news")
        cursor = db.cursor()
    except Exception as e:
        print(e)
    cursor.execute(sql_Query)
    results = cursor.fetchall()
    db.close()
    return results

# print querys out


def results_to_print(queryList):
    """Print the results of the queries."""
    for head, result in queryList:
        print('{} - {} views'.format(head, result))
    print("\n")


def main():
    """Main sub-routine."""
    # assign each fed query into a variable and feed it to the function
    query1 = get_Results(q1)
    query2 = get_Results(q2)
    query3 = get_Results(q3)

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
    print("\n")
    for day, errorPercent in query3:
        print('{} - {}%'.format(day, errorPercent))
        print("\n")


if __name__ == '__main__':
    main()
