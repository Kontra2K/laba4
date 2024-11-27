import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime

csv_file = 'employees.csv'
try:
    df = pd.read_csv(csv_file)
except Exception as e:
    print("Failed to open CSV file:", e)
    exit()

gender_counts = df['Gender'].value_counts()
print("Gender counts:")
print(gender_counts)

gender_counts.plot(kind='bar', title='Employee Gender Distribution')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

today = datetime.today()
df['BirthDate'] = pd.to_datetime(df['BirthDate'])
df['Age'] = (today - df['BirthDate']).dt.days // 365
age_categories = {
    'Younger than 18': df[df['Age'] < 18],
    '18-45': df[(df['Age'] >= 18) & (df['Age'] <= 45)],
    '45-70': df[(df['Age'] > 45) & (df['Age'] <= 70)],
    'Older than 70': df[df['Age'] > 70]
}

print("Age category counts:")
for category, data in age_categories.items():
    print(f"{category}: {len(data)}")

age_counts = {category: len(data) for category, data in age_categories.items()}
plt.figure()
plt.bar(age_counts.keys(), age_counts.values())
plt.title('Employee Age Distribution')
plt.xlabel('Age Category')
plt.ylabel('Count')
plt.show()

for category, data in age_categories.items():
    gender_age_counts = data['Gender'].value_counts()
    print(f"\n{category} Gender counts:")
    print(gender_age_counts)

    plt.figure()
    gender_age_counts.plot(kind='bar', title=f'{category} Gender Distribution')
    plt.xlabel('Gender')
    plt.ylabel('Count')
    plt.show()
