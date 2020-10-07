import csv


def main():

    with open("ljusnedal_date_time.csv", "r") as file:
        text = csv.reader(file)

        next(text)

        for line in text:
            split_line = line[0].split(";")
            date = split_line[0]
            temp = float(split_line[1])

            while "2010-10-01" <= date <= "2010-10-31":
                print(date, "the temp was: ", temp)
                break


        # temperatures = []


if __name__ == '__main__':
    main()
