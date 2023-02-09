from common.constants import bcolors
from objects import glob

def printServerStartHeader(asciiArt=True):
	"""
	Print server start message

	:param asciiArt: print BanchoBoat ascii art. Default: True
	:return:
	"""
	if asciiArt:
		printColored(r""" __    ___  __ _ 
/  |  /   |/ _(_)
`| | / /| | |_ _ 
 | |/ /_| |  _| |
_| |\___  | | | |
\___/   |_/_| |_|
                 
                 """,bcolors.GREEN)

	printColored(f"# Welcome to 14fi's bancho server.", bcolors.BLUE)
	printColored(f"# Thanks to osuHOW, RealistikOsu, osu!ainu, and Ripple.", bcolors.BLUE)

def printNoNl(string):
	"""
	Print a string without \n at the end

	:param string: string to print
	:return:
	"""
	print(string, end="")

def printColored(string, color):
	"""
	Print a colored string

	:param string: string to print
	:param color: ANSI color code
	:return:
	"""
	print("{}{}{}".format(color, string, bcolors.ENDC))

def printError():
	"""
	Print a red "Error"

	:return:
	"""
	printColored("Error", bcolors.RED)

def printDone():
	"""
	Print a green "Done"

	:return:
	"""
	printColored("Done", bcolors.GREEN)

def printWarning():
	"""
	Print a yellow "Warning"

	:return:
	"""
	printColored("Warning", bcolors.YELLOW)
