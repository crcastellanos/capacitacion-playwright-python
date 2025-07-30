import http.server
import socketserver

PORT = 5502

Handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", PORT), Handler) as httpd:
    print(f"Servidor iniciado en http://127.0.0.1:{PORT}")
    httpd.serve_forever()
