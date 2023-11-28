import pyspark
sc = pyspark.SparkContext()

# map: (latitude, longitude)
def mapper(line):
    # split on tab characters:
    fields = line.split("\t")
    try:
        lat = float(fields[4])
        longitude = float(fields[5])
    except:
        lat = 0
        longitude = 0

    return lat, longitude

# read from the NYC collisions file:
a = sc.textFile("NYCcollisions.gz")
pairs = a.map(mapper) # lat, long
pairFilter = pairs.filter(lambda x: x[0] != 0 and x[1] != 0) # lat, long (!= 0) 

# get all the pairs and print "lat | long":
test = pairFilter.collect()

for t in test:
    print(t[0], "|", t[1])
