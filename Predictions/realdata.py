
from pylab import plot, xlabel, ylabel, show, xlim, ylim, scatter

#Initial conditions
xbottom = 0.01
xtop = 1.0
rbottom = 2.4
rtop = 4.0
spacing = 0.01

#Initials lists
rlist = []
xlist = []

def logisticmap(x, r):
    return r * x * (1-x)

r = 0
x = 0

while r <= rtop:
    x = 0.01
    for i in range(int((xtop-xbottom)/spacing)):
        x = logisticmap(x,r)
        xlist.append(x)
        rlist.append(r)

    r += spacing

scatter(rlist,xlist, s=0.05)
ylim(xbottom, xtop)
xlim(rbottom, rtop)
xlabel("r")
ylabel("x")
show()
