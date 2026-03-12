import streamlit as st
import pandas as pd
from Database import conn
from Customers import Customers
from Products import Products
from Sales import Sales
from salesitem import SaleItems

Customers.create_table()
Products.create_table()
Sales.create_table()
SaleItems.create_table()

st.set_page_config(page_title="Smart Inventory System", layout="wide")

st.title("📦 Smart Sales & Inventory Dashboard")

menu = st.sidebar.selectbox(
    "Navigation",
    [
        "Customers",
        "Products",
        "Sales",
        "Analytics",
        "Reports"
    ]
)

# -------------------------
# CUSTOMER MANAGEMENT
# -------------------------

if menu == "Customers":

    st.header("Customers Management")

    tab1, tab2 = st.tabs(["Add Customer", "View Customers"])

    with tab1:

        name = st.text_input("Customer Name")
        contact = st.text_input("Contact")

        if st.button("Add Customer"):

            Customers.insert_customer(name, contact)
            st.success("Customer Added Successfully")

    with tab2:

        customers = Customers.get_all_customers()

        if customers:
            df = pd.DataFrame(customers, columns=["ID", "Name", "Contact"])
            st.dataframe(df)

# -------------------------
# PRODUCT MANAGEMENT
# -------------------------

elif menu == "Products":

    st.header("Product Management")

    tab1, tab2 = st.tabs(["Add Product", "View Products"])

    with tab1:

        name = st.text_input("Product Name")
        description = st.text_area("Description")
        price = st.number_input("Price")
        quantity = st.number_input("Quantity")

        if st.button("Add Product"):

            Products.insert_product(name, description, price, quantity)
            st.success("Product Added Successfully")

    with tab2:

        products = Products.get_all_products()

        if products:
            df = pd.DataFrame(
                products,
                columns=["ID", "Name", "Description", "Price", "Quantity"]
            )
            st.dataframe(df)

# -------------------------
# SALES MANAGEMENT
# -------------------------

elif menu == "Sales":

    st.header("Sales Management")

    tab1, tab2 = st.tabs(["Create Sale", "View Sales"])

    with tab1:

        customer_id = st.number_input("Customer ID")
        date = st.date_input("Sale Date")
        total = st.number_input("Total Amount")

        if st.button("Create Sale"):

            Sales.insert_sale(customer_id, date, total)
            st.success("Sale Recorded")

    with tab2:

        sales = Sales.get_all_sales()

        if sales:
            df = pd.DataFrame(
                sales,
                columns=["ID", "Customer ID", "Date", "Total Amount"]
            )
            st.dataframe(df)

# -------------------------
# ANALYTICS DASHBOARD
# -------------------------

elif menu == "Analytics":

    st.header("📊 Analytics Dashboard")

    col1, col2 = st.columns(2)

    with col1:

        st.subheader("Total Sales by Date")

        start = st.date_input("Start Date")
        end = st.date_input("End Date")

        if st.button("Calculate"):

            result = Sales.total_sale_by_date(start, end)

            if result:
                st.metric("Total Sales", result[0])

    with col2:

        st.subheader("Top Selling Products")

        top_products = Sales.get_top_selling_products()

        if top_products:

            df = pd.DataFrame(top_products, columns=["Quantity"])
            st.bar_chart(df)

# -------------------------
# REPORTS SECTION
# -------------------------

elif menu == "Reports":

    st.header("📄 Reports")

    report_type = st.selectbox(
        "Select Report",
        [
            "All Customers",
            "All Products",
            "All Sales"
        ]
    )

    if report_type == "All Customers":

        customers = Customers.get_all_customers()
        df = pd.DataFrame(customers, columns=["ID", "Name", "Contact"])
        st.dataframe(df)

        st.download_button(
            "Download CSV",
            df.to_csv(index=False),
            "customers_report.csv"
        )

    elif report_type == "All Products":

        products = Products.get_all_products()
        df = pd.DataFrame(
            products,
            columns=["ID", "Name", "Description", "Price", "Quantity"]
        )

        st.dataframe(df)

        st.download_button(
            "Download CSV",
            df.to_csv(index=False),
            "products_report.csv"
        )

    elif report_type == "All Sales":

        sales = Sales.get_all_sales()
        df = pd.DataFrame(
            sales,
            columns=["ID", "Customer ID", "Date", "Total Amount"]
        )

        st.dataframe(df)

        st.download_button(
            "Download CSV",
            df.to_csv(index=False),
            "sales_report.csv"
        )