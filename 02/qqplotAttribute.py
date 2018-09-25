__author__ = 'ubuntu'
import numpy as np
import pylab
import scipy.stats as stats
import urllib.request  ## jgwei, replace urllib2 with urllib.request (similarly in usage)
import matplotlib.pyplot as plt
import sys

target_url = ("https://archive.ics.uci.edu/ml/machine-learning-"
"databases/undocumented/connectionist-bench/sonar/sonar.all-data")

data = urllib.request.urlopen(target_url)


#arrange data into list for labels and list of lists for attributes
xList = []
labels = []

for line in data:
    #split on comma
    row = line.decode().strip().split(",")  #jgwei, added decode()
    xList.append(row)
nrow = len(xList)
ncol = len(xList[1])

type = [0]*3
colCounts = []

#generate summary statistics for column 3 (e.g.)
col = 3
colData = []
for row in xList:
    colData.append(float(row[col]))


#stats.probplot(colData, dist="norm", plot=pylab)
#pylab.show()
stats.probplot(colData, dist="norm", plot=plt)
plt.show()
