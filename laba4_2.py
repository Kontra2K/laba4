import pandas as pd
from datetime import datetime

csv_file = 'employees.csv'
try:
    df = pd.read_csv(csv_file)
except Exception as e:
    print("Failed to open CSV file:", e)
    exit()

today = datetime.today()
df['BirthDate'] = pd.to_datetime(df['BirthDate'])
df['Age'] = (today - df['BirthDate']).dt.days // 365

younger_18 = df[df['Age'] < 18]
age_18_45 = df[(df['Age'] >= 18) & (df['Age'] <= 45)]
age_45_70 = df[(df['Age'] > 45) & (df['Age'] <= 70)]
older_70 = df[df['Age'] > 70]

excel_file = 'employees.xlsx'
try:
    with pd.ExcelWriter(excel_file) as writer:
        df.to_excel(writer, sheet_name='all', index=False)
        younger_18.to_excel(writer, sheet_name='younger_18', index=False)
        age_18_45.to_excel(writer, sheet_name='18-45', index=False)
        age_45_70.to_excel(writer, sheet_name='45-70', index=False)
        older_70.to_excel(writer, sheet_name='older_70', index=False)

    print("XLSX file created successfully.")
except Exception as e:
    print("Failed to create XLSX file:", e)
