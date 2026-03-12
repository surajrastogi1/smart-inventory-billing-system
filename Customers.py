from Database import conn


class Customers:
    def __init__(self):
        # self.name = name 
        # self.contact = contact
        pass
    @staticmethod
    def create_table():
        cur = conn.cursor()
        cur.execute(
            """CREATE TABLE IF NOT EXISTS customers (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            contact VARCHAR(15) NOT NULL
            )"""
        )
        conn.commit()
        cur.close()
    @staticmethod
    def insert_customer(name,contact):
        cur = conn.cursor()
        cur.execute(
            """INSERT INTO customers (name,contact)
            VALUES (%s,%s)""",
            (name,contact),
        )
        conn.commit()
        cur.close()
    @staticmethod
    def update_customer(customer_id,name=None,contact=None):
        cur = conn.cursor()
        cur.execute("SELECT * FROM customers WHERE id = %s",(customer_id,))
        customer = cur.fetchone()
        if not customer:
            print(">>>> Customer Not Found")
            cur.close()
            return
        update_field = []
        if name:
            update_field.append(f"name = '{name}'")
        if contact:
            update_field.append(f"contact = '{contact}'")
        update_query = f"UPDATE customers SET {','.join(update_field)} WHERE ID = %s"

        cur.execute(update_query,(customer_id,))
        conn.commit()
        cur.close()
    @staticmethod
    def delete_customer(customer_id):
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM customers WHERE id = %s",(customer_id),)
        conn.commit()
        cur.close() 
    @staticmethod
    def get_all_customers():
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM customers")
        customers = cur.fetchall()
        cur.close()   
        return customers
    @staticmethod
    def customer_menu():
        while True:
            print("1. Create Table")
            print("2. Insert Customer")
            print("3. Update Customer")
            print("4. Delete Customer")
            print("5. View Customer")
            print("0. STOP/EXIT")
            choice = input("Enter your choice = ")

            if choice == "1":
                Customers().create_table()
                print(">>>> Customer Table Created!")

            elif choice == "2":
                name = input("Enter customer Name = ")
                contact = input("Enter Customer Contact = ")
                Customers().insert_customer(name,contact)
                print(">>>> Customer Inserted")

            elif choice == "3":
                customer_id = input("Enter Customer ID = ")
                name = input("Enter customer Name = ")
                contact = input("Enter Customer Contact = ")
                Customers().update_customer(customer_id,name,contact)
                print(">>>> Customer Updated!")

            elif choice == "4":
                customer_id = input("Enter Customer ID = ")
                Customers().delete_customer(customer_id)
                print(">>>> Customer Deleted")
            elif choice == "5":
                customers = Customers().get_all_customers()
                print(customers)
                print(">>>> Customer Fetched!")

            elif choice == "0":
                print("Exiting...")
                break

            else:
                print("Invalid choice! Please Try Again.")

           


