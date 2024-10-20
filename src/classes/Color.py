try:
    from colorama import Fore, Style, init
    init()
    coloramaImported = True
except:
    coloramaImported = False

import os
import platform

class Color():
    platforms = ['8', '10', '11']
    if (os.name == 'nt' and platform.release() not in platforms) or (coloramaImported == False):
        black = lblack = red = lred = green = lgreen = yellow = lyellow = blue = lblue = magenta = lmagenta = cyan = lcyan = white = lwhite = reset = ''
    else:
        black = Fore.BLACK
        lblack = Fore.LIGHTBLACK_EX
        red = Fore.RED
        lred = Fore.LIGHTRED_EX
        green = Fore.GREEN
        lgreen = Fore.LIGHTGREEN_EX
        yellow = Fore.YELLOW
        lyellow = Fore.LIGHTYELLOW_EX
        blue = Fore.BLUE
        lblue = Fore.LIGHTBLUE_EX
        magenta = Fore.MAGENTA
        lmagenta = Fore.LIGHTMAGENTA_EX
        cyan = Fore.CYAN
        lcyan = Fore.LIGHTCYAN_EX
        white = Fore.WHITE
        lwhite = Fore.LIGHTWHITE_EX
        reset = Style.RESET_ALL
