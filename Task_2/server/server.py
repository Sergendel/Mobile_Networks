import socket
import pickle
from Main_Mobile_Network import build_towers_and_connections, dfs

# set host and port
HOST = '0.0.0.0'  # Standard loopback interface address (localhost)
PORT = 5000       # Port to listen on (non-privileged ports are > 1023)

while True:
    # connection
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((HOST, PORT))
        s.listen()
        conn, addr = s.accept()
        with conn:
            print('\n server connected by', addr)
            while True:
                recv_data = conn.recv(1024)
                if not recv_data:
                    break
                data = pickle.loads(recv_data)
                print('     sever received data in list format: ', data)

                # build towers list and connections dictionary
                towers, connections = build_towers_and_connections(data)

                # initiate visited dictionary
                visited = {k: False for k in towers}

                # run dfs
                print('     performing deep first searh ...')
                num_users = dfs(connections, visited, data[1], data[2])   # 2 - main tower, 1- users around towers
                print('     visited = {}'.format(visited))
                print('     number of users around broken towers = {}'.format(num_users))



                # compose answer to client
                msg = pickle.dumps(num_users)
                # send answer to client
                print('     server sending anser to client ...')
                conn.sendall(msg)
