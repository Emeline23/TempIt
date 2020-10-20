from temperatures import TemperatureStatistics


def city_input():
    cities = ["arvika", "hemavan", "idre", "ljusnedal", "sylarna"]
    city = input("Please enter a city (Arvika/Hemavan/Idre/Ljusnedal/Sylarna): ").lower()
    while True:
        if city not in cities:
            city = input("Sorry, please enter a one of the available city names: ").lower()
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
                if time == "m":
                    time_abbrev = "morning"
                elif time == "a":
                    time_abbrev = "afternoon"
                else:
                    time_abbrev = "night"
                return time, time_abbrev
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


def current_month(m):

    if m == 1:
        month = "January"
    elif m == 2:
        month = "February"
    elif m == 3:
        month = "March"
    elif m == 4:
        month = "April"
    elif m == 5:
        month = "May"
    elif m == 6:
        month = "June"
    elif m == 7:
        month = "July"
    elif m == 8:
        month = "August"
    elif m == 9:
        month = "September"
    elif m == 10:
        month = "October"
    elif m == 11:
        month = "November"
    else:
        month = "December"
    return month


def main():

    city = city_input()

    month = month_input()
    chosen_month = current_month(month)

    time, time_abbrev = time_input()
    accuracy_number = accuracy_input()
    start_date = accuracy_number

    year = start_date
    end_date = month

    city1 = TemperatureStatistics(year, month, start_date, end_date, accuracy_number, city, time)

    result = city1.avg_temp()
    print('\n'f"You can expect around {result} {'C°'} in {city.capitalize()} in the {time_abbrev} in {chosen_month} ")


if __name__ == '__main__':
    main()
