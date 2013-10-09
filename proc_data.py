from math import log

# Compute average yearly growth from year idx1 to idx2
# inside index
def yearly_growth(idx1, idx2, index):
    t = idx2-idx1 # number of years
    if t <= 0:
        return -1
    b = float(index[idx1])
    #print "b = %f" % b
    e = float(index[idx2])
    #print "e = %f" % e
    r = e/b
    #print "r = %f" % r
    lr = log(r)
    #print "lr = %f" % lr
    t = float(t)
    #print "t = %f" % t
    yr = lr/t
    #print "yr = %f" % yr
    return yr * 100.0

# Given an index of yearly numbers, computes the average
# yearly growth rate for all 30 year periods
def compute_30(index):
    yearly_30_avg = []
    for k in range(len(index)-30):
        x = yearly_growth(k,k+30,index)
        yearly_30_avg.append(x)
    return yearly_30_avg
