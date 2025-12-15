import mysql.connector
from pprint import pprint
import logging
from logging_setup import setup_logger

logger= setup_logger('db_helper')



def get_db_cursor():

     connection= mysql.connector.connect(
    host= "localhost",
    user= "root",
    password= "Bajwa123",
    database= "expense_manager"
)
     if connection.is_connected():

        print("Database connected successfully")
     else:

        print("failed to connect database")

     cursor= connection.cursor(dictionary=True)
     return cursor,connection

def fetch_all_expenses():
    cursor,connection= get_db_cursor()

    try:
        cursor.execute("SELECT * FROM expenses")
        expenses= cursor.fetchall()
        return expenses
    finally:
        cursor.close()
        connection.close()
def fetch_expenses_by_date(expense_date):
    cursor,connection= get_db_cursor()
    logger.info(f"fetch_expenses_by_date {expense_date}")
    try:
        cursor.execute("SELECT * FROM expenses Where expense_date= %s",(expense_date,))
        expenses= cursor.fetchall()
        return expenses
    finally:
        cursor.close()
        connection.close()

def insert_expenses(expense_date,amount,category,notes):
    cursor,connection= get_db_cursor()
    logger.info(f"insert_expenses: expense_date:{expense_date},amount:{amount},category:{category},notes: {notes}")
    try:


        cursor.execute("INSERT INTO expenses(expense_date,amount,category,notes) VALUES(%s,%s,%s,%s)",(expense_date,amount,category,notes))
        connection.commit()
        print("Values inserted successfully")
    finally:
        cursor.close()
        connection.close()

def delete_expenses(expense_date):
    cursor,connection= get_db_cursor()
    try:


        cursor.execute("DELETE FROM expenses WHERE expense_date= %s",(expense_date,))
        connection.commit()
        print("Deleted Successfully")

    finally:
        cursor.close()
        connection.close()

def fetch_expense_summary(start_date,end_date):
    cursor,connection= get_db_cursor()
    logger.info(f"fetch_expense_summary {start_date}-{end_date}")
    try:
        cursor.execute("select category, sum(amount) as total from expenses where expense_date between %s and %s group by category",(start_date,end_date))
        expenses= cursor.fetchall()
        return expenses
    finally:
        cursor.close()
        connection.close()










if __name__ == "__main__":
    results = fetch_expense_summary("2024-08-01","2024-08-05")
    print(results)




