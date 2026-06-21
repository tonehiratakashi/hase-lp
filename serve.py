import http.server
import os

os.chdir("/Users/tonehira/Desktop/hase_lp")

handler = http.server.SimpleHTTPRequestHandler
httpd = http.server.HTTPServer(("", 3456), handler)
httpd.serve_forever()
