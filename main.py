from temperatures import TemperatureStatistics


def main():

    year = input("Please enter a year (yyyy): ")
    month = int(input("Please enter a month (m): "))

    start_date = year
    end_date = month

    city1 = TemperatureStatistics(year, month, start_date, end_date)

    result = city1.avg_temp()
    print('\n'f"You can expect around {result} {'C°'}")


if __name__ == '__main__':
    main()
