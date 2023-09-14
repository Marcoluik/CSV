import csv
import matplotlib
import matplotlib.pyplot as plt

Time = []
distance = []
velocity = []
acceleration = []

with open ("files/drag_racer.csv") as datafil:
    # "," adskiller elementer
    csv_laeser = csv.reader(datafil, delimiter=",")
    next(csv_laeser)
    for linje in csv_laeser:
        #omdanner alle til floats
        tid, dist, vel, acc = [float(element) for element in linje]
        Time.append(tid)
        distance.append(dist)
        velocity.append(vel)
        acceleration.append(acc)
plt.style.use("seaborn-darkgrid")
fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,tight_layout=True, figsize = (10,8))
fig.suptitle("Drag Racer Data", fontsize=16)


ax1.plot(Time, distance, "-", color="blue", label="Distance")
ax1.set_xlabel("Time (s)")
ax1.set_ylabel("Distance (m)")
ax1.legend()


ax2.plot(Time, velocity, "-", color="green", label="Velocity")
ax2.set_xlabel("Time (s)")
ax2.set_ylabel("Velocity (m/s)")
ax2.legend()


ax3.plot(Time, acceleration, "-", color="red", label="Acceleration")
ax3.set_xlabel("Time (s)")
ax3.set_ylabel("Acceleration (m/s^2)")
ax3.legend()

plt.show()