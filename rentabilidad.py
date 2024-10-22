import pandas as pd
import sqlite3
import matplotlib.pyplot as plt
from scripts.analysis import create_plot


conn = sqlite3.connect('Northwind.db')

if __name__ == "__main__":

    query = '''
    SELECT ProductName , SUM(Price * Quantity) as Revenue
    FROM OrderDetails od
    Join Products P
    ON
    p.ProductId = od.productId
    GROUP BY p.ProductId
    ORDER BY Revenue DESC
    LIMIT 10
    '''

    top_products = pd.read_sql_query(query,conn) # parametros: Consulta y conexión
    create_plot(conn,"ProductName","Revenue","10 most revenue products","10_revenue_products")
    
#TOP 10 EMPLEADOS

query2 = '''
SELECT FirstName, LastName as Employee,Count(*) as Total
FROM ORDERS O
JOIN EMPLOYEES E
ON
e.EmployeeId  = o.EmployeeId
GROUP BY O.EmployeeID
ORDER BY Total '''

top_employees = pd.read_sql_query(query2,conn)

top_employees.plot(x='Employee',y='Total',kind='bar',legend=False)
plt.title('TOP 10 EMPLEADOS')
plt.xlabel('Empleados')
plt.ylabel('Total Vendido')
plt.xticks(rotation = 90)
plt.show()

#PRODUCTOS MÁS BARATOS

productos_baratos = '''
SELECT ProductName, Price from Products 
order by Price ASC 
Limit 5
'''
top_productos_baratos = pd.read_sql_query(productos_baratos,conn)
top_productos_baratos.plot(x='ProductName',y='Price',kind='bar',legend=False)
plt.title('TOP 5 PRODUCTOS BARATOS')
plt.xlabel('Producto')
plt.ylabel('Precio')
plt.xticks(rotation = 90)
plt.show()