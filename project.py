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

## color palette
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"


## welcome message start

print(f"{GREEN}****************************************************{GREEN}")
print(f"{GREEN}*                                                  *{GREEN}")
print(f"{GREEN}*{GREEN}       {MAGENTA} WELCOME TO THE WEATHER APPLICATION {MAGENTA}       {GREEN}*{GREEN}")
print(f"{GREEN}*                                                  *{GREEN}")
print(f"{GREEN}****************************************************{GREEN}")

## ## welcome message end 


def current_weather():
    city = input(f"{RESET}Please enter city:{RESET} ")
    api_key = ""
    api_call = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"

    response = requests.get(api_call)
    response.raise_for_status()
    data = response.json()
    print(f"Location: {YELLOW}{data['location']['name']}, {data['location']['region']}, {data['location']['country']}{YELLOW}")
    print(f"{RESET}Local Time: {data['location']['localtime']}{RESET}")
    if data['current']['temp_c'] < 0:
        print(f"Current Temperature: {CYAN}{data['current']['temp_c']}°C{CYAN} 🌡️")
    if data['current']['temp_c'] > 0 and data['current']['temp_c'] < 20:
        print(f"Current Temperature: {YELLOW}{data['current']['temp_c']}°C{YELLOW} 🌡️")
    if data['current']['temp_c'] > 0 and data['current']['temp_c'] > 20:
        print(f"Current Temperature: {RED}{data['current']['temp_c']}°C{RED} 🌡️")    
    
    # print(f"Current Temperature: {data['current']['temp_c']}°C 🌡️")
    print(f"{RESET}Condition: {data['current']['condition']['text']}{RESET}")
    print(f"Wind: {data['current']['wind_kph']} km/h from {data['current']['wind_dir']}")
    print(f"Humidity: {data['current']['humidity']}%")
    return response.raise_for_status()


current_weather()
