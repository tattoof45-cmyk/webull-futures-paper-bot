import os
from http.server import HTTPServer, BaseHTTPRequestHandler

class BotStatus(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b"Webull Futures Bot is running!")

port = int(os.environ.get("PORT", 8080))

server = HTTPServer(("0.0.0.0", port), BotStatus)
print("Futures bot server started")

server.serve_forever()
