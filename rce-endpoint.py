from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, unquote
import argparse
import os
import subprocess

class MyServer(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200) 
        self.send_header("Content-type", "text/html") 
        self.end_headers()
        url_decode = unquote(self.path)
        url = urlparse(url_decode)
        result = processing_request(url.path, url.query)
        self.wfile.write(bytes(f"{result}\n", "utf-8"))

def create_parser():
    parser = argparse.ArgumentParser()
    parser.add_argument('-a', '--server_address', default=False, help='Server address (default: 8080)')
    parser.add_argument('-p', '--server_port', default=False, help='Server port (default: 127.0.0.1')
    parser.add_argument('-u', '--url_path', default=False, help='Usrl path (default: "/ping")')
    parser.add_argument('-q', '--query_params', default=False, help='Query params (default: "/ping?ip=")')
    parser.add_argument('-c', '--call_command', default=False, help='Called command (default: "ping -c 3 $QUERY_PARAMS")')
    script_arg = parser.parse_args()
    return script_arg

def call_command(query_params):
    result = subprocess.check_output(f'{CALL_COMMAND} {query_params}', stderr=subprocess.STDOUT, shell=True)
    return result

def print_info(request_path, query):
    print(f"Path: '{request_path}'")
    print(f"Query params: '{query[0]}'")
    print(f"Quer value: '{query[1]}'")

def processing_request(request_path, request_query):
    if request_path == f"{URL_PATH}":
        query = request_query.split("=")
        print_info(request_path, query)
        if query[0] == f"{QUERY_PARAMS}":
            query_params = query[1]
            result = call_command(query_params)
    return result

script_arg = create_parser()

ADDRESS_SERVER= script_arg.server_address or "127.0.0.1"
SERVER_PORT = int(script_arg.server_port) or 8080
URL_PATH = script_arg.url_path or "/ping"
QUERY_PARAMS = script_arg.query_params or "ip"
CALL_COMMAND = script_arg.call_command or "ping -c 3"

def main():
    try:
        simple_server = HTTPServer((ADDRESS_SERVER, SERVER_PORT), MyServer)
        print(f"Server started http://{ADDRESS_SERVER}:{SERVER_PORT}")

        simple_server.serve_forever()
    except KeyboardInterrupt:
        simple_server.server_close()
        print("Server stopped.")

if __name__ == "__main__":        
    main()