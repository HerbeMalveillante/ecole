import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math
import tkinter

def draw_trajectory_graph(initialSpeed, initialHeight, angle, gravity):
    """
    Draws the trajectory of a projectile using matplotlib.
    :param initialSpeed: initial speed
    :param initialHeight: initial height
    :param angle: angle of the projectile
    :param gravity: gravity
    """
    # Initialize the lists to store the values of the trajectory
    x = []
    y = []
    # Calculate the trajectory
    i = 0
    while True :
        x.append(i)
        y.append(initialHeight + (initialSpeed * math.sin(angle) * i) - (gravity * i * i) / 2)
        i+=0.1
        if y[-1] < 0:
            break

    return x, y


# draw_trajectory_graph(100, 0, math.pi / 4, 9.81)

# run the GUI
root = tkinter.Tk()
root.title("Projectile")
root.geometry("400x400")


# adds two separate sections to the GUI
frame1 = tkinter.Frame(root)
frame1.pack()
frame2 = tkinter.Frame(root)
frame2.pack()

# adds four number selectors to the second section
initialSpeed = tkinter.Scale(frame1, from_=0, to=100, orient=tkinter.HORIZONTAL, label="Initial speed (m/s)")
initialSpeed.pack(side=tkinter.LEFT)
initialHeight = tkinter.Scale(frame1, from_=0, to=100, orient=tkinter.HORIZONTAL, label="Initial height (m)")
initialHeight.pack(side=tkinter.LEFT)
angle = tkinter.Scale(frame1, from_=0, to=math.pi, orient=tkinter.HORIZONTAL, label="Angle (rad)")
angle.pack(side=tkinter.LEFT)
gravity = tkinter.Scale(frame1, from_=0, to=10, orient=tkinter.HORIZONTAL, label="Gravity (m/s^2)")
gravity.pack(side=tkinter.LEFT)

# adds the trajectory of the projectile in the first section

figureObject = plt.Figure(figsize=(5, 4), dpi=100)
figure = figureObject.gca()

x, y = draw_trajectory_graph(initialSpeed.get(), initialHeight.get(), angle.get(), gravity.get())
# x, y = draw_trajectory_graph(100, 0, math.pi / 4, 9.81)
figure.plot(x, y)
figure.set_xlabel('Time (s)')
figure.set_ylabel('Height (m)')
figure.set_title('Trajectory of a projectile')
figure.text(0, 0, 'Initial speed = ' + str(initialSpeed.get()) + ' m/s\nInitial height = ' + str(initialHeight.get()) + ' m\nAngle = ' + str(angle.get()) + ' rad\nGravity = ' + str(gravity.get()) + ' m/s^2')
figure.grid(True)
# display the graph in the first section of the tkinter GUI
canvas = FigureCanvasTkAgg(figureObject, master=frame2)
canvas.draw()
canvas.get_tk_widget().pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)



root.mainloop()
