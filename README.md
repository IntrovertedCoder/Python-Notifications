# Python Notifications
 Show notifications with python tkinter

Example:
'''
import Notification

x = 1570
y = 955
width = 350
height = 75

Notification.notification('Battery', 'Battery monitor\nStarted successfully',
             1000, 'black', Notification.averageColorInverted(width, height, x, y),
             'black', width, height, x ,y)
'''
