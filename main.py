# STEP 1A
# Import SQL Library and Pandas
import sqlite3
import pandas as pd 

# STEP 1B
# Connect to the database
conn = sqlite3.connect('data.sqlite')


# STEP 2
# Replace None with your code
df_first_five = pd.read_sql_query("SELECT employeeNumber, lastName FROM employees", conn)

# STEP 3
# Replace None with your code
df_five_reverse = pd.read_sql_query("SELECT lastName, employeeNumber FROM employees", conn)

# STEP 4
# Replace None with your code
df_alias = pd.read_sql_query("SELECT name AS employee_name FROM employees", conn)

# STEP 5
# Replace None with your code
df_executive = pd.read_sql_query("SELECT * FROM employees WHERE position = 'Executive'", conn)  

# STEP 6
# Replace None with your code
df_name_length = pd.read_sql_query("SELECT name, LENGTH(name) AS name_length FROM employees", conn)

# STEP 7
# Replace None with your code
df_short_title = pd.read_sql_query("SELECT * FROM employees WHERE LENGTH(title) < 10", conn)

# STEP 8
# Replace None with your code
sum_total_price = pd.read_sql_query("SELECT SUM(price) AS total_price FROM products", conn).iloc[0, 0]

# STEP 9
# Replace None with your code
df_day_month_year = pd.read_sql_query("SELECT strftime('%d', hire_date) AS day, strftime('%m', hire_date) AS month, strftime('%Y', hire_date) AS year FROM employees", conn)