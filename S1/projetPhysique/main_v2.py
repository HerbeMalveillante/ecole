import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import math
import tkinter
import random

trajectories = []  # Creates the base list containing the trajectories


class Trajectory:
    """
    The class used to create and represent a trajectory
    """

    def __init__(self, initialSpeed, initialHeight, angle, gravity):
        """
        Initialize the trajectorieeeee
        """
        self.initialSpeed = initialSpeed
        self.initialHeight = initialHeight
        self.angle = angle
        self.gravity = gravity
        self.color = "#" + "".join(
            [str(hex(int(random.random() * 16)))[2:] for i in range(6)]
        )

    def get_trajectory(self):
        # Initialize the lists to store the values of the trajectory
        x = []
        y = []
        # Calculate the trajectory
        i = 0
        while True:
            x.append(i)
            y.append(
                self.initialHeight
                + (self.initialSpeed * math.sin(self.angle) * i)
                - (self.gravity * i * i) / 2
            )
            i += 0.1
            if y[-1] < 0:  # If the trajectory is over (ball touches the ground)
                break

        return x, y

    def get_trajectory_with_air_resistance(self):

        pass


def add_trajectory(listbox):
    """
    Add a trajectory to the list of trajectories
    Updates the listbox with the new trajectory.
    """
    trajectories.append(Trajectory(10, 10, math.pi / 4, 9.81))
    listbox.insert(tkinter.END, "Trajectory " + str(len(trajectories)))
    listbox.itemconfig(len(trajectories) - 1, bg=trajectories[-1].color)
    update_graph()


def remove_trajectory(listbox):
    """
    Remove a trajectory from the list of trajectories
    Updates the listbox with the removed trajectory.
    """
    try:
        w = listbox.curselection()[0]
    except IndexError:
        tkinter.messagebox.showinfo("Error", "Please select a trajectory")
        return
    trajectories.pop(w)
    listbox.delete(w)
    update_graph()


def on_select(
    event,
    label1,
    label2,
    label3,
    label4,
    label5,
    initialSpeedSlider,
    initialHeightSlider,
    angleSlider,
    gravitySlider,
):
    """
    When a trajectory is selected, update the labels and the sliders with the values of the selected trajectory
    """
    w = event.widget
    index = int(w.curselection()[0])
    traj = trajectories[index]

    w.itemconfig(index, bg=traj.color)
    label1.config(text=f"Initial speed (m/s) : {traj.initialSpeed}")
    label2.config(text=f"Initial height (m) : {traj.initialHeight}")
    label3.config(text=f"Angle (rad) : {traj.angle}")
    label4.config(text=f"Gravity (m/s^2) : {traj.gravity}")
    label5.config(text=f"Color (hex) : {traj.color}")
    initialSpeedSlider.set(traj.initialSpeed)
    initialHeightSlider.set(traj.initialHeight)
    angleSlider.set(traj.angle)
    gravitySlider.set(traj.gravity)


def on_update_slider(
    listbox, initialSpeedSlider, initialHeightSlider, angleSlider, gravitySlider
):
    """
    When the sliders are updated, update the values of the selected trajectory and the corresponding labels
    """
    try:
        w = listbox.curselection()[0]
    except IndexError:  # If no trajectory is selected
        tkinter.messagebox.showinfo("Error", "Please select a trajectory")
        return
    trajectories[w].initialSpeed = initialSpeedSlider.get()
    trajectories[w].initialHeight = initialHeightSlider.get()
    trajectories[w].angle = angleSlider.get()
    trajectories[w].gravity = gravitySlider.get()
    traj = trajectories[w]
    label1.config(text=f"Initial speed (m/s) : {traj.initialSpeed}")
    label2.config(text=f"Initial height (m) : {traj.initialHeight}")
    label3.config(text=f"Angle (rad) : {traj.angle}")
    label4.config(text=f"Gravity (m/s^2) : {traj.gravity}")
    label5.config(text=f"Color (hex) : {traj.color}")
    update_graph()


def update_graph():
    """
    Update the graph with the new trajectories.
    """

    global frame2  # The frame containing the graph. Must be global to be able to update it.
    frame2.destroy()  # Destroy the frame containing the graph
    frame2 = tkinter.Frame(root)  # Create a new frame
    frame2.grid(
        column=1, row=0
    )  # Place it in the second column and first row of the main window

    figureObject = plt.Figure(figsize=(6, 6), dpi=100)  # Create a new figure
    figure = figureObject.gca()  # Get the axis of the figure

    for i in trajectories:
        x, y = i.get_trajectory()  # Get the trajectory
        figure.plot(x, y, color=i.color)  # Plot the trajectory
    figure.set_xlabel("Time (s)")
    figure.set_ylabel("Height (m)")
    figure.set_title("Trajectory")
    figure.grid(True)
    canvas = FigureCanvasTkAgg(
        figureObject, master=frame2
    )  # Create a new canvas with the figure in it
    canvas.draw()  # Draw the canvas
    canvas.get_tk_widget().pack(
        side=tkinter.TOP, fill=tkinter.BOTH, expand=1
    )  # display the graph


root = tkinter.Tk()
root.title("projectile")

# adds four separate columns to the GUI
frame1 = tkinter.LabelFrame(root, text="Sliders")
frame1.grid(column=0, row=0)
frame2 = tkinter.LabelFrame(root, text="Graph")
frame2.grid(column=1, row=0)
frame3 = tkinter.LabelFrame(root, text="Select Trajectory")
frame3.grid(column=2, row=0)
frame4 = tkinter.LabelFrame(root, text="Trajectory info")
frame4.grid(column=3, row=0)


# adds four sliders to the first section
initialSpeedSlider = tkinter.Scale(
    frame1,
    length=200,
    from_=0,
    to=100,
    orient=tkinter.HORIZONTAL,
    label="Initial speed (m/s)",
    command=lambda _: on_update_slider(
        listbox, initialSpeedSlider, initialHeightSlider, angleSlider, gravitySlider
    ),
)
initialSpeedSlider.grid(column=0, row=0)
initialHeightSlider = tkinter.Scale(
    frame1,
    length=200,
    from_=0,
    to=100,
    orient=tkinter.HORIZONTAL,
    label="Initial height (m)",
    command=lambda _: on_update_slider(
        listbox, initialSpeedSlider, initialHeightSlider, angleSlider, gravitySlider
    ),
)
initialHeightSlider.grid(column=0, row=1)
angleSlider = tkinter.Scale(
    frame1,
    from_=0,
    length=200,
    to=math.pi,
    resolution=0.1,
    orient=tkinter.HORIZONTAL,
    label="Angle (rad)",
    command=lambda _: on_update_slider(
        listbox, initialSpeedSlider, initialHeightSlider, angleSlider, gravitySlider
    ),
)
angleSlider.grid(column=0, row=2)
gravitySlider = tkinter.Scale(
    frame1,
    from_=1,
    length=200,
    to=100,
    resolution=0.2,
    orient=tkinter.HORIZONTAL,
    label="Gravity (m/s^2)",
    command=lambda _: on_update_slider(
        listbox, initialSpeedSlider, initialHeightSlider, angleSlider, gravitySlider
    ),
)
gravitySlider.grid(column=0, row=3)

# adds a listbox to the third section
listbox = tkinter.Listbox(frame3)
listbox.grid(column=0, row=0)
listbox.bind(
    "<<ListboxSelect>>",
    lambda event: on_select(
        event,
        label1,
        label2,
        label3,
        label4,
        label5,
        initialSpeedSlider,
        initialHeightSlider,
        angleSlider,
        gravitySlider,
    ),
)
# adds the default trajectory to the listbox
add_trajectory(listbox)

# adds a button to the third section
button = tkinter.Button(
    frame3, text="Add Trajectory", command=lambda: add_trajectory(listbox)
)
button.grid(column=0, row=1)
# adds a button to the third section
button = tkinter.Button(
    frame3, text="Remove Trajectory", command=lambda: remove_trajectory(listbox)
)
button.grid(column=0, row=2)

# adds five labels to the fourth section
label1 = tkinter.Label(frame4, text=f"Initial speed (m/s) : None")
label1.grid(column=0, row=0)
label2 = tkinter.Label(frame4, text=f"Initial height (m) : None")
label2.grid(column=0, row=1)
label3 = tkinter.Label(frame4, text=f"Angle (rad) : None")
label3.grid(column=0, row=2)
label4 = tkinter.Label(frame4, text=f"Gravity (m/s^2) : None")
label4.grid(column=0, row=3)
label5 = tkinter.Label(frame4, text=f"Color : None")
label5.grid(column=0, row=4)

# draws the graph
update_graph()

# run the GUI
root.mainloop()
