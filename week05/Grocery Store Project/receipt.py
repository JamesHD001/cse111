"""
Author: Henry Daniel James

Description:
Create a program that uses the following details;
    Read the products inventory from the file products.csv.
    Read the customer's order from the file request.csv
    For each item in the order, look up the product in the catalog. Use the catalog information to calculate and display the order.
    Display the order receipt.
    
Creativity:
    Custom store branding and clean receipt formatting added.
    Added a 10% discount feature

"""
import os; os.system('cls')
import datetime
import csv

def read_dictionary(filename, key_column_index):
    product_dict = {}
    with open(filename, 'rt') as productscsv:
        csvreader = csv.reader(productscsv, delimiter=",")
        next(csvreader)
        for row in csvreader:
            key_value = row[key_column_index]
            product_dict[key_value] = row
    return product_dict

def main():
    KEY_INDEX = 0
    now = datetime.datetime.now()

    print("Welcome To Big Uncle's Online Grocery Store!\n")
    print("Items Purchased:")
    print("--------------------------------------------------------")

    total_items = 0
    subtotal = 0
    tax = 0.006
    sales_tax = 0
    total = 0
    discount_rate = 0.10
    discount_amount = 0
    final_total = 0

    try:
        product_dict = read_dictionary('products.csv', KEY_INDEX)

        with open('request.csv', 'rt') as customer_request:
            csvreader = csv.reader(customer_request)
            next(csvreader)

            for row in csvreader:
                product_id = row[0]
                quantity = int(row[1])

                product = product_dict[product_id]
                product_name = product[1]
                product_price = float(product[2])

                print(f"{product_name}: {quantity} @ {product_price:.2f}")

                total_items += quantity
                subtotal += quantity * product_price

        discount_amount = subtotal * discount_rate
        discounted_subtotal = subtotal - discount_amount

        sales_tax = discounted_subtotal * tax
        total = discounted_subtotal + sales_tax
        final_total = total


    except KeyError as keyerror:
        print(f"Error: unknown product ID {keyerror}")

    except FileNotFoundError as filenotfound:
        print("Error: missing file")
        print(filenotfound)

    finally:
        print("================== PURCHASE RECEIPT ====================")
        print(f"Number of items: {total_items}")
        print(f"Subtotal: {subtotal:.2f}")
        print(f"Discount (10%): -{discount_amount:.2f}")
        print(f"Sales Tax: {sales_tax:.2f}")
        print(f"Total: {final_total:.2f}")
        print(now.strftime("%a %b %d %H:%M:%S %Y"))
        print("Thank you for shopping with us! See you next time.")
        print("========================================================")

if __name__ == "__main__":
    main()