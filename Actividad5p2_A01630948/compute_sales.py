"""
Mariana Gonzalez Bravo, A01630948
File that, from two JSON files, one containing a price list
and the other a list of sold products, calculates
the total sales. It prints it on the console and
appends it to a .txt file.
"""
import json
import time
import sys
import os


def total_cost_f(prices, sales_record):
    """
    Calculates the total cost and lists products not found
    """
    total_cost = 0
    nf_products = []

    for sale in sales_record:
        product_name = sale["Product"]
        quantity = sale["Quantity"]

        product_info = next(
            (item for item in prices if item["title"] == product_name),
            None
        )

        if product_info:
            product_cost = product_info["price"] * quantity
            total_cost += product_cost
        else:
            nf_products.append(product_name)

    return round(total_cost, 2), nf_products


def read_json(file_path):
    """
    Reads JSON
    """
    with open(file_path, 'r', encoding='utf-8') as file:
        return json.load(file)


def write_file(results_file, filename, total_cost, results_exist):
    """
    Write results
    """
    if not results_exist:
        results_file.write("Total\n")

    filename_without_extension = os.path.splitext(filename)[0]

    results_file.write(f"{filename_without_extension}    ${total_cost}\n")



def print_warnings(nf_products):
    """
    Products not found
    """
    for product in nf_products:
        print(f"'{product}' no se encuentra en la lista de precios\n")


def get_filename(file_path):
    """
    Obtain filename
    """
    return os.path.splitext(os.path.basename(file_path))[0]


def main():
    """
    Obtain total costs and print results
    """
    if len(sys.argv) != 3:
        return

    prices_path = sys.argv[1]
    sales_record_path = sys.argv[2]

    try:
        start_time = time.time()

        prices = read_json(prices_path)
        sales_record = read_json(sales_record_path)

        total_cost, nf_products = total_cost_f(prices, sales_record)
        filename = get_filename(sales_record_path)

        results_exist = os.path.isfile("SalesResults.txt")

        with open("SalesResults.txt", "a", encoding='utf-8') as results_file:
            write_file(results_file, filename, total_cost, results_exist)

        print_warnings(nf_products)

        print(f"{filename}    ${total_cost}")
        end_time = time.time()
        execution_time = round(end_time - start_time, 2)
        print(f"Tiempo total de ejecucion: {execution_time} s")

    except FileNotFoundError:
        print("Error: No se encuentra el archivo")
    except json.JSONDecodeError:
        print("Error: No se pudo decodificar el JSON")


if __name__ == "__main__":
    main()
