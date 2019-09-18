import socket

"""
Simple Port Scanner Using Socket Module
"""

target = input("Enter a IP address to scan: ")
port_range = input("Enter the port range to scan ex (1-200): ")

try:
    starting_port_value = int(port_range.split('-')[0])
    ending_port_value = int(port_range.split('-')[1])
except IndexError:
    print("Please Enter A Starting Value And A Ending Value Separated With '-' , Example: 1-200")
else:

    print('Scanning Port ', target, 'from port', starting_port_value, 'to port', ending_port_value)

    for port in range(starting_port_value, ending_port_value):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        status = s.connect_ex((target, port))
        if status == 0:
            print('PORT NUMBER - ', port, ' - OPEN')
        else:
            print('PORT NUMBER - ', port, ' - CLOSED')
        s.close()
