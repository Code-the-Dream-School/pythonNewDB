import csv
import random
import math
from faker import Faker
from faker_commerce import Provider
fake = Faker()
fake.add_provider(Provider)

with open('./employees.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['employee_id', 'first_name', 'last_name', 'phone'])
    for i in range(1,21):
        writer.writerow([i,fake.first_name(),fake.last_name(), fake.country_calling_code() +
                          ' ' + fake.phone_number()])
    file.close()

with open('./products.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['product_id', 'product_name', 'price'])
    for i in range(1,60):
        price = random.random() * 10.0
        price = round(price,2)
        writer.writerow([i, fake.ecommerce_name(), price])
    file.close()

with open('./customers.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['customer_id', 'customer_name', 'contact', 'street', 'city', 'country', 
                     'postal_code', 'phone'])
    for i in range(1,101):
        phone = fake.country_calling_code() + ' ' + fake.phone_number()
        writer.writerow([i,fake.company(), fake.name(), fake.street_address(), fake.city(), 
                         fake.country(), fake.postalcode(), phone ])
    file.close()

date_array = []
for i in range(250):
    date_array.append(fake.date())
date_array.sort()
line_id = 1
with open('./orders.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerow(['order_id','date','customer_id','employee_id'])
    with open('./line_items.csv', 'w') as file2:
        writer2 = csv.writer(file2)
        writer2.writerow(['line_item_id','order_id','product_id','quantity'])
        for i in range(1,250):
            customer_id = math.trunc(random.random() * 100) + 1
            employee_id = math.trunc(random.random() * 20 ) + 1
            writer.writerow([i, date_array[i],customer_id,employee_id])
            item_count = math.trunc(random.random() * 8) + 1
            for j in range (1, item_count+1):
                product_id = math.trunc(random.random() * 60) + 1
                quantity = math.trunc(random.random() * 20) + 1
                writer2.writerow([line_id, i, product_id, quantity])
                line_id += 1
        file2.close()
    file.close()
