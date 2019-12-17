# Python Notifications
 Show notifications with python tkinter

Example:
```
import Notification

x = 1570
y = 955
width = 350
height = 75

Notification.notification('Battery', 'Battery monitor\nStarted successfully',
             1000, 'black', Notification.averageColorInverted(width, height, x, y),
             'black', width, height, x ,y)
```
![Dark background](https://github.com/IntrovertedCoder/Python-Notifications/blob/master/Dark%20background%20test.png)
Because of the darker background the text became lighter.

![Light background](https://github.com/IntrovertedCoder/Python-Notifications/blob/master/Light%20background%20test.png)
Because of the ligher background the text became darker.
This will work for other colors, just black and white are easier to show.
