import csv

"""
def __str__(self):
    return f"{self.temp}, {self.date} {self.time}"""


class TemperatureStatistics:
    def __init__(self, year, month, start_date, end_date, accuracy_number):
        """self.city = city  # så länge som varje stad har en csv-fil
        self.date = date
        self.time = time
        self.temp = temps

        city, date, time, temp"""

        self.year = year
        self.month = month

        self.start_date = start_date
        self.end_date = end_date
        self.accuracy_number = accuracy_number

        for self.year in range(2020 - self.accuracy_number, 2020):
            self.year = (2019 - self.accuracy_number)
            self.year += 1
            if self.month < 10:
                self.start_date = (str(self.year) + "-" + "0" + str(self.month) + "-" + "01")
            else:
                self.start_date = (str(self.year) + "-" + str(self.month) + "-" + "01")

        months_31 = [1, 3, 5, 7, 8, 10, 12]
        months_30 = [4, 6, 9, 11]

        if self.month in months_31:
            self.end_date = (str(self.year) + "-" + str(self.month) + "-" + "31")
        elif self.month in months_30:
            self.end_date = (str(self.year) + "-" + str(self.month) + "-" + "30")
        else:
            self.end_date = (str(self.year) + "-" + str(self.month) + "-" + "27")

    def avg_temp(self):
        with open("ljusnedal.csv", "r") as file:
            text = csv.reader(file)

            next(text)

            sum_temp = 0
            line_count = 0

            for line in text:
                split_line = line[0].split(";")
                date = split_line[0]
                time = split_line[1]

                if self.start_date <= date <= self.end_date:
                    temp = float(split_line[2])
                    sum_temp += temp
                    line_count += 1
                    break
            return round(sum_temp / line_count, 1)
