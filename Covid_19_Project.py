import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
# Load the dataset
try:
    df = pd.read_csv("owid-covid-data.csv")
    print("Data loaded successfully!")
except FileNotFoundError:
    print("Dataset not found. Make sure 'owid-covid-data.csv' is in your working directory.")

# Preview structure
print(df.columns)
print(df.head())

# Check missing values
print(df.isnull().sum())


# Filter countries
countries = ['Kenya', 'India', 'United States']
df = df[df['location'].isin(countries)]

# Convert date column
df['date'] = pd.to_datetime(df['date'])

# Fill missing values
df.fillna(0, inplace=True)




# Plot total cases over time
plt.figure(figsize=(10,6))
for country in countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_cases'], label=country)

plt.title("Total COVID-19 Cases Over Time")
plt.xlabel("Date")
plt.ylabel("Total Cases")
plt.legend()
plt.show()

plt.figure(figsize=(10,6))
for country in countries:
    country_data = df[df['location'] == country]
    plt.plot(country_data['date'], country_data['total_vaccinations'], label=country)

plt.title("Vaccination Progress Over Time")
plt.xlabel("Date")
plt.ylabel("Total Vaccinations")
plt.legend()
plt.show()


