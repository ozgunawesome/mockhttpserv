#!/c/python27/python
from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
class requestHandler(BaseHTTPRequestHandler):
  def do_GET(self):
    self.send_response(200)
    self.end_headers()
    return
  def do_POST(self): do_GET(self)
  def do_HEAD(self): do_GET(self)
try:
  server = HTTPServer(('', 2680), requestHandler)
  server.serve_forever()
except KeyboardInterrupt:
  server.socket.close()
