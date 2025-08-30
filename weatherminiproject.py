import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df=pd.read_csv("C:\\Users\\nitin\\Desktop\\Weather_Data.csv")
print(df.head())

df['Date']=pd.to_datetime(df['Date/Time'])

print(df.info())
print(df.describe())

plt.figure(figsize=(12, 6))
plt.plot(df['Date/Time'],df['Temp_C'],color='yellow')
plt.title('Temperature Over Time')
plt.xlabel('Date/Time')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.show()

plt.figure(figsize=(8, 6))
sns.histplot(df['Dew Point Temp_C'],kde=True,color='blue')
plt.title('Dew Point Temp_C')
plt.xlabel('Dew Point(%)')
plt.show()

plt.figure(figsize=(6, 5))
sns.boxplot(data=df,y='Wind Speed_km/h')
plt.title('Wind Speed Spread')
plt.show()

plt.figure(figsize=(10, 6))
sns.countplot(data=df,x='Weather',order=df['Weather'].value_counts().index)
plt.xticks(rotation=45)
plt.title('Frequency of Weather Conditions')
plt.show()