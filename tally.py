# helper function to convert a float number to the standardized conversion form:
def convert(num:float, div=.005):
    return str(num//div)

# helper function to populate a dictionary with "latide | longitude" tallies:
def createQuads(line: str, div: float, dic: dict):
    # split on pipe character:
    new = line.split("|")

    # get the latitude and longitude, converting to float:
    latitude = float(new[0].strip())
    longitude = float(new[1].strip())

    # divide by .005 to create a standardized conversion for all points
    # (essentially making a grid):
    k = convert(latitude, div) + "|" + convert(longitude, div)

    # tally using the parameter dictionary:
    if k not in dic:
        dic[k] = 1
    else:
        dic[k] += 1

# establish which number all coordinate points will be divided by (it will
# be the same for all of them so it's standardized):
div = 0.005

# tally the trees:
f = open("allLatLongTree", "rt") # open file for reading
line = f.readline()

# tree tally dictionary:
tree = {}

while line:
    createQuads(line, div, tree)
    line = f.readline() # read the next line

f.close()  # close the file

# tally the crashes:
g = open("allLatLongCrash", "rt") # open file for reading
line = g.readline()

# crash tally dictionary:
crash = {}  

while line:
    createQuads(line, div, crash)
    line = g.readline() # read the next line

g.close() # close the file

# if the key is in both dictionaries, print the key, followed by a colon
# and then the tree tally, a comma, and then the crash tally:
for key in tree:
    if key in crash:
        print(str(key) + ":" + str(tree[key]) + "," + str(crash[key]))
