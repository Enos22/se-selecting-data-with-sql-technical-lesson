import sqlite3
import pandas as pd

conn = sqlite3.connect('data.sqlite')

#get all information about the employee records, we might do something like this (* means all columns):

# employee_data = pd.read_sql("""SELECT * FROM employees;""", conn)
# print(employee_data)

print(pd.read_sql("""
SELECT *
FROM employees;
""", conn))

#select/Retrieve the first and last name of the employees

employees_first_and_last_name = pd.read_sql("""
SELECT firstName, lastName
  FROM employees;
""", conn).head()

print(employees_first_and_last_name)

#use aliases (AS keyword) to change the column names in our query result:
employees_first_name = pd.read_sql("""
SELECT firstName AS name
  FROM employees;
""", conn).head()

print(employees_first_name)

#use of SQL CASE statements
employees_by_role =pd.read_sql("""
SELECT firstName, lastName, jobTitle,
        CASE
        WHEN jobTitle = "Sales Rep" THEN "Sales Rep"
        ELSE "Not Sales Rep"
        END AS role
    FROM employees;
""", conn).head(10)

print(employees_by_role)

#use a CASE statement with multiple WHEN clauses to transform the officeCode
# employees_with_location = pd.read_sql("""
# SELECT firstName, lastName, officeCode,
#        CASE
#        WHEN officeCode = "1" THEN "San Francisco, CA"
#        WHEN officeCode = "2" THEN "Boston, MA"
#        WHEN officeCode = "3" THEN "New York, NY"
#        WHEN officeCode = "4" THEN "Paris, France"
#        WHEN officeCode = "5" THEN "Tokyo, Japan"
#        END AS office
#   FROM employees;
# """, conn).head(10)

# print(employees_with_location)

employees_with_location = pd.read_sql("""
SELECT firstName, lastName, officeCode,
       CASE officeCode
       WHEN "1" THEN "San Francisco, CA"
       WHEN "2" THEN "Boston, MA"
       WHEN "3" THEN "New York, NY"
       WHEN "4" THEN "Paris, France"
       WHEN "5" THEN "Tokyo, Japan"
       END AS office
  FROM employees;
""", conn).head(10)

print(employees_with_location)

#t returns the number of characters

employee_name_lengths = pd.read_sql("""
SELECT length(firstName) AS name_length
  FROM employees;
""", conn).head()

print(employee_name_lengths)

#To upper function in SQL
upper_employees = pd.read_sql("""
SELECT upper(firstName) AS name_in_all_caps
  FROM employees;
""", conn).head()

print(upper_employees)

#finding a substring (subset of a string)

employees_initials = pd.read_sql("""
SELECT substr(firstName, 1, 1) AS first_initial
  FROM employees;
""", conn).head()

print(employees_initials)

#add a . after each first initial, we could use the SQLite || (concatenate) operator. This works similarly to + with strings in Python:

employees_initials = pd.read_sql("""
SELECT substr(firstName, 1, 1) || "." AS first_initial
  FROM employees;
""", conn).head()

print(employees_initials)

# combine multiple column values, not just string literals

employees_full_names = pd.read_sql("""
SELECT firstName || lastName AS full_name
  FROM employees;
""", conn).head()

print(employees_full_names)

#concatenate those column values with a space (" ") string literal:
employees_full_names = pd.read_sql("""
SELECT firstName || " " || lastName AS full_name
  FROM employees;
""", conn).head()

print(employees_full_names)

#switch over to using the orderDetails table:
order_details = pd.read_sql("""SELECT * FROM orderDetails;""", conn)
print(order_details)

#Round the price to the nearest dollar. 

rounded_prices = pd.read_sql("""
SELECT round(priceEach) AS rounded_price
  FROM orderDetails;
""", conn)

print(rounded_prices)

#returning integers instead floating-point numbers. 
rounded_prices = pd.read_sql("""
SELECT CAST(round(priceEach) AS INTEGER) AS rounded_price_int
  FROM orderDetails;
""", conn)

print(rounded_prices)

#Basic mathematics - Multiply
totals = pd.read_sql("""
SELECT priceEach * quantityOrdered AS total_price
  FROM orderDetails;
""", conn)

print(totals)

# Built-in SQL Functions for Date and Time Operations

orders = pd.read_sql("""SELECT * FROM orders;""", conn)
print(orders)



days_remaining = pd.read_sql("""
SELECT requiredDate - orderDate
  FROM orders;
""", conn)

print(days_remaining)

#he difference in days.
days_remaining = pd.read_sql("""
SELECT julianday(requiredDate) - julianday(orderDate) AS days_from_order_to_required
  FROM orders;
""", conn)

print(days_remaining)

#select the order dates as well as dates 1 week after the order dates
order_dates = pd.read_sql("""
SELECT orderDate, date(orderDate, "+7 days") AS one_week_later
  FROM orders;
""", conn)

print(order_dates)

#plit apart a date or time value into different sub-parts
order_dates = pd.read_sql("""
SELECT orderDate,
       strftime("%m", orderDate) AS month,
       strftime("%Y", orderDate) AS year,
       strftime("%d", orderDate) AS day
  FROM orders;
""", conn)

print(order_dates)
