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