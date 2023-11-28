import math
import matplotlib.pyplot as plt
import numpy as np

f = open("tally","rt")  # open the tally file for reading
line = f.readline()

# x and y arrays to be later plotted:
x = []
y = []

while line:
    # split on a colon to make an array with array[0] = latitude,longitude and
    #array[1] = treeTally,crashTally:
    split = line.split(":")

    # split the tallies on a comma, which will create an array with array[0] =
    # tree tally and array[1] = crash tally (stripping to eliminate starting +
    # ending whitespace):
    new = split[1].strip().split(",")

    # the x axis measures number of trees and the y axis measures number of car
    # crashes, so add the tree tally to the x array and the crash tally to the
    # y array (taking the log of the values to make the graph more readable):
    x.append(math.log(int(new[0])))
    y.append(math.log(int(new[1])))
    line = f.readline() # read the next line

f.close() # close the file

# create a figure instance that will later be written to a pdf:
fig = plt.figure()

# make the scatter plot:
plt.scatter(x,y,color="#588157",alpha = 0.5)

# label axes:
plt.xlabel("Number of Trees")
plt.ylabel("Number of Motor Vehicle Collisions")
plt.title("Number of Trees and Motor Vehicle Collisions per 1820 sq ft in NYC")

# create line of best fit/trendline (instructions found on:
# https://www.statology.org/matplotlib-trendline/):
z = np.polyfit(x,y,1) # linear trendline
p = np.poly1d(z)
plt.plot(x,p(x),color="#576d81") # plot trendline on graph

# save the plot into a pdf file (plot.pdf):
fig.savefig("plot.pdf")
