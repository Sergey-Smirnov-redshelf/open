import http.server
import socketserver

# This variable is needed to process client requests to the server.
handler = http.server.SimpleHTTPRequestHandler

# The server run on port 1234.
with socketserver.TCPServer(("", 1111), handler) as httpd:

    # The server will run continuously, waiting for requests from the client.
    httpd.serve_forever()
