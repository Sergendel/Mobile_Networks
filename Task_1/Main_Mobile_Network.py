import json
import os


def read_input_file(file_name):
    """
    This function gt the name of input text file, read it and returns the list with input objects.
    If file can not be read from some reason, the script execution is stopped
    :param file_name: input text file
    :return: List of input entries
    """
    # reference path
    fun_path = os.path.dirname(os.path.abspath(__file__))

    file = os.path.join(fun_path,'data', file_name)
    try:
        with open(file, 'r') as f:
            s = f.read()
            s = s.replace('\'', '\"')
            s = s.replace('\n', '')
            s = s.replace('{', '[', 1)
            s = s[::-1].replace("}", "]", 1)[::-1]
            list_data = json.loads(s)
            return list_data
    except:
        print('Wrong input')
        exit()


def check_input(inp):
    """
    This function verifies that input file is correct:
          1. The number of entries
          2. All entries are from the correct type
          3. All entries are not empty
          4. The tower connections list fits to the dictionary of user around towers
          5. The main tower name fits to tower connections list
          6. The broken tower name  fits to tower connections list
    :param inp: list of input entries
    :return: No output,
             the script execution stops if input is wrong
    """
    # check input is correct:
    if len(inp) != 4:
        print(' Input file should contain 4 objects:\n'
              '     1. Network connections (list of lists). \n'
              '     2. Population size around towers (dictionary) \n'
              '     3. Main tower (list) \n'
              '     4. Broken  towers (list)')
        exit()

    # check  input objects
    if not isinstance(inp[0], list) or inp[0] == []:
        print('First input entry should be non-empty list of connections')
        exit()

    if not isinstance(inp[1], dict) or inp[1] == {}:
        print('Second input entry should be non-empty  dictionary of user numbers near towers')
        exit()

    if not isinstance(inp[2], str) or not inp[2]:
        print('Third input entry should be non-empty  string with name of main tower')
        exit()

    if not isinstance(inp[3], list) or inp[3] == []:
        print('Forth input entry should be non-empty list of broken towers')
        exit()

    # compare that connections list and users dictionary are in agreement
    towers = set([item for sublist in inp[0] for item in sublist])
    connection_keys = set(inp[1].keys())
    if towers != connection_keys:
        print('Towers connections list and users around towers '
              'dictionary are not in agreement. Recheck your input file.')
        exit()

    # check if main tower name is OK
    if not inp[2] in towers:
        print('Name of the  main tower is incorrect')
        exit()

    # check if broken towers are OK:
    for i_t in inp[3]:
        if i_t not in towers:
            print('list of broken towers names is wrong')
            exit()


# build connections dict
def build_towers_and_connections(data_list):
    """
        1. Constructs the list of unique tower names.
        2. Constructs the dictionary of towers connections:
               keys = names of towers (one key for each tower).
               values = list of tower connection
            for example { 'A':['B','C'],'B':['A'],'C':'A'}
            means  that A is connected to B and C , B is connected to A, C is connected to A
            This dictionary is build in order to simplify dfs search
    :param data_list: list of input entries
    :return: 1. all_towers:         list of unique tower names
             2. connections_dict:   dictionary of towers connections
    """
    # get list of all tower names (unique) by flattening the connections list of lists
    all_towers = list(set([item for sublist in data_list[0] for item in sublist]))

    # initiate connections dict
    connections_dict = {k: [] for k in all_towers}

    for l in data_list[0]:
        if l[0] not in data_list[3] and l[1] not in data_list[3]: # 3 - broken towers
            connections_dict[l[0]].append(l[1])
            connections_dict[l[1]].append(l[0])
    # remove duplications if exist
    for i_k in connections_dict.keys():
        connections_dict[i_k] = list(set(connections_dict[i_k]))

    return all_towers, connections_dict


def dfs(connections, visited,users, start):
    """
    Performs Depth-First Search (DFS). Recursive function and calculate number of users near broken towers
    :param connections:   dictionary of connections of each tower. for example { 'A':['B','C'],'B':['A'],'C':'A'}
           means  that A is connected to B and C , B is connected to A, C is connected to A
    :param visited: Dictionary of all visited towers. For example {'A': True, 'B': False, 'C':False} means
           that tower A was visited druing DFS while B and C were not visited yet.
    :param start: string. name of the main tower
    :return: number of users around broken towers
    """
    # start dfs
    visited[start] = True
    for k in connections.get(start, []):
        if not visited[k]:
            dfs(connections, visited, users, k)

    # calculate  number of users around broken towers
    num_users = 0
    for i_k in visited.keys():
        if not visited[i_k]:
            num_users += users[i_k]  # 1 - tower users

    return num_users


if __name__== '__main__':

    # find all input files in "data" folder
    fun_path = os.path.dirname(os.path.abspath(__file__))
    full_path = os.path.join(fun_path, "data")
    file_list = [x for x in os.listdir(full_path) if x.endswith(".txt")]
    print('\n found {} input files in directory {}'.format(len(file_list), full_path))

    # execute for all input files:
    for filename in file_list:
        print('\n Processing file: {}'.format(filename))
        # read input file
        data = read_input_file(filename)

        # check if the data is OK
        check_input(data)

        print('     input data in list format: ', data )

        # build towers list and connections dictionary
        towers, connections = build_towers_and_connections(data)

        # initiate visited dictionary
        visited = {k: False for k in towers}

        # run dfs
        num_users = dfs(connections, visited, data[1], data[2])  # 2 - main tower, 1- users around towers
        print('     visited = {}'.format(visited))

        # output
        print('     number of users around broken towers = {} \n'.format(num_users))
