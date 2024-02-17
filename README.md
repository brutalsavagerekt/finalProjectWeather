### DSMP (Digital Societas Meteorologica Palatina) Weather app

#### Video demo: https://youtu.be/g2IURrVwNcc

#### Description
The first systematic records of weather began to be kept in Ancient China. As early as the 4th century BC, Chinese astronomers kept records of meteorological phenomena such as winds, precipitation and fogs, which they considered in the context of astrological predictions and effects on crops. In Europe, one of the first to systematically record weather data was the Italian scientist Francesco Petrarca in the 14th century. He recorded weather observations during his travels and studies.

However, systematic and daily records of weather as we understand them today began much later. The first coordinated and systematic meteorological observations on a regular basis began with the work of Ludwig von Butch in Germany and the founding in 1780 of the Societas Meteorologica Palatina (Mannheimer Meteorologische Gesellschaft) in Mannheim, Germany, which is one of the first meteorological societies in the world.

The DSMP program is a tool that can tell you about the current weather anywhere in the world, warn about extreme weather conditions, and provide complete information about basic weather metrics. The program can also store the history of recordings, add notes to the data and read them conveniently in the console.

The program uses a free API - https://www.weatherapi.com/

For the program to work correctly, you need to add your API key in the project.py file:
```python
api_key = "PUT_YOUR_API_KEY"
```
The main function is responsible for the main functionality and provides the user with a choice:
- Find out the weather by entering the city
- View recording history
- Exit the program

![image](https://github.com/brutalsavagerekt/finalProjectWeather/assets/33382983/f45b8b7a-8530-4d44-b608-6076cd6a5e8a)

If the user chooses to check the weather, the console displays information for the selected location. The user will also be asked to add their observations as a weather note. If the user adds a message, it will be saved in history.

![image](https://github.com/brutalsavagerekt/finalProjectWeather/assets/33382983/7e2dc077-5923-40d0-8742-045cb3d1274a)

If, when starting the program, the user chooses to read the history, the module **prettytable** displays a table in the console.

![image](https://github.com/brutalsavagerekt/finalProjectWeather/assets/33382983/f0b1f755-4355-465a-b4df-9e457e484de9)

In addition, the program notifies about extreme weather conditions, such as temperatures above 30 degrees Celsius and below -20. As well as wind speeds of more than 90 kilometers per hour.

![image](https://github.com/brutalsavagerekt/finalProjectWeather/assets/33382983/b87f4edd-7130-4503-b7ea-f4712a7d68a8)

#### File structure
- log.csv - this is csv file containe all logs
- project.py - main python file that contain all functionality
- requirements.txt - txt file with all dependecies
- temp_test_file.csv - mock file for testing purposes
- test_project.py - python files with test for functions
