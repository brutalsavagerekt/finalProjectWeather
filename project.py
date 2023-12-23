# def main():
#     ...


# def function_1():
#     ...


# def function_2():
#     ...


# def function_n():
#     ...


# if __name__ == "__main__":
#     main()
import requests

def current_weather(city):
    api_key = "---"
    api_call = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"

    response = requests.get(api_call)
    response.raise_for_status()
    data = response.json()
    print(f"Location: {data['location']['name']}, {data['location']['region']}, {data['location']['country']}")
    print(f"Local Time: {data['location']['localtime']}")
    print(f"Current Temperature: {data['current']['temp_c']}°C")
    print(f"Condition: {data['current']['condition']['text']}")
    print(f"Wind: {data['current']['wind_kph']} km/h from {data['current']['wind_dir']}")
    print(f"Humidity: {data['current']['humidity']}%")
    return response.raise_for_status()


current_weather("London")