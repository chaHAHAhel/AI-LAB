import webbrowser
import time

# Open Edge browser and search for "guess"
webbrowser.register('edge', None, webbrowser.BackgroundBrowser("C:\\Program Files (x86)\\Microsoft\\Edge\\Application\\msedge.exe"))
webbrowser.get('edge').open('https://www.bing.com/search?q=guess')
 