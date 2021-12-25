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
    parser.add_argument('-a', '--server_address', default=False, help='server_address')
    parser.add_argument('-p', '--server_port', default=False, help='server_port')
    script_arg = parser.parse_args()
    return script_arg

def ping_command(ip):
    result = subprocess.check_output(f'ping -c 3 {ip}', stderr=subprocess.STDOUT, shell=True)
    return result

def print_info(request_path, query):
    print(f"path: '{request_path}'")
    print(f"query_params: '{query[0]}'")
    print(f"quer_value: '{query[1]}'")

def processing_request(request_path, request_query):
    if request_path == "/ping":
        query = request_query.split("=")
        print_info(request_path, query)
        if query[0] == "ip":
            result = ping_command(query[1])
    return result


def main():
    try:
        script_arg = create_parser()

        address_server = script_arg.server_address or "localhost"
        server_port = int(script_arg.server_port) or 8080

        simple_server = HTTPServer((address_server, server_port), MyServer)
        print(f"Server started http://{address_server}:{server_port}")

        simple_server.serve_forever()
    except KeyboardInterrupt:
        simple_server.server_close()
        print("Server stopped.")

if __name__ == "__main__":        
    main()