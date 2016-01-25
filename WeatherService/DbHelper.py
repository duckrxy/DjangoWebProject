import pymssql
import pyodbc
import os

class DbHelper:
    def __init__(self):
        pass

    def mssqlconn(self):
        #self.conn = pymssql.connect(server='vemjmt51z1.database.windows.net', user='tigeren@vemjmt51z1', password='Duckrenxiaoyin0', database='supermarket')
        self.conn = pyodbc.connect('DRIVER={ODBC Driver 11 for SQL Server};SERVER=vemjmt51z1.database.windows.net;DATABASE=supermarket;UID=tigeren@vemjmt51z1;PWD=Duckrenxiaoyin0')\
        #self.conn = pyodbc.connect('DRIVER={SQL Server};SERVER=tigersql;DATABASE=cp_china;UID=sa;PWD=P@ssw0rd')
        return self.conn

    def mssqldisconn(self):
        self.conn.close()

    def update_weather_forecast(self, date, low, high, maxwind, avgwind):
        query = 'exec dbo.spUpdateWeatherForecast @date = \'{0}\', @low = {1}, @high = {2}'.format(date, low, high)
        print query
        cursor = self.conn.cursor()
        cursor.execute(query)
        return

    def execute_query(self,query):
        cursor = self.conn.cursor()
        cursor.execute(query)
        return cursor.fetchall()

    def test(self):
        helper = DbHelper()
        helper.mssqlconn()
        rows = helper.execute_query('select top 100 * from dbo.SalesTemperature')
        for row in rows:
            print row[0]
        helper.mssqldisconn()
       