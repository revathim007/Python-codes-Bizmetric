import pyodbc
import logging
from datetime import datetime

def get_connection():
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=LAPTOP-7DKKRVFQ\SQLEXPRESS;" 
        "DATABASE=RESTAURANT;"
        "Trusted_Connection=yes;"
    )
    return conn


class Menu:

    def display_menu(self):
        conn = get_connection()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM Menu")

        print("\n========= RESTAURANT MENU =========")
        print("ID   Dish Name                  Price")
        print("----------------------------------------")

        for row in cursor:
            print(f"{row.item_id:<4} {row.dish_name:<25} ₹{row.price}")

        conn.close()


class Order:

    def __init__(self, table_number):
        self.table_number = table_number
        self.orders = []

    def take_order(self):
        conn = get_connection()
        cursor = conn.cursor()
        logging.basicConfig(
            level=logging.INFO,
            format="%(asctime)s - %(levelname)s - %(message)s"
        )

        while True:
            try:
                item_id = int(input("\nEnter Item ID (0 to Finish): "))
                if item_id == 0:
                    break
            
                quantity = int(input("Enter Quantity: "))

                cursor.execute("SELECT dish_name, price FROM Menu WHERE item_id = ?", item_id)
                item = cursor.fetchone()

                if item:
                    dish_name = item[0]
                    price = float(item[1])
                    total = price * quantity

                    self.orders.append((dish_name, price, quantity, total))

                    cursor.execute("""
                        INSERT INTO Orders (table_number, dish_name, price, quantity, total)
                        VALUES (?, ?, ?, ?, ?)
                    """, self.table_number, dish_name, price, quantity, total)

                    conn.commit()

                    print(" Item Added Successfully")

                else:
                    print(" Invalid Item ID")

            except:
                print(" Invalid Input. Try Again.")

        conn.close()


class Billing:

    def __init__(self, table_number, orders):
        self.table_number = table_number
        self.orders = orders

    def generate_bill(self):
        print("\n\n=========== FINAL BILL ===========")
        print(f"Table Number: {self.table_number}")
        print(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
        print("-----------------------------------")

        grand_total = 0

        for item in self.orders:
            dish_name, price, quantity, total = item
            print(f"{dish_name} x{quantity}  =  ₹{total}")
            grand_total += total

        print("-----------------------------------")
        print(f"GRAND TOTAL: ₹{grand_total}")
        print("===================================")

        return grand_total

    def print_bill_to_file(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        filename = f"D:/Revathi/Biz Metric Internship/Python/Python Code/Bill_Table_{self.table_number}_{timestamp}.txt"

        with open(filename, "w", encoding="utf-8") as file:
            file.write("=========== RESTAURANT BILL ===========\n")
            file.write(f"Table Number: {self.table_number}\n")
            file.write(f"Date: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            file.write("---------------------------------------\n")

            grand_total = 0

            for item in self.orders:
                dish_name, price, quantity, total = item
                file.write(f"{dish_name} x{quantity} = ₹{total}\n")
                grand_total += total

            file.write("---------------------------------------\n")
            file.write(f"GRAND TOTAL: ₹{grand_total}\n")
            file.write("=======================================\n")

        print(f"Bill saved as '{filename}' successfully!")


def main():
    menu = Menu()
    menu.display_menu()

    try:
        table_number = int(input("\nEnter Table Number: "))
    except:
        print("Invalid Table Number")
        return

    order = Order(table_number)
    order.take_order()

    if len(order.orders) == 0:
        print("No items ordered.")
        logging.log(logging.INFO,"Stopped the procces no orders")
        return

    billing = Billing(table_number, order.orders)
    billing.generate_bill()

    choice = input("\nDo you want to print bill to text file? (y/n): ")
    if choice.lower() == 'y':
        billing.print_bill_to_file()
        logging.log(logging.INFO,"Process is completed")


if __name__ == "__main__":
    main()
