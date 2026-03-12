import Database


from Customers import Customers
from Products import Products
from Sales import Sales

@staticmethod
def main_menu():
    while True:
        print("1. Customer Management")
        print("2. Product Management")
        print("3. Sales Management")
        print("4. Stop/Exit")
        choice = input("Enter your choice = ")
        if choice == "1":
            Customers().customer_menu()
        elif choice == "2":
            Products().product_menu()
        elif choice == "3":
            Sales().sale_menu()
        elif choice == "4":
            print("Exitting Application...")
            break
        else:
            print("Invalid Choice. Please Try Again.😊")

if __name__ == "__main__":
    main_menu()
    
