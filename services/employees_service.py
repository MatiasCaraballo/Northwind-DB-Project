import pandas as pd
import matplotlib.pyplot as plt

class employees_service:
    def __init__(self,conn,analysis):
        self.conn = conn
        self.analysis = analysis
    
    def top_most_revenue_employees(self):
        query_orders = '''
        SELECT FirstName, LastName as Employee,Count(*) as Total
        FROM ORDERS O
        JOIN EMPLOYEES E
        ON
        e.EmployeeId  = o.EmployeeId
        GROUP BY O.EmployeeID
        ORDER BY Total DESC '''

        top_employees = pd.read_sql_query(query_orders,self.conn)

        self.analysis.create_plot(top_employees)

        top_employees.plot(x='Employee',y='Total',kind='bar',legend=False)
        plt.title('TOP 10 EMPLOYEES')
        plt.xlabel('EMPLOYEES')
        plt.ylabel('TOTAL SALES')
        plt.xticks(rotation = 90)
        plt.show()