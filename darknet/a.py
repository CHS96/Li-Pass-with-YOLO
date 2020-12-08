import sys
import os
import http.server
import socketserver
import webbrowser

password = sys.argv[1]
print('Password : ' + password)
url = 'http://localhost:8080'
webbrowser.open(url)
os.system('python3 -m http.server 8080 --bind 127.0.0.1')
