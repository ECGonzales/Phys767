import matplotlib.pyplot as plt
import csv
from mpl_toolkits.mplot3d import Axes3D

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

# graph()

# To make interactive (i.e add axes labels for this particular file) use: import plottingmonte as plotm
# To plot from the python console plotm.graph()


# ------------------------------------------------------------------------------------------------
# Making a 3D plot of the information
# ------------------------------------------------------------------------------------------------
fig = plt.figure()
ax = fig.add_subplot(111, projection = '3d')

def threeDplot():
    """ Make a 3D plot """
    with open('MonteCarlo.csv', 'r') as montecarlo:
        data = csv.reader(filter(lambda row: row[0] != '#', montecarlo), delimiter=',')
        for eachline in data:  # filter(lambda row: row[0] != '#' lets the csv reader skip comments
            percentROI = float(eachline[0])  # Defining which each variable is in the csv file
            wagersizepercent = float(eachline[1])
            wagercount = float(eachline[2])
            pcolor = eachline[3]

            ax.scatter(wagersizepercent, wagercount, percentROI, color=pcolor)
            ax.set_xlabel('wager percent size')
            ax.set_ylabel('wager count')
            ax.set_zlabel('Percent ROI')

    plt.show()
