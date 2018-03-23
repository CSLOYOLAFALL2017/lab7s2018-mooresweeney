
def error():
    filename = input("please enter a file name: ")
    file_not_found = True  # get inside loop at least once
    while (file_not_found):
        try:

            file = open(filename, "r")
            fileNotFound = False  # do not get back in loop
            # read from file
            return file


        except FileNotFoundError:  # ask for file name again
            filename = input("Enter a file name: ")



def profit(file):
    for line in file:
        date, name, budget, revenue = line.split(",")
        profit = revenue - budget

        return profit
def write():
    filename: open("file", "w")


def main():
    filename = error()
    profit = profit()

error()
