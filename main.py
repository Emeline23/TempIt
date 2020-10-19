from temperatures import TemperatureStatistics


def city_input():
    cities = ["Arvika", "Hemavan", "Idre", "Ljusnedal", "Sylarna"]
    city = input("Please enter a city (Arvika/Hemavan/Idre/Ljusnedal/Sylarna): ")
    while True:
        if city not in cities:
            city = input("Sorry, please enter a one of the available city names: ")
            # TODO lower city name
        else:
            return city


def month_input():
    while True:
        try:
            month = int(input("Please enter a month (m): "))
            if month < 1 or month > 12:
                raise ValueError
            return month
        except ValueError:
            print("Month must be given with a numeric value between 1 and 12")


def time_input():
    while True:
        try:
            time = input("Please choose time of the day (morning(m)/afternoon(a)/night(n)): ")
            if time == "m" or time == "a" or time == "n":
                # TODO fix time association
                return time
            else:
                raise ValueError
        except ValueError:
            print("Time of the day must be given with the letter 'm', 'a' or 'n'")


def accuracy_input():
    while True:
        try:
            accuracy_number = int(input("Please choose accuracy (number of years back - max 10 yrs): "))
            if accuracy_number < 1 or accuracy_number > 10:
                raise ValueError
            return accuracy_number
        except ValueError:
            print("Number of years must be given with a numeric value between 1 and 10")


def main():

    city = city_input()

    month = month_input()
    time = time_input()
    accuracy_number = accuracy_input()
    start_date = accuracy_number

    year = start_date
    end_date = month

    city1 = TemperatureStatistics(year, month, start_date, end_date, accuracy_number, city, time)

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
    elif month == 11:
        month = "November"
    else:
        month = "December"

    result = city1.avg_temp()
    print('\n'f"You can expect around {result} {'C°'} in {city} in {month} in the {time}")


if __name__ == '__main__':
    main()
