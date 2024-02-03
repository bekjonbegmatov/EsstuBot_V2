from bs4 import BeautifulSoup
import requests
import json

''' 
THE CLEASS FOR GETTING SCHELDULE ANY GROUPS
    USING :
        INIT THE GROUP
    WHEN YOU INT THIS CLASS YOU SHUD BE PUT GROUP NAME
        FOR EXAMPLE
    Schedule(schedule='743')
        METHODS :
            Schedule(schedule='743').get_schedule()
    returns dic of schedule 
            Schedule(schedule='743').save_schedule_to_json(filename='file.json')
        arument filename : str - Output file name and end with .json
    Saves schedule into the JSON file 
 '''
class Schedule:

    # Init the class 
    def __init__(self, schedule_url: str) -> None:
        self.schedule_url = schedule_url
        self.main_url = 'https://portal.esstu.ru/bakalavriat/'

    # Prinate method for getting a page
    def __get_page(self):
        # url = f'{self.main_url}{self.schedule}.htm'
        data = requests.get(url=self.schedule_url)
        return data.text

    def __parse_page(self):
        '''Private method for parsing pagee '''
        data = self.__get_page()
        soup = BeautifulSoup(data, 'html.parser')
        schedule_data = []

        # Extracting time values
        time_row = soup.find_all('tr')[1]
        time_cells = time_row.find_all('td')[1:]
        time_values = [cell.get_text(strip=True).encode("latin-1").decode('cp1251') for cell in time_cells]

        # Extracting data for each day of the week
        days_rows = soup.find_all('tr')[2:]
        for day_row in days_rows:
            day_name_cell = day_row.find('td')
            day_name = day_name_cell.get_text(strip=True).encode("latin-1").decode('cp1251')

            # Extracting data for each pair
            pair_cells = day_row.find_all('td')[1:]
            pair_values = [cell.get_text(strip=True).encode("latin-1").decode('cp1251') for cell in pair_cells]

            # Creating a dictionary for the current day
            day_data = {
                'day': day_name,
                'schedule': [
                    {
                        'time': time,
                        'subject': subject
                    } for time, subject in zip(time_values, pair_values)
                ]
            }

            schedule_data.append(day_data)
        return schedule_data

    def get_schedule(self):
        '''The method for getting schedule'''
        schedule_data = self.__parse_page()
        # Output the schedule in JSON format
        return json.dumps(schedule_data, ensure_ascii=False, indent=2)
    
    def save_schedule_to_json(self, filename:str):
        '''The method for saving to the JSON FILE'''
        schedule_data = self.__parse_page()
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(schedule_data, f, ensure_ascii=False, indent=2)
        print(f'Schedule saved to {filename}')



# Schedule(schedule=45).save_schedule_to_json(filename='schedule.json')