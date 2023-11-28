# runs everything + dependencies, echoing "completed" when done:
all: plot.pdf
	echo "Completed"

# clear all intermediate files:
clean: 
	rm allLatLongCrash allLatLongTree tally plot.pdf

# get all latitude + longitude coordinates of car crashes and send to allLatLongCrash file:
allLatLongCrash: NYCcollisions.gz
	spark-submit ./allLatLongCrash.py > allLatLongCrash

# get all latitude + longitude coordinates of trees and send to allLatLongTree file:
allLatLongTree: TreeCensus.tsv
	spark-submit ./allLatLongTree.py > allLatLongTree

# tally up all the car crashes + trees by quadrant and send to tally file:
tally: allLatLongCrash allLatLongTree
	python3 ./tally.py > tally

# plot the information from the tally file and send it to plot.pdf:
plot.pdf: tally
	python3 ./tallyPlot.py
