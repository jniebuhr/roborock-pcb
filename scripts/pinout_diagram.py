###########################################
#
# Example script to build a
# pinout diagram. Includes basic
# features and convenience classes.
#
###########################################

from pinout.core import Group, Image
from pinout.components.layout import Diagram
from pinout.components.pinlabel import PinLabelGroup, PinLabel, Body
from pinout.components.text import TextBlock
from pinout.components import leaderline as lline
from pinout.components.legend import Legend


# Import data for the diagram
import data

# Create a new diagram
# The Diagram_2Rows class provides 2 panels,
# 'panel_01' and 'panel_02', to insert components into.
diagram = Diagram(1024, 800, "diagram")

# Add a stylesheet
diagram.add_stylesheet("styles.css", embed=True)

# Create a group to hold the pinout-diagram components.
graphic = diagram.add(Group(169, 42))

# Add and embed an image
hardware = graphic.add(Image("../assets/Roborock-CPAP_top.png", embed=True))

# Measure and record key locations with the hardware Image instance
hardware.add_coord("in_vcc", 324, 54)
hardware.add_coord("mot_pwm", 615, 306)
hardware.add_coord("fan_gnd", 340, 630)
# Other (x,y) pairs can also be stored here
hardware.add_coord("pin_pitch_v", 0, 30)
hardware.add_coord("pin_pitch_h", 30, 0)

# Create pinlabels on the left header
graphic.add(
    PinLabelGroup(
        x=hardware.coord("in_vcc").x,
        y=hardware.coord("in_vcc").y,
        pin_pitch=hardware.coord("pin_pitch_h", raw=True),
        label_start=(284, 10),
        label_pitch=(0, 30),
        scale=(-1, -1),
        labels=data.left_header,
        leaderline=lline.Curved(direction="vh"),
    )
)

# Create pinlabels on the lower header
graphic.add(
    PinLabelGroup(
        x=hardware.coord("fan_gnd").x,
        y=hardware.coord("fan_gnd").y,
        scale=(-1, 1),
        pin_pitch=hardware.coord("pin_pitch_h", raw=True),
        label_start=(300, 10),
        label_pitch=(0, 30),
        labels=data.lower_header,
        leaderline=lline.Curved(direction="vh"),
    )
)

# Create pinlabels on the right header
graphic.add(
    PinLabelGroup(
        x=hardware.coord("mot_pwm").x,
        y=hardware.coord("mot_pwm").y,
        pin_pitch=hardware.coord("pin_pitch_v", raw=True),
        label_start=(60, 0),
        label_pitch=(0, 30),
        labels=data.right_header,
    )
)

# Export the diagram via commandline:
# >>> py -m pinout.manager --export pinout_diagram.py diagram.svg
