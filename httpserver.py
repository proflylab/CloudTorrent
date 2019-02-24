import os
from http.server import SimpleHTTPRequestHandler, HTTPServer                                                                                                                                   

os.chdir('../content/drive')
http = HTTPServer(('', 8888), SimpleHTTPRequestHandler)
http.serve_forever()
