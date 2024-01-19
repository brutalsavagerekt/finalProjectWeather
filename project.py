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
import csv
import json
import os

from prettytable import from_csv

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
print(f"{GREEN}****************************************************{GREEN}{RESET}{RESET}")

## ## welcome message end 


def main():
    while True:
        print(f"{RESET}If you wanna read log file, please type command{RESET} {CYAN}'history'{CYAN}, {RESET}for exit type {RESET}{CYAN}'exit'{CYAN}")
        city = input(f"{RESET}Please enter city or command:{RESET} ")
        
        if city.lower() == 'exit':
            print("Goodbye! Have a nice day!")
            break
        if  city.lower() == 'history':
            history_log()
            break
        
        try:
            api_key = ""
            api_call = f"https://api.weatherapi.com/v1/current.json?key={api_key}&q={city}&aqi=no"
            response = requests.get(api_call)
            response.raise_for_status()
            data = response.json()
            logging(data)
            emergency(data)
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
            print(f"{CYAN}Wind:{CYAN} {RESET}{data['current']['wind_kph']} km/h from {data['current']['wind_dir']}{RESET}")
            print(f"{BLUE}Humidity:{BLUE} {RESET}{data['current']['humidity']}%{RESET}")
            return response.raise_for_status()
        except requests.exceptions.HTTPError as err:
            if response.status_code == 400:
                print("Hmm...we couldn't find this location. Please try again or type exit to stop application.")
            else:
                print(f"Error log: {err}")


def csv_cheker(file_csv):
    is_file_exist = os.path.isfile(file_csv) and os.path.getsize(file_csv) > 0
    return is_file_exist

def logging(collected_data):
    file_csv = 'log.csv'
    is_file_exist = csv_cheker(file_csv)
    # is_file_exist = os.path.isfile(file_csv) and os.path.getsize(file_csv) > 0
    with open(file_csv, 'a', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)

        if not is_file_exist:
            writer.writerow(['Location', 'Local Time', 'Current Temperature', 'Condition', 'Wind', 'Humidity'])
        
        writer.writerow([collected_data['location']['name'], collected_data['location']['localtime'], collected_data['current']['temp_c'], 
                         collected_data['current']['condition']['text'], collected_data['current']['wind_kph'], 
                         collected_data['current']['humidity']])
        

    print(f"Record added to {file_csv}")
    


def history_log():
    file_csv = 'log.csv' #создает переменную в которой хранит название файла
    is_file_exist = csv_cheker(file_csv) # вызывает функцию проверки существует ли файл

    if not is_file_exist: # если файлда нет, он выводит сообщение что файла нет
        print("There is not history file yet :(")

    if is_file_exist: #ксли он существует, то он читает его и с помощью функции читения из файла выводит таблицу в консоль from prettytable import from_csv
        with open(file_csv) as fp:
            mytable = from_csv(fp)
            print(mytable) 
        

def emergency(collected_data):
    if collected_data['current']['temp_c'] > 30 or collected_data['current']['temp_c'] < -20:
        print(f"{RED}****************************************************{RED}")
        print(f"{RED}*{RED}       {YELLOW} Attention, extreme temperature recorded {YELLOW}  {RED}*{RED}")
        print(f"{RED}****************************************************{RED}{RESET}{RESET}")

    if collected_data['current']['wind_kph'] > 90:
        print(f"{RED}****************************************************{RED}")
        print(f"{RED}*{RED}       {YELLOW} Caution: Extreme wind speeds detected.{YELLOW}  {RED}*{RED}")
        print(f"{RED}****************************************************{RED}{RESET}{RESET}")

if __name__ == "__main__":
    main()