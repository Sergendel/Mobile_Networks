import requests
from Main_Mobile_Network import read_input_file, check_input
import os
import json

# set url
#HOST = 'localhost'             # to run on lcal machine !!!
HOST = 'task_3_server_1'    # to run on docker !


PORT = 80       # The port used by the server
url = "http://" + HOST + ":"+str(PORT)


# list of input files
fun_path = os.path.dirname(os.path.abspath(__file__))
full_path=os.path.join(fun_path,"data")
file_list = [x for x in os.listdir(full_path) if x.endswith(".txt")]
print('\n found {} input files in directory {}'.format(len(file_list),full_path))


for filename in file_list:
    print('\n Processing file: {}'.format(filename))

    # read input file
    data = read_input_file(filename)
    print('     input data in list format: ', data)

    # check the data is OK
    check_input(data)

    # create msg to server
    my_json_msg = json.dumps(data)

    # print('     sending data to server ...')
    x = requests.post(url, json=my_json_msg)

    # ugly :(( pull the result from response string
    match1 = x.text.find('{', 0)
    match2 = x.text.find('}', 0)
    myjson = json.loads(x.text[match1:match2+1].replace("\\",''))
    num_users = myjson['num_users']
    print('     number of users around broken towers = {} \n'.format(num_users))

print('Task accomplished')
