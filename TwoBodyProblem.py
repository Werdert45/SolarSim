
G = 6.67e-11
m1 = 2.0e30
m2 = 3.3e23
au = 1.5e8
day = 24.0*60*60
gravCons = G*m1*m2


# Sun initial position/velocity
x1 = 0
y1 = 0


vx1 = 0
vy1 = 0


# Earth initial position/velocity
x2 = 1.0*au
y2 = 0


vx2 = 0
vy2 = 25920


t = 0
dt = 0.1*day

# Empty lists to append the positions into
x1list = []
y1list = []

x2list = []
y2list = []

n = 1
for n in range(5):
    rx = x2-x1
    ry = y2-y1


    r3 = (rx**2+ry**2)

    fx = -gravCons*rx/r3
    fy = -gravCons*ry/r3


    # Earth

    vx2 += fx*dt/m2
    vy2 += fy*dt/m2


    x2 += vx2*dt
    y2 += vy2*dt


    # Sun

    vx1 += -fx*dt/m1
    vy1 += -fy*dt/m1


    x1 += -vx1*dt
    y1 += -vy1*dt


    x1list.append(x1)
    y1list.append(y1)

    x2list.append(x2)
    y2list.append(y2)

    t += dt
