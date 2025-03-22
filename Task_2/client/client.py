import socket
import pickle
import time
import os
from Main_Mobile_Network import read_input_file, check_input

# ser address
HOST = 'localhost'  # The server's hostname or IP address
PORT = 5000        # The port used by the server

# server_addr = HOST  # use to run on local machine

# to run on docker use docker
server_addr='task_2_server'

# create connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((server_addr,PORT)) # in order to run on local machine


# list of input files
fun_path = os.path.dirname(os.path.abspath(__file__))
full_path=os.path.join(fun_path,"data")
file_list = [x for x in os.listdir(full_path) if x.endswith(".txt")]
print('found {} input files in directory {}'.format(len(file_list),full_path))


for filename in file_list:
    print('\n Processing file: {}'.format(filename))

    # read input file
    data = read_input_file(filename)
    print('     input data in list format: ', data)


    # check the data is OK
    check_input(data)

    # create msg to server
    msg = pickle.dumps(data)

    # send msg to server
    print('     sending data to server ...')
    s.sendall(msg)

    # get answer form server
    serv_answr = s.recv(1024)
    num_users = pickle.loads(serv_answr)
    print('     number of users around broken towers = {} \n'.format(num_users))
#time.sleep(1)
print('Task accomplished')
