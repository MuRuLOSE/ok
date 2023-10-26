import http.server
import socketserver
import os
import urllib.parse

class MyRequestHandler(http.server.SimpleHTTPRequestHandler):
    def do_GET(self):
        try:
            file_path = urllib.parse.unquote(self.path)
            file_path = file_path.lstrip('/')
            file_path = os.path.join(os.getcwd(), file_path)

            if not os.path.exists(file_path) or not os.path.isfile(file_path):
                self.send_error(404, "Файл не найден")
                return

            with open(file_path, 'rb') as file:
                file_content = file.read()

            self.send_response(200)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(file_content)

        except Exception as e:
            self.send_error(500, str(e))

def run_server(port):
    try:
        handler = MyRequestHandler
        with socketserver.TCPServer(("", port), handler) as httpd:
            print(f"Serving at port {port}")
            httpd.serve_forever()
    except OSError as e:
        print(f"Error starting server: {e}")

if __name__ == "__main__":
    run_server(8000)
