import cx_Oracle
import pandas as pd

"""
Some quick start guides:
* cx_Oracle 8: https://cx-oracle.readthedocs.io/en/latest/user_guide/installation.html
* pandas: https://pandas.pydata.org/pandas-docs/stable/user_guide/10min.html
"""
# TODO change path of Oracle Instant Client to yours
cx_Oracle.init_oracle_client(lib_dir = "./instantclient_19_9")

# TODO change credentials
# Connect as user "user" with password "mypass" to the "CSC423" service
# running on lawtech.law.miami.edu
connection = cx_Oracle.connect(
    "usr", "pwd", "lawtech.law.miami.edu/CSC_423")
cursor = connection.cursor()
print('Welcome to the Busy Bee Cleaning Company! We are all set for the annual audit. Kindly let me know if you have any questions')
print('What would you like to see? Respond with the options below to view requisite info!')
print('Type 1 to Print all Employees')
print('Type 2 to Print all Clients')
print('Type 3 to Print all Equipments')
print('Type 4 to Print all Services')
print('Type 5 to Print Master Table')
print('Type 6 to Quit')
print('All other values will be rejected!')
response = int(input("Enter your value: ")) 
while (response != 6):
      if (response == 1):
          cursor.execute("""SELECT * FROM EMPLOYEE""")
          # get column names from cursor
          columns = [c[0] for c in cursor.description]
          # fetch data
          data = cursor.fetchall()
          # bring data into a pandas dataframe for easy data transformation
          df = pd.DataFrame(data, columns = columns)
          print(df) # examine
          print(df.columns)
          # print(df['FIRST_NAME']) # example to extract a column
      elif (response ==2):
          cursor.execute("""SELECT * FROM CLIENT""")
          # get column names from cursor
          columns = [c[0] for c in cursor.description]
          # fetch data
          data = cursor.fetchall()
          # bring data into a pandas dataframe for easy data transformation
          df = pd.DataFrame(data, columns = columns)
          print(df) # examine
          print(df.columns)
          # print(df['FIRST_NAME']) # example to extract a column
      elif (response ==3):
          cursor.execute("""SELECT * FROM EQUIPMENT""")
          # get column names from cursor
          columns = [c[0] for c in cursor.description]
          # fetch data
          data = cursor.fetchall()
          # bring data into a pandas dataframe for easy data transformation
          df = pd.DataFrame(data, columns = columns)
          print(df) # examine
          print(df.columns)
          # print(df['FIRST_NAME']) # example to extract a column
      elif (response ==4):
          cursor.execute("""SELECT * FROM SERVICE""")
          # get column names from cursor
          columns = [c[0] for c in cursor.description]
          # fetch data
          data = cursor.fetchall()
          # bring data into a pandas dataframe for easy data transformation
          df = pd.DataFrame(data, columns = columns)
          print(df) # examine
          print(df.columns)
          # print(df['FIRST_NAME']) # example to extract a column
      elif (response == 5):
          cursor.execute("""SELECT * FROM BOOKING""")
          # get column names from cursor
          columns = [c[0] for c in cursor.description]
          # fetch data
          data = cursor.fetchall()
          # bring data into a pandas dataframe for easy data transformation
          df = pd.DataFrame(data, columns = columns)
          print(df) # examine
          print(df.columns)
          # print(df['FIRST_NAME']) # example to extract a column
      
      response = int(input("Enter another value: ")) 
else:
      print('Thanks for stopping! Happy Holidays!')
      

'''
# cursor.execute("""
#    SELECT *  FROM BOOKING
    """)
'''


