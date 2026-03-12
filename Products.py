from Database import conn


class Products:
    def __init__(self):
        # self.name = name 
        # self.contact = contact
        pass
    @staticmethod
    def create_table():
        cur = conn.cursor()
        cur.execute(
            """CREATE TABLE IF NOT EXISTS products (
            id SERIAL PRIMARY KEY,
            name VARCHAR(50) NOT NULL,
            description TEXT NOT NULL,
            price DECIMAL(10,2) NOT NULL,
            quantity INTEGER NOT NULL
            )"""
        )
        conn.commit()
        cur.close()
    @staticmethod
    def insert_product(name,description,price,quantity):
        cur = conn.cursor()
        cur.execute(
            """INSERT INTO products (name,description,price,quantity)
            VALUES (%s,%s,%s,%s)""",
            (name,description,price,quantity),
        )
        conn.commit()
        cur.close()
    @staticmethod
    def update_product(product_id,name=None,description=None,price=None,quantity=None):
        cur = conn.cursor()
        cur.execute("SELECT * FROM products WHERE id = %s",(product_id,))
        product = cur.fetchone()
        if not product:
            print(">>>> Product Not Found")
            cur.close()
            return
        update_field = []
        if name:
            update_field.append(f"name = '{name}'")
        if description:
            update_field.append(f"description = '{description}'")
        if price:
            update_field.append(f"price = '{price}'")
        if quantity:
            update_field.append(f"quantity = '{quantity}'")
        update_query = f"UPDATE products SET {','.join(update_field)} WHERE id = %s"

        cur.execute(update_query,(product_id,))
        conn.commit()
        cur.close()
    @staticmethod
    def delete_product(product_id):
        cur = conn.cursor()
        cur.execute(
            "DELETE FROM products WHERE id = %s",(product_id),)
        conn.commit()
        cur.close() 
    @staticmethod
    def get_all_products():
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM products")
        products = cur.fetchall()
        cur.close()   
        return products
    
    @staticmethod
    def get_all_products_by_id(product_id):
        cur = conn.cursor()
        cur.execute(
            "SELECT * FROM products WHERE id = %s",(product_id))
        products = cur.fetchall()
        cur.close()   
        return products
    
    @staticmethod
    def product_menu():
        while True:
            print("1. Create Table")
            print("2. Insert Product")
            print("3. Update Product")
            print("4. Delete Product")
            print("5. View Product")
            print("6. View Product By ID")
            print("0. STOP/EXIT")
            choice = input("Enter your choice = ")

            if choice == "1":
                Products().create_table()
                print(">>>> Product Table Created!")

            elif choice == "2":
                name = input("Enter Product Name = ")
                description = input("Enter product Description = ")
                price = input("Enter Product Price = ")
                quantity = input("Enter Product Quantity = ")
                Products().insert_product(name,description,price,quantity)
                print(">>>> Product Inserted")

            elif choice == "3":
                product_id = input("Enter Product ID = ")
                name = input("Enter Product Name = ")
                description = input("Enter Product Description = ")
                price = input("Enter Product Price = ")
                quantity = input("Enter Product Quantity = ")
                Products().update_product(product_id,name,description,price,quantity)
                print(">>>> Product Updated!")

            elif choice == "4":
                product_id = input("Enter product ID = ")
                Products().delete_product(product_id)
                print(">>>> Product Deleted")
            elif choice == "5":
                products = Products().get_all_products()
                print(products)
                print(">>>> Products Fetched!")

            elif choice == "6":
                product_id = input("Enter Product ID = ")
                product = Products().get_all_products_by_id(product_id)
                print(product)
                print(">>>> Product Fetched!")

            elif choice == "0":
                print("Exiting...")
                break

            else:
                print("Invalid choice! Please Try Again.")


