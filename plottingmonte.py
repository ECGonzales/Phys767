import matplotlib.pyplot as plt
import csv


# Plotting the results of the monte carlo for determining which wager
def graph():
    """ Plotting the results of a csv file for monte carlo example """
    with open('MonteCarlo.csv', 'r') as montecarlo:
        data = csv.reader(filter(lambda row: row[0] != '#', montecarlo), delimiter=',')
        for eachline in data:                       # filter(lambda row: row[0] != '#' lets the csv reader skip comments
            percentROI = float(eachline[0])          # Defining which each variable is in the csv file
            wagersizepercent = float(eachline[1])
            wagercount = float(eachline[2])
            pcolor = eachline[3]

            plt.scatter(wagersizepercent, wagercount, color=pcolor)

    plt.show()

graph()
