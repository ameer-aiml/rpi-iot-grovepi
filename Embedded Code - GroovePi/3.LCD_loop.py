from grove_rgb_lcd import *
from time import sleep
setRGB(0,255,0) # (Green) RGB Pattern

for i in range(5):
    setText(str(i))
    #setText_norefresh(i)
    time.sleep(0.5)


# NOTE : TypeError: object of type 'int' has no len()
# Convert int to str
