import csv


"""def __str__(self):
    return f"{self.temp}, {self.date} {self.time}"""


class TemperatureStatistics:  # Här kan man t.ex. räkna ut medeltemperaturen
    def __init__(self):
        """self.city = city  # så länge som varje stad har en csv-fil
        self.date = date
        self.time = time
        self.temp = temp

        city, date, time, temp"""

        # self.temps = []

    def add_temp(self, temp):
        self.temps.append(temp)


    def avg_temp(self):
        with open("ljusnedal.csv", "r") as file:
            text = csv.reader(file)

            next(text)

            sum_temp = 0
            line_count = 0

            month = input("Please choose a month: ")
            for line in text:
                split_line = line[0].split(";")
                date = split_line[0]
                time = split_line[1]

                if month.lower() == "january" or month == "1":
                    if "2019-01-01" <= date <= "2020-01-31":
                        temp = float(split_line[2])
                        sum_temp += temp
                        line_count += 1
                        break
                elif month.lower() == "february" or month == "2":
                    if "2019-02-01" <= date <= "2020-02-27":
                        temp = float(split_line[2])
                        sum_temp += temp
                        line_count += 1
                        break
                elif month.lower() == "march" or month == "3":
                    if "2019-03-01" <= date <= "2020-03-31":
                        temp = float(split_line[2])
                        sum_temp += temp
                        line_count += 1
                        break
                elif month.lower() == "april" or month == "4":
                    if "2019-04-01" <= date <= "2020-04-30":
                        temp = float(split_line[2])
                        sum_temp += temp
                        line_count += 1
                        break
                elif month.lower() == "may" or month == "5":
                    if "2019-05-01" <= date <= "2020-05-31":
                        temp = float(split_line[2])
                        sum_temp += temp
                        line_count += 1
                        break
                elif month.lower() == "june" or month == "6":
                    if "2019-06-01" <= date <= "2020-06-30":
                        temp = float(split_line[2])
                        sum_temp += temp
                        line_count += 1
                        break
                elif month.lower() == "july" or month == "7":
                    if "2019-07-01" <= date <= "2020-07-31":
                        temp = float(split_line[2])
                        sum_temp += temp
                        line_count += 1
                        break
                elif month.lower() == "august" or month == "8":
                    if "2019-08-01" <= date <= "2020-08-31":
                        temp = float(split_line[2])
                        sum_temp += temp
                        line_count += 1
                        break
                elif month.lower() == "september" or month == "9":
                    if "2019-09-01" <= date <= "2020-09-30":
                        temp = float(split_line[2])
                        sum_temp += temp
                        line_count += 1
                        break
                elif month.lower() == "october" or month == "10":
                    if "2019-10-01" <= date <= "2020-10-31":
                        temp = float(split_line[2])
                        sum_temp += temp
                        line_count += 1
                        break
                elif month.lower() == "november" or month == "11":
                    if "2019-11-01" <= date <= "2020-11-30":
                        temp = float(split_line[2])
                        sum_temp += temp
                        line_count += 1
                        break
                elif month.lower() == "december" or month == "12":
                    if "2019-12-01" <= date <= "2020-12-31":
                        temp = float(split_line[2])
                        sum_temp += temp
                        line_count += 1
                        break
            return round(sum_temp / line_count, 1)