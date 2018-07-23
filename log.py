'''!/usr/bin/env python3
imports prettytable.py which is used for visual table design'''
import prettytable
import psycopg2


def main():
    # Connect to an existing database given
    conn = psycopg2.connect("dbname=news")

    # Open a cursor to perform database operations
    cur = conn.cursor()
    # Question 1
    sql_popular_articles = """
      SELECT * FROM articles_views LIMIT 3;
    """
    cur.execute(sql_popular_articles)

    print("::: Most popular articles are :::")
    printTable(cur)
    print("\n")

    # Question 2
    sql_popular_authors = """
    SELECT * FROM author LIMIT 3;
    """
    cur.execute(sql_popular_authors)

    print("::: Most popular authors are :::")
    printTable(cur)
    print("\n")

    # Question 3
    sql_more_than_one_percent_errors = """
    SELECT *
    FROM (SELECT time::date AS "DAY",round(sum(case log.status
    WHEN '404 NOT FOUND' then 1 else 0 end * 100.0)/count(log.status),2)
    AS "ERRORS"
    FROM log
    GROUP BY time::date
    ORDER BY "ERRORS" DESC) AS "QUERY" WHERE "ERRORS" > 1;
    """
    cur.execute(sql_more_than_one_percent_errors)
    x = prettytable.PrettyTable(["Date", "Percentage"])

    print("::: Days with more than 1% errors are :::")
    for (date, percentage) in cur.fetchall():
        x.add_row([date, percentage])
    print(x)
    print("\n")

    # Close communication with the database
    cur.close()
    conn.close()
''' Format: prettytable.PrettyTable(["header name", "header name"])
        Format: x.add_row([data, data])'''


def printTable(cur):
    x = prettytable.PrettyTable(["Title", "Views"])
    for (title, view) in cur.fetchall():
        x.add_row([title, view])
    print(x)

if __name__ == "__main__":
    main()
