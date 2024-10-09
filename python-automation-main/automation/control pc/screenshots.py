from mss import mss
import time
from datetime import datetime

interval = 600

while True:
    with mss() as screen:
        current_time = datetime.now().strftime('%Y-%m-%d %H_%M_%S')
        filepath = f"{current_time}.png"
        screen.shot(output=filepath)

    print(filepath)
    time.sleep(interval) # Wait 600 sec/ 10 min