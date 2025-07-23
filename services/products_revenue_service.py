import pandas as pd
import matplotlib.pyplot as plt

class products_service:
    def __init__(self,conn,analysis):
        self.conn = conn
        self.analysis = analysis
    def top_most_revenue_products(self):
        query_revenue_products = '''
        SELECT ProductName , SUM(Price * Quantity) as Revenue
        FROM OrderDetails od
        Join Products P
        ON
        p.ProductId = od.productId
        GROUP BY p.ProductId
        ORDER BY Revenue DESC
        LIMIT 10
        '''

        top_products = pd.read_sql
        
        top_products = pd.read_sql_query(query_revenue_products,self.conn) 
        self.analysis.create_plot(top_products,"ProductName","Revenue","10 most revenue products","10_revenue_products")
    def top_cheapest_products(self):
        cheapest_products = '''
        SELECT ProductName, Price from Products 
        order by Price ASC 
        Limit 5
        '''
        top_cheapest_products = pd.read_sql_query(cheapest_products,self.conn)
        top_cheapest_products.plot(x='ProductName',y='Price',kind='bar',legend=False)
        plt.title('TOP 5 CHEAPEST PRODUCTS')
        plt.xlabel('Products')
        plt.ylabel('Prices')
        plt.xticks(rotation = 90)
        plt.show()
        