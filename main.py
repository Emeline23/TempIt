from temperatures import TemperatureStatistics


def main():

    month = int(input("Please enter a month (m): "))

    accuracy_number = int(input("Please choose accuracy (number of years back - max 10 yrs): "))
    start_date = accuracy_number

    year = start_date
    end_date = month

    city1 = TemperatureStatistics(year, month, start_date, end_date, accuracy_number)

    result = city1.avg_temp()
    print('\n'f"You can expect around {result} {'C°'}")


if __name__ == '__main__':
    main()