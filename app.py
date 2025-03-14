## This function opens the CSV for You!
def csv_to_list(file_path):
    data_list = []
    
    with open(file_path, 'r') as file:
        for line in file:
            row = line.strip().split(',')
            row = [int(value) if value.isdigit() else value for value in row]
            data_list.append(row)

    return data_list


file_path = "SalesData.csv"  
data = csv_to_list(file_path)


def calcRow(data):
    row_totals = {}
    row_averages = {}

    for row in data[1:]:  # Skipping the first row
        store_name = row[0]  # First column is the store name
        sales = list(map(int, row[1:]))  # Convert sales to numbers
        total_sales = sum(sales)  # Sum up sales for the store
        average_sales = total_sales / len(sales)
        row_totals[store_name] = total_sales
        row_averages[store_name] = average_sales

    return row_totals, row_averages

total_sales, average_sales = calcRow(data)
individual_sales = average_sales.items()

for sale in individual_sales:
    store, avg = sale
    print(f"Store: {store}, Average Sales: {avg}")

def sort_profitable_stores(average_sales):
    sorted_stores = sorted(average_sales.items(), key=lambda x: x[1], reverse=True)
    return sorted_stores

sorted_stores = sort_profitable_stores(average_sales)
print(f"Sorted stores by average sales: {sorted_stores}")

def calculate_overall_average(average_sales):
    total_average_sales = sum(average_sales.values())
    number_of_stores = len(average_sales)
    overall_average = total_average_sales / number_of_stores
    return overall_average

overall_average_sales = calculate_overall_average(average_sales)
print(f"Overall average sales across all stores: ${overall_average_sales}")

def dangered_stores(average_sales):
    dangered_stores = {}
    for store, avg in average_sales.items():
        if avg < (overall_average_sales * 0.80):
            dangered_stores[store] = avg
dangered = dangered_stores(average_sales)

print(f"The stores that are in dangered is: {dangered}")