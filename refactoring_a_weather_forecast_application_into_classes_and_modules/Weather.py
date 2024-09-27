# Objective: The aim of this assignment is to refactor an existing Python script for a weather forecast application into a more structured, object-oriented, and modular format. The focus will be on identifying parts of the script that can be encapsulated into classes and organizing these classes into appropriate modules to enhance code readability, maintainability, and scalability.

# Task 1: Identifying and Creating Classes Analyze the provided script and identify distinct functionalities that can be encapsulated into classes. Create classes that represent different aspects of the weather forecast application, such as fetching data, parsing data, and user interaction.

# Problem Statement: The existing script for the weather forecast application is written in a procedural style and lacks organization.

# Expected Outcome:

# Clear definitions of classes such as `WeatherDataFetcher`, `DataParser`, and `UserInterface`, each handling specific parts of the application.

class DataFetcher:
    def __init__(self):
        self.data = {
            "New York": {"temperature": 70, "condition": "Sunny", "humidity": 50, "city": "New York"},
            "London": {"temperature": 60, "condition": "Cloudy", "humidity": 65, "city": "London"},
            "Tokyo": {"temperature": 75, "condition": "Rainy", "humidity": 70, "city": "Tokyo"}
        }
        
    def fetch_weather_data(self,city):
        # Simulated function to fetch weather data for a given city
        print(f"Fetching weather data for {city}...")
        return self.data.get(city, {})

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
        self.city=city
        self.data=data
        # Function to provide a detailed weather forecast for a city
        data = DataFetcher.fetch_weather_data(self.city)
        return DataParser.parse_weather_data(self.data)

    def display_weather(self,city):
        self.city=city
        self.data=data
        # Function to display the basic weather forecast for a city
        data = DataFetcher.fetch_weather_data(self.city)
        if not data:
            print(f"Weather data not available for {self.city}")
        else:
            weather_report = DataParser.parse_weather_data(self.data)
            print(weather_report)

class UserInterface:
    def __init__(self):
        pass
    def main():
        while True:
            city = input("Enter the city to get the weather forecast or 'exit' to quit: ")
            if city.lower() == 'exit':
                break
            detailed = input(f"Do you want a detailed forecast for {city}? (yes/no): ").lower()
            if detailed == 'yes':
                forecast = DataParser.get_detailed_forecast(city)
            else:
                forecast = DataParser.display_weather(city)
            print(forecast)

UserInterface.main()
