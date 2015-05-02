#!/usr/bin/python
import matplotlib.pyplot as plt
import collections
import scipy.stats as stats

x = [1, 1, 1, 1, 1, 1, 1, 1, 2, 2, 2, 3, 4, 4, 4, 4, 5, 6, 6, 6, 7, 7, 7, 7, 7, 7, 7, 7, 8, 8, 9, 9]

# freqs
c = collections.Counter(x)
count_sum = sum(c.values())
for k,v in c.iteritems():
  print "The frequency of number " + str(k) + " is " + str(float(v) / count_sum)

# plots
plt.figure()
plt.boxplot(x)
plt.savefig("box.png")

plt.figure()
plt.hist(x, histtype='bar')
plt.savefig("hist.png")

# qq
plt.figure()
graph2 = stats.probplot(
    x, dist="norm", plot=plt
)
plt.savefig("qq.png")