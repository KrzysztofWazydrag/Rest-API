from csv import DictReader
from datetime import datetime

class PdfReport():
    def __init__(self):
        self.row = []
    def save(self, filename: str):
def read_file(filename: str):
    employee_report = {}

    with open(filename,'r', encoding='utf8') as file:
        reader = DictReader(file)
        for row in reader:
            start_date = datetime.strptime(row['Start Date'],'%Y-%m-%d %H:%M:%S')
            end_date = datetime.strptime(row['End Date'],'%Y-%m-%d %H:%M:%S')
            employee = row['Employee']
            customer = row['Client Name']
            time_delta = end_date - start_date

            if employee in employee_report:
                employee_report[employee] += time_delta
            else:
                employee_report[employee] = time_delta

    return employee_report

report = read_file('logs.txt')

for employee, duration in report.items():
    hours, remainder = divmod(duration.total_seconds(), 3600)
    minutes, _ =divmod(remainder, 60)
    #print("Czas pracy", employee, int(hours), 'godzin', int(minutes), 'minut')
    print(f'Pracownik {employee} Czas pracy: {hours} godzin i {minutes} minut.')
