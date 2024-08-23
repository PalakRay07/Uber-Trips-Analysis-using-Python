
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read data
data = pd.read_csv("C:/Users/super/Downloads/uber-raw-data-sep14.csv")

# Check for missing values (optional)
print(data.isnull().sum())  # Check for missing values

# Convert Date/Time to datetime
data["Date/Time"] = pd.to_datetime(data["Date/Time"])

# Extract features
data["Day"] = data["Date/Time"].dt.day
data["Weekday"] = data["Date/Time"].dt.weekday
data["Hour"] = data["Date/Time"].dt.hour

# Print first few rows
print(data.head())

# Set theme (optional)
sns.set_theme()

# Distribution plots
sns.histplot(data["Day"], kde=True, label="Day of Month")
sns.histplot(data["Hour"], kde=True, label="Hour of Day")
sns.histplot(data["Weekday"], kde=True, label="Weekday")
plt.legend()

# Heatmap - Weekday vs Hour (correlation)
df = data.groupby(["Weekday", "Hour"]).apply(lambda x: len(x))
df = df.unstack()
sns.heatmap(df, annot=False, cmap="YlGnBu")

# Scatter plot - Lon vs Lat with point size based on Day
plt.figure(figsize=(12, 8))
data.plot(
    kind="scatter", x="Lon", y="Lat", alpha=0.4, s=data["Day"], label="Uber Trips", cmap="viridis"
)
plt.title("Uber Trips Analysis")
plt.legend()
plt.show()
