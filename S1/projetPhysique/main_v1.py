import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math
import tkinter


def draw_trajectory_graph(initialSpeed, initialHeight, angle, gravity):
    """
    Returns the x and y coordinates of the trajectory of the projectile.
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
    while True:
        x.append(i)
        y.append(
            initialHeight + (initialSpeed * math.sin(angle) * i) - (gravity * i * i) / 2
        )
        i += 0.05
        if y[-1] < 0:  # if the projectile hits the ground
            break  # stop the loop

    return x, y


# run the GUI
root = tkinter.Tk()
root.title("Projectile")
# root.geometry("800x800")


# adds two separate sections to the GUI
frame1 = tkinter.Frame(root)
frame1.grid(column=0, row=0)
frame2 = tkinter.Frame(root)
frame2.grid(column=1, row=0)

# update the graph automatically as the value of the sliders change
def update_graph(
    _,
):  # _ is a dummy variable because the function is called with an argument by default
    global frame2
    """clears the first section from any tkinter graph it contains and draws a new one using the values from the sliders."""
    frame2.destroy()
    frame2 = tkinter.Frame(root)
    frame2.grid(column=1, row=0)
    draw_graph(
        initialSpeedSlider.get(),
        initialHeightSlider.get(),
        angleSlider.get(),
        gravitySlider.get(),
    )


def draw_graph(initialSpeed, initialHeight, angle, gravity):  # draw the graph
    # adds the trajectory of the projectile in the first section
    figureObject = plt.Figure(figsize=(10, 10), dpi=100)
    figure = figureObject.gca()

    x, y = draw_trajectory_graph(
        initialSpeed, initialHeight, angle, gravity
    )  # get the coordinates of the trajectory
    figure.plot(x, y)  # plot the trajectory
    figure.set_xlabel("Time (s)")
    figure.set_ylabel("Height (m)")
    figure.set_title("Trajectory of a projectile")
    figure.text(
        0,
        0,
        "Initial speed = "
        + str(initialSpeed)
        + " m/s\nInitial height = "
        + str(initialHeight)
        + " m\nAngle = "
        + str(angle)
        + " rad\nGravity = "
        + str(gravity)
        + " m/s^2",
    )
    figure.grid(True)
    # display the graph in the first section of the tkinter GUI
    canvas = FigureCanvasTkAgg(figureObject, master=frame2)
    canvas.draw()
    canvas.get_tk_widget().pack(
        side=tkinter.TOP, fill=tkinter.BOTH, expand=1
    )  # display the graph


# adds four number selectors to the second section
initialSpeedSlider = tkinter.Scale(
    frame1,
    from_=0,
    to=200,
    orient=tkinter.HORIZONTAL,
    label="Initial speed (m/s)",
    command=update_graph,
    length=200,
)
initialSpeedSlider.pack()
initialSpeedSlider.set(10)
initialHeightSlider = tkinter.Scale(
    frame1,
    from_=0,
    to=100,
    orient=tkinter.HORIZONTAL,
    label="Initial height (m)",
    command=update_graph,
    length=200,
)
initialHeightSlider.pack()
initialHeightSlider.set(0)
angleSlider = tkinter.Scale(
    frame1,
    from_=0,
    to=math.pi,
    orient=tkinter.HORIZONTAL,
    resolution=0.1,
    label="Angle (rad)",
    command=update_graph,
    length=200,
)
angleSlider.pack()
angleSlider.set(math.pi / 4)
gravitySlider = tkinter.Scale(
    frame1,
    from_=1,
    to=50,
    orient=tkinter.HORIZONTAL,
    label="Gravity (m/s^2)",
    command=update_graph,
    length=200,
)
gravitySlider.pack()
gravitySlider.set(9.81)


root.mainloop()  # run the GUI
