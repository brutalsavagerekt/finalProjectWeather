import pytest
import os
from project import csv_cheker, emergency 
from io import StringIO
import sys


## color palette
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
BLUE = "\033[94m"
MAGENTA = "\033[95m"
CYAN = "\033[96m"
WHITE = "\033[97m"
RESET = "\033[0m"


def test_csv_cheker_existing_file():
    test_filename = 'test_file.csv'
    with open(test_filename, 'w') as file:
        file.write('some data')

    assert csv_cheker(test_filename) == True
    os.remove(test_filename)

def test_csv_cheker_non_existing_file():
    assert csv_cheker('non_existing_file.csv') == False


def test_csv_cheker_empty_file():
    test_filename = 'empty_test_file.csv'
    open(test_filename, 'a').close()

    assert csv_cheker(test_filename) == False
    os.remove(test_filename)


# Функция для перехвата вывода
def capture_output(function, *args, **kwargs):
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    function(*args, **kwargs)
    output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    return output

def test_emergency_high_wind():
    data = {'current': {'temp_c': 20, 'wind_kph': 100}}
    output = capture_output(emergency, data)

    expected_output = (
        f"{RED}****************************************************{RED}\n"
        f"{RED}*{RED}       {YELLOW} Caution: Extreme wind speeds detected.{YELLOW}  {RED}*{RED}\n"
        f"{RED}****************************************************{RED}{RESET}{RESET}\n"
    )

    assert output == expected_output

def test_emergency_hot_temperature():
    data = {'current': {'temp_c': 31, 'wind_kph': 20}}
    output = capture_output(emergency, data)
    expected_output = (
        f"{RED}****************************************************{RED}\n"
        f"{RED}*{RED}       {YELLOW} Attention, extreme temperature recorded {YELLOW}  {RED}*{RED}\n"
        f"{RED}****************************************************{RED}{RESET}{RESET}\n"
    )

    assert output == expected_output


def test_emergency_normal_conditions():
    data = {'current': {'temp_c': 20, 'wind_kph': 10}}
    output = capture_output(emergency, data)

    expected_output = ('')
    assert output == expected_output