from http.server import BaseHTTPRequestHandler, HTTPServer

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        try:
            file_path = self.path[1:]
            file_content = open(file_path, encoding='utf-8').read()
            self.send_response(200)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(bytes(file_content, 'utf-8'))
        except FileNotFoundError:
            self.send_response(404)
            self.send_header('Content-type', 'text/plain; charset=utf-8')
            self.end_headers()
            self.wfile.write(bytes("Файл не найден", 'utf-8'))

def run():
    print('Запуск сервера...')
    server_address = ('', 8080)
    httpd = HTTPServer(server_address, MyHandler)
    print('Сервер работает на порту 8080')

    httpd.serve_forever()

run()
