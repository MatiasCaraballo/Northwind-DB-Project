from services.employees_service import employees_service
from data.connection import connection
from scripts.analysis import analysis

#gets the conection to the database
conn = connection()
analysis = analysis()

if __name__ == "__main__":
    employees_service = employees_service(conn,analysis)
    employees_service.top_most_revenue_employees()
    

    
    
