from temperatures import TemperatureStatistics


def main():

    city = input("Please enter a city (Arvika/Hemavan/Idre/Ljusnedal/Sylarna): ")
    month = int(input("Please enter a month (m): "))

    accuracy_number = int(input("Please choose accuracy (number of years back - max 10 yrs): "))
    start_date = accuracy_number

    year = start_date
    end_date = month

    city1 = TemperatureStatistics(year, month, start_date, end_date, accuracy_number, city)

    if month == 1:
        month = "January"
    elif month == 2:
        month = "February"
    elif month == 3:
        month = "March"
    elif month == 4:
        month = "April"
    elif month == 5:
        month = "May"
    elif month == 6:
        month = "June"
    elif month == 7:
        month = "July"
    elif month == 8:
        month = "August"
    elif month == 9:
        month = "September"
    elif month == 10:
        month = "October"
    elif month == "11":
        month = "November"
    else:
        month = "December"

    result = city1.avg_temp()
    print('\n'f"You can expect around {result} {'C°'} in {city} in {month}")


if __name__ == '__main__':
    main()
