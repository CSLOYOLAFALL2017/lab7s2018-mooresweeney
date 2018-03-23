# Programmers: Brendan Sweeney and Brendan Moore
# Course: CS151.02, Professor Franceschi
# Date: 3/23/18
# Lab Assignment: Lab 7
# Problem Statement: This program reads a file input by the user and outputs the highest movie profit and writes the list to a new file.
# Data In: file name
# Data Out: highest profit, list to new file
# Other Files: movies.csv and test.csv

def error(): # tests whether or not the input name of a file is valid
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



def profit(file): # finds the highest profit among the list of movies
    profitB = 0
    for line in file:
        date, name, budget, revenue = line.split(",")
        budget = float(budget)
        revenue = float(revenue)
        profitA = revenue - budget
        if profitA > profitB: # compares current profit to previous profits of the loop, sorts through and finds the highest
          profitB = profitA
    return profitB


def write(file):#opens file to write into another file
    filename = open("file", "w")
    new_file = input("what is the new name of the file")
    information = output.write(file)





def main():#calls the other functions and outputs the information for the user
    fileName = error()
    highestProfit = profit(fileName)
    print(" ")
    print("The movie with the highest profit made $%.2f" % highestProfit)




main()

