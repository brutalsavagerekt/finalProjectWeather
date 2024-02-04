import pytest
import os
from unittest.mock import patch
from project import csv_cheker, emergency, history_log, notes
import io
from io import StringIO
import sys
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

# csv_cheker function start
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
# csv_cheker function end

def capture_output(function, *args, **kwargs):
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    function(*args, **kwargs)
    output = sys.stdout.getvalue()
    sys.stdout = old_stdout
    return output

# test emergency function start
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

# test emergency function end

# test notes function start
def test_notes_not_added():
    with patch('builtins.input', return_value='n'):
        assert notes() == '---'

def test_notes_not_added_capital():
    with patch('builtins.input', return_value='N'):
        assert notes() == '---'

def test_notes_add_note():
    with patch('builtins.input', return_value='This is somple text for test'):
        assert notes() == 'This is somple text for test'

# test notes function end

# test history_log file exist
def test_history_log_file_not_exists():
    with patch('project.csv_cheker', return_value=False):
        with patch('sys.stdout', new_callable=io.StringIO) as fake_output:
            history_log()
            assert "There is not history file yet :(" in fake_output.getvalue()
