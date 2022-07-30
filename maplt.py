#! python3
#from audioop import add
import webbrowser, sys, pyperclip

chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s'
google_map_path = 'google.com/maps/place/'

#take the split, create a new string with + between each

if len(sys.argv) > 1:
    #get address from CL
    address = ' '.join(sys.arg[1:])

#TODO: Get address from clipboard
else:
    #Get the address from the clipboard
    address = pyperclip.paste()

webbrowser.get(chrome_path).open(google_map_path + address)