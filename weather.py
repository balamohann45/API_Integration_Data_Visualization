import requests
import matplotlib.pyplot as plt
import seaborn as sns
import warnings
import json

warnings.filterwarnings("ignore")
sns.set(style='whitegrid')  # Clean background style

# API Setup
API_KEY = "38280eaf4afd2cd501147112a68734d6"  # Replace with your own key
CITY = "HYDERABAD"
URL = f"https://api.openweathermap.org/data/2.5/weather?q={CITY}&appid={API_KEY}&units=metric"

try:
    response = requests.get(URL)
    response.raise_for_status()
    data = response.json()

    # Extracting weather data
    temperature = data["main"]["temp"]
    humidity = data["main"]["humidity"]
    wind_speed = data["wind"]["speed"]
    description = data["weather"][0]["description"].title()
    city_name = data["name"]

    # Console Output
    print(f"\n🌤️  Weather Report: {city_name}")
    print(f"🌡️  Temperature: {temperature}°C")
    print(f"💧 Humidity: {humidity}%")
    print(f"🌬️  Wind Speed: {wind_speed} m/s")
    print(f"📝 Description: {description}\n")

    # Plotting
    plt.figure(figsize=(14, 8))

    # Bar Chart - Weather Metrics
    plt.subplot(2, 2, 1)
    metrics = ["Temperature (°C)", "Humidity (%)", "Wind Speed (m/s)"]
    values = [temperature, humidity, wind_speed]
    colors = ["#FF6F61", "#6BAED6", "#58D68D"]  # Warm, cool, neutral
    sns.barplot(x=metrics, y=values, palette=colors)
    plt.title(f"🌡️ Weather Metrics in {city_name}", fontsize=14, weight='bold')
    plt.xlabel("")
    plt.ylabel("Value")
    plt.xticks(rotation=15)

    # Pie Chart - Weather Description
    plt.subplot(2, 2, 2)
    plt.pie([1], labels=[description], autopct='%1.1f%%',
            startangle=140, colors=["#FAD7A0"])
    plt.title("📝 Weather Description", fontsize=14, weight='bold')

    # City Info Box
    plt.subplot(2, 2, 3)
    plt.axis('off')
    plt.text(0.5, 0.5, f"📍 City: {city_name}", fontsize=16,
             ha='center', va='center', bbox=dict(boxstyle="round,pad=0.5", facecolor="#AED6F1", edgecolor='black'))

    # Timestamp Box
    from datetime import datetime
    now = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    plt.subplot(2, 2, 4)
    plt.axis('off')
    plt.text(0.5, 0.5, f"🕒 Data Retrieved: {now}", fontsize=12,
             ha='center', va='center', bbox=dict(boxstyle="round,pad=0.3", facecolor="#D5F5E3", edgecolor='gray'))

    plt.tight_layout()
    plt.suptitle(f"📊 Current Weather Dashboard for {city_name}", fontsize=16, weight='bold', y=1.03)
    plt.show()

except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
except KeyError as e:
    print(f"Key Error: {e}")
except json.JSONDecodeError as e:
    print(f"JSON Decode Error: {e}")
except Exception as e:
    print(f"Unexpected Error: {e}")









    

