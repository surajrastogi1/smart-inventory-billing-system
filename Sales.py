from Database import conn


class Sales:
    def __init__(self):
        pass
    @staticmethod
    def create_table():
        cur = conn.cursor()
        cur.execute(
            """CREATE TABLE IF NOT EXISTS sales (
            id SERIAL PRIMARY KEY,
            customer_id INTEGER NOT NULL,
            date DATE NOT NULL,
            total_amount DECIMAL(10,2) NOT NULL,
            CONSTRAINT fk_sales_customer
                FOREIGN KEY (customer_id)
                REFERENCES customers(id)
                ON DELETE CASCADE
            )"""
        )
        conn.commit()
        cur.close()
    @staticmethod
    def insert_sale(customer_id,date,total_amount):
        cur = conn.cursor()
        cur.execute(
            """INSERT INTO sales (customer_id,date,total_amount)
            VALUES (%s,%s,%s)""",
            (customer_id,date,total_amount),
        )
        conn.commit()
        cur.close()

    @staticmethod
    def update_sale(sale_id,customer_id=None,date=None,total_amount=None):
        cur = conn.cursor()
        cur.execute("SELECT * FROM sales WHERE id = %s",(sale_id,))
        sale = cur.fetchone()
        if not sale:
            print(">>>> sale Not Found")
            cur.close()
            return
        update_field = []
        if customer_id:
            update_field.append(f"customer_id = '{customer_id}'")
        if date:
            update_field.append(f"date = '{date}'")
        if total_amount:
            update_field.append(f"total_amount = '{total_amount}'")
        
        update_query = f"UPDATE sales SET {','.join(update_field)} WHERE id = %s"

        cur.execute(update_query,(sale_id,))
        conn.commit()
        cur.close()
    
    @staticmethod
    def delete_sale(sale_id):
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM sales WHERE id = %s",(sale_id),)
        conn.commit()
        cur.close() 
    
    @staticmethod
    def generate_bill(sale_id):
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM Sales WHERE id = %s",(sale_id,))
        sale_items = cur.fetchall()
        total_amount = 0
        for item in sale_items:
            total_amount+=item[4]*item[3]

        cur.close()   
        return total_amount

    @staticmethod
    def get_all_sales():
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM sales")
        sales = cur.fetchall()
        cur.close()   
        return sales
    
    @staticmethod
    def get_sale_by_id(sale_id):
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM sales WHERE id = %s",(sale_id,))
        sales = cur.fetchall()
        cur.close()   
        return sales
    
    #Analytical Queries
    
    @staticmethod
    def total_sale_by_date(start_date,end_date):
        cur = conn.cursor()
        cur.execute(
            "SELECT SUM(total_amount) FROM sales WHERE date BETWEEN %s AND %s",(start_date,end_date,))
        total_sales = cur.fetchone()
        cur.close()   
        return total_sales
    
    @staticmethod
    def get_top_selling_products():
        cur = conn.cursor()
        cur.execute(
            """SELECT SUM(quantity) AS total_quantity 
            FROM sale_items
            GROUP BY product_id
            ORDER BY total_quantity DESC
            LIMIT 5""")
        total_products = cur.fetchall()
        cur.close()   
        return total_products
    
    @staticmethod
    def get_sales_by_customer(customer_id):
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM sales WHERE id = %s",(customer_id,))
        sales = cur.fetchone()
        cur.close()   
        return sales

    
    @staticmethod
    def sale_menu():
        while True:
            print("1. Create Table")
            print("2. Insert Sale")
            print("3. Update Sale")
            print("4. Delete Sale")
            print("5. View Sale")
            print("6. View Sale By ID")
            print("7. Generate Bill")
            print("8. Total Sale By Date")
            print("9. Top Selling Products")
            print("10. Sales By Customers")
            print("0. STOP/EXIT")
            choice = input("Enter your choice = ")

            if choice == "1":
                Sales().create_table()
                print(">>>> Sale Table Created!")

            elif choice == "2":
                customer_id = input("Enter Customer Id = ")
                date = input("Enter sale date = ")
                total_amount = input("Enter Total Amount = ")
                Sales().insert_sale(customer_id,date,total_amount)
                print(">>>> Sale Inserted")

            elif choice == "3":
                customer_id = input("Enter Customer Id = ")
                date = input("Enter Sale date = ")
                total_amount = input("Enter Total Amount = ")
                Sales().update_sale(customer_id,date,total_amount)
                print(">>>> Sale Updated!")

            elif choice == "4":
                sale_id = input("Enter Sale ID = ")
                Sales().delete_sale(sale_id)
                print(">>>> Sale Deleted")

            elif choice == "5":
                sales = Sales().get_all_sales()
                print(sales)
                print(">>>> Sales Fetched!")

            elif choice == "6":
                sale_id = input("Enter Sale ID = ")
                sale = Sales().get_sale_by_id(sale_id)
                print(sale)
                print(">>>> Sale Fetched!")

            elif choice == "7":
                sale_id = input("Enter Sale ID = ")
                bill = Sales().generate_bill(sale_id)
                print(bill)
                print(">>>> Bill Generated!")

            elif choice == "8":
                start_date = input("Enter Start Date = ")
                end_date = input("Enter End Date = ")
                total_sale = Sales().total_sale_by_date(start_date,end_date)
                print(total_sale)
                print(">>>> Sale Fetched!")

            elif choice == "9":
                top_sale_products = Sales().get_top_selling_products()
                print(top_sale_products)
                print(">>>> Top 5 Products Fetched!") 

            elif choice == "10":
                customer_id = input("Enter Customer ID = ")
                sale = Sales().get_sales_by_customer(customer_id)
                print(sale)
                print(">>>> Sale Fetched!") 


            elif choice == "0":
                print("Exiting...")
                break

            else:
                print("Invalid choice! Please Try Again.")




