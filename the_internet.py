"""
File:    the_internet.py
Author:  Judson Asomani
Date:    12/8/2024
Section: 11
E-mail:  judsona1@umbc.edu
Description:
  traces the path to different servers and outputs the time
"""
server_dict = {}
running = True
current_server = []



def get_key_by_value(value, dictionary):
    for key, val in dictionary.items():
        if val == [value]:  # Check for equality
            return key
    return None


def call_input():
    while running:
        user_input = input('>>> ')
        return user_input


def break_user_input(user_input):
    if 'create-server' in user_input:
        _, server_name, ip_v4_address = user_input.split()  # Split input into parts
        create_server(server_name, ip_v4_address)
    if 'create-connection' in user_input:
        _, server_1, server_2, connect_time = user_input.split()
        create_connection(server_1, server_2, connect_time)
    if 'set-server' in user_input:
        _, set_value = user_input.split()
        # current_server.remove()
        current_server.append(set_server(set_value))
    if 'ip-config' in user_input:
        ip_config()
    if 'traceroute' in user_input:
        _, destination_server = user_input.split()
        traceroute(server_dict, current_server[0], destination_server)


def create_server(server_name, ip_v4_address):
    server_dict[server_name] = []
    server_dict[server_name].append(ip_v4_address)


def create_connection(server_1, server_2, connect_time):
    if server_1 and server_2 in server_dict:
        server_dict[server_1].append(server_2)
        server_dict[server_1].append(connect_time)
        server_dict[server_2].append(server_1)
        server_dict[server_2].append(connect_time)


def set_server(
        set_value):  # will set the current server with either the name (easy) or with the ipv4 address (hard, gotta use getKey)
    if set_value in server_dict:
        current_server.clear()
        selected_server = set_value
        return selected_server
    elif get_key_by_value(set_value, server_dict) in server_dict:
        current_server.clear()
        selected_server = get_key_by_value(set_value, server_dict)
        return selected_server


def ip_config():  # prints out the selected server at the current moment
    print(current_server[0], '    ', server_dict[current_server[0]][0])


def display_servers():  # shows each server, it's IP, and the connections to that selected server
    pass


def ping(search_value):  # will search for the listed server with either the name (easy) or
    # with the ipv4 address (hard, gotta use getKey) and display the time it took to reach that server
    pass


"""
def traceroute(search_value): #will search for the listed server with either the name (easy) or
                              #with the ipv4 address (hard, gotta use getKey) and display the individual servers used as a path
                              #and show to time for each individual server it went through
    pass
"""


def traceroute(server_dict, starting_place, destination):
    visited = {}
    for place in server_dict:
        visited[place] = False

    return traceroute_rec(server_dict, starting_place, destination, visited)


def traceroute_rec(server_dict, starting_place, destination, visited):
    path = []  # set the path to empty at first, this will contain the path from the current place that we start to the end.

    if starting_place == destination:  # if we've reached the end, then begin constructing the path from the back.
        return [destination]
    # setting the visited to true so we don't loop back.
    visited[starting_place] = True

    for index in range(1, len(server_dict[starting_place]), 2):
        next_place = server_dict[starting_place][index]

        if not visited[next_place]:
            path = traceroute_rec(server_dict, next_place, destination, visited)
            if path:
                display_time = 0
                print('tracing route to ', destination, ' ', server_dict[destination][0])
                print('path was ', [starting_place] + path)
                for times in range(2, len(server_dict[starting_place]), 2):
                    display_time += server_dict[next_place][times]
                    new_display_time = display_time

    visited[starting_place] = False
    # essentially this will return if no path is found, i.e. we still have  path = []
    print('Unable to route to target system name ', destination)


def run_the_internet():
    while running:
        user_input = call_input()
        if user_input != 'quit':
            break_user_input(user_input)
            print('test output to see full dict')
            print(server_dict)
            print(current_server)
        if user_input == 'quit':
            return 'end of project :)'


if __name__ == '__main__':
    run_the_internet()
