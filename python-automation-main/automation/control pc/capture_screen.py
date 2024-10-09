from mss import mss
import time
from datetime import datetime

with mss() as screen:
    screen.shot(output="myscreen.png")