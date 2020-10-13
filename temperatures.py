import csv


class TemperatureStatistics:
    def __init__(self, year, month, start_date, end_date):

        self.year = year  # TODO set year(instead of user input) here and in a loop
        self.month = month

        self.start_date = start_date
        self.end_date = end_date

        if self.month < 10:
            self.start_date = (self.year + "-" + "0" + str(self.month) + "-" + "01")
        else:
            self.start_date = (self.year + "-" + str(self.month) + "-" + "01")

        if end_date > 30:
            self.end_date = (self.year + "-" + str(self.month) + "-" + "31")  # TODO modify 31 days, how reach date in csv-file?
        else:
            self.end_date = (self.year + "-" + str(self.month) + "-" + "30")

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
