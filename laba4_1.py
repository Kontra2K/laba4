import csv
import random
from faker import Faker

fake = Faker()

male_names = [fake.first_name_male() for _ in range(1000)]
female_names = [fake.first_name_female() for _ in range(1000)]
surnames = [fake.last_name() for _ in range(2000)]

data = []
for i in range(2000):
    gender = 'Male' if i < 1200 else 'Female'
    first_name = random.choice(male_names) if gender == 'Male' else random.choice(female_names)
    data.append({
        "Surname": random.choice(surnames),
        "Name": first_name,
        "Patronymic": fake.last_name(),
        "Gender": gender,
        "BirthDate": fake.date_of_birth(minimum_age=15, maximum_age=86).strftime('%Y-%m-%d'),
        "Position": fake.job(),
        "City": fake.city(),
        "Address": fake.address().replace('\n', ' '),
        "Phone": fake.phone_number(),
        "Email": fake.email()
    })

csv_file = 'employees.csv'
with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
    writer = csv.DictWriter(file, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)

print("CSV file created successfully.")
