from BaseHTTPServer import BaseHTTPRequestHandler,HTTPServer
from os import curdir, sep

PORT_NUMBER = 8050


class myHandler(BaseHTTPRequestHandler):
	
	
	def do_GET(self):
		if self.path=="/":
			self.path="/simple.html"

		try:
			

			sendReply = False
			if self.path.endswith("simple.html"):
				mimetype='text/html'
				sendReply = True

			if sendReply == True:
				
				f = open(curdir + sep + self.path) 
				self.send_response(200)
				self.send_header('Content-type',mimetype)
				self.end_headers()
				self.wfile.write(f.read())
				f.close()
			return


		except IOError:
			self.send_error(404,'File Not Found: %s' % self.path)

try:
	
	server = HTTPServer(('', PORT_NUMBER), myHandler)
	print 'Started httpserver on port ' , PORT_NUMBER
	
	
	server.serve_forever()

except KeyboardInterrupt:
	print '^C received, shutting down the web server'
	server.socket.close()