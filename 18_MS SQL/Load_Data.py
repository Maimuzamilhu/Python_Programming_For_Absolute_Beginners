import pyodbc as sql
try:
    cs = """Driver = {ODBC Driver 11 for SQL Server};
        Server = RAJABBHATTI-PC;
        Database = Python_customer;
        UID  = SA;
        PWD = 123;
    """
#print(Connection)
#print(sql.drivers())
    Connection= sql.connect(cs)
except Exception as ex:
    print("ERROR :"+str(ex))

cur = Connection.cursor()
rows = cur.execute("SELECT *FROM [Python_customer].[dbo].[Customer_Info]")

#-------Show Date----
for rwow in rows:
    print(rwow)

#-------------Fetch method --------------------

result_list =cur.fetchall()
print(result_list)


