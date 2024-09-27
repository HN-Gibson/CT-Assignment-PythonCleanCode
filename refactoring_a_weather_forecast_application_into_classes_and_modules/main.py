# Objective: The aim of this assignment is to refactor an existing Python script for a weather forecast application into a more structured, object-oriented, and modular format. The focus will be on identifying parts of the script that can be encapsulated into classes and organizing these classes into appropriate modules to enhance code readability, maintainability, and scalability.

# Task 1: Identifying and Creating Classes Analyze the provided script and identify distinct functionalities that can be encapsulated into classes. Create classes that represent different aspects of the weather forecast application, such as fetching data, parsing data, and user interaction.

# Problem Statement: The existing script for the weather forecast application is written in a procedural style and lacks organization.

# Expected Outcome:

# Clear definitions of classes such as `WeatherDataFetcher`, `DataParser`, and `UserInterface`, each handling specific parts of the application.

class Weather:
    def __init__(self):
        self.data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
        }

class DataFetcher:
    def __init__(self):
        pass
        
    def fetch_weather_data(self,city):
        # Simulated function to fetch weather data for a given city
        print(f"Fetching weather data for {city}...")
        return Weather.data(city, "Weather data not available for this city.")

class DataParser:
    def __init__(self):
        pass

    def parse_weather_data(self,data):
        # Function to parse weather data
        if not data:
            return "Weather data not available"
        city =data["city"]
        temperature = data["temperature"]
        condition = data["condition"]
        humidity = data["humidity"]
        return f"Weather in {city}: {temperature} degrees, {condition}, Humidity: {humidity}%"

    def get_detailed_forecast(self,city):
        # Function to provide a detailed weather forecast for a city
        data = DataFetcher.fetch_weather_data(city)
        return DataParser.parse_weather_data(data)

    def display_weather(self,city):
        # Function to display the basic weather forecast for a city
        data = DataFetcher.fetch_weather_data(city)
        if not data:
            print(f"Weather data not available for {city}")
        else:
            weather_report = DataParser.parse_weather_data(data)
            print(weather_report)

class UserInterface(Weather):
    def main():
        while True:
            city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
            if city.lower() == 'exit':
                break
            detailed = input("Do you want a detailed forecast? (yes/no): ").lower()
            if detailed == 'yes':
                forecast = DataParser.get_detailed_forecast(city)
            else:
                forecast = DataParser.display_weather(city)
            print(forecast)

# if __name__ == "__main__":
#     main()

UserInterface.main()

