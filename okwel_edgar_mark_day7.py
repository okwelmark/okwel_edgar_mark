import pandas as pd

# Sample data
data = {
    'ID': [1, 2, 3, 4, 5, 6, 6, 7],
    'Name': ['John Doe', 'Jane Smith', 'Bob Johnson', None, 'Alice Brown', 'Charlie Davis', 'Charlie Davis', 'Eve White'],
    'Age': [28, 34, 45, 30, 27, None, None, 22],
    'Salary': [50000, None, 75000, 60000, 48000, 70000, 70000, 52000],
    'JoinDate': ['2021-05-15', '2021-06-01', '2021-07-20', '2021-08-10', '2021-09-12', None, None, '2021-10-01']
}

# Creating DataFrame
df = pd.DataFrame(data)
print("Original DataFrame:")
print(df)

# Handling missing values without inplace parameter
df['Name'] = df['Name'].fillna('Unknown')
df['Age'] = df['Age'].fillna(df['Age'].mean())
df['Salary'] = df['Salary'].fillna(df['Salary'].median())
df['JoinDate'] = df['JoinDate'].fillna(df['JoinDate'].mode()[0])

print("\nCleaned DataFrame:")
print(df)
