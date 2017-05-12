'''import SimpleHTTPServer
import SocketServer

PORT = 8080

Handler = SimpleHTTPServer.SimpleHTTPRequestHandler

httpd = SocketServer.TCPServer(("localhost", PORT), Handler)

print "serving at port", PORT
httpd.serve_forever()'''

from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer

PORT_NUMBER = 8040


class myHandler(BaseHTTPRequestHandler):
	
	
	def do_GET(self):
		self.send_response(200)
		self.send_header('Content-type','text/html')
		self.end_headers()
		
		self.wfile.write("Hello World !")
		self.wfile.write("hi")
		return

try:
	
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER
	
	
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()