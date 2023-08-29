from __future__ import print_function
import os
from src.infi.systray.traybar import SysTrayIcon
import ctypes

icon_path = os.path.join(os.path.dirname(__file__), "test.ico")
def say_hello(systray):
    print("Exit")

menu_options = (("Exit", None, SysTrayIcon.QUIT),)
systray = SysTrayIcon("test.ico", "Icon", menu_options)
systray.start()
systray.shutdown()