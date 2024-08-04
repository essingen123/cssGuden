import os
import http.server
import webbrowser
import socket

PORT = 8082  # Start from this port

# Find a free port
while True:
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)
        print(f"Trying port: {PORT}")
        print(f"Found free port: {PORT}")
        sock.close()  # Close the socket
        break

    except OSError:
        sock.close()
        PORT += 1


# Create a simple HTTP server
httpd = http.server.HTTPServer(("", PORT), http.server.SimpleHTTPRequestHandler)

print(f"Server started on port {PORT}")

# Open the browser to the server
webbrowser.open(f"http://localhost:{PORT}")

# Keep the server running
httpd.serve_forever()
