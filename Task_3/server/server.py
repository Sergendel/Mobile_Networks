from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse
import json
from Main_Mobile_Network import build_towers_and_connections, dfs


class RequestHandler(BaseHTTPRequestHandler):

    def _set_headers(self):
        self.send_response(200)
        self.send_header('Content-type', 'application/json')
        self.end_headers()

    def do_GET(self):
        parsed_path = urlparse(self.path)
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'MGT!')
        return

    def do_POST(self):
        self._set_headers()
        # get dsta
        data_string = self.rfile.read(int(self.headers['Content-Length']))

        # parse data list from json
        data_string = json.loads(data_string)
        data = json.loads(data_string)

        # build towers list and connections dictionary
        towers, connections = build_towers_and_connections(data)

        # initiate visited dictionary
        visited = {k: False for k in towers}

        # run dfs
        print('     performing deep first searh ...')
        num_users = dfs(connections, visited, data[1], data[2])  # 2 - main tower, 1- users around towers
        print('     visited = {}'.format(visited))
        print('     number of users around broken towers = {}'.format(num_users))

        # create message
        message = json.dumps({'num_users':num_users})

        # send response to client
        self.wfile.write(json.dumps(message).encode('utf8'))  # works
        self.end_headers()
        return


if __name__ == '__main__':
    HOST = '0.0.0.0'  # The server's hostname or IP address
    PORT = 80  # The port used by the server
    server_address = (HOST, PORT)
    server = HTTPServer(server_address, RequestHandler)
    url = "http://" + HOST + ":" + str(PORT)
    print('Starting server at ' + url)
    server.serve_forever()