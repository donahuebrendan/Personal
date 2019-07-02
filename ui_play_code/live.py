import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from random import randint

# Create figure for plotting
fig = plt.figure(1)
ax = fig.add_subplot(2, 1, 1)
bx = fig.add_subplot(2, 1, 2)

xs = []
ys = []

xs1 = []
ys1 = []

def myrand1():
        return (randint(0, 9))

def myrand2():
        return (randint(0, 100))

# This function is called periodically from FuncAnimation
def animate(i, xs, ys):

    # Get Values
    temp_c = myrand1()
    
    # Add x and y to lists
    xs.append(dt.datetime.now())
    ys.append(temp_c)

    # Limit x and y lists to 20 items
    xs = xs[-20:]
    ys = ys[-20:]

    # Draw x and y lists
    ax.clear()
    ax.plot(xs, ys)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)
    #plt.title('TMP102 Temperature over Time')
    #plt.ylabel('Temperature (deg C)')

def animate1(i, xs1, ys1):

    # Get Values

    temp_c = myrand2()

    # Add x and y to lists
    xs1.append(dt.datetime.now())
    ys1.append(temp_c)

    # Limit x and y lists to 20 items
    xs1 = xs1[-20:]
    ys1 = ys1[-20:]

    # Draw x and y lists
    bx.clear()
    bx.plot(xs1, ys1)

    # Format plot
    plt.xticks(rotation=45, ha='right')
    plt.subplots_adjust(bottom=0.30)

# Set up plot to call animate() function periodically
ania = animation.FuncAnimation(fig, animate, fargs=(xs, ys), interval=1000)
anib = animation.FuncAnimation(fig, animate1, fargs=(xs1, ys1), interval=10)
plt.show()
