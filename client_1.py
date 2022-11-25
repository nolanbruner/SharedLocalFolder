
# Author : Ayesha S. Dina

import os
import socket
import time
import datetime
print("please enter username")
username = input()
if username == "Nolan":
    print("please enter password")
    password = input()
    if password == "Nolan":
        print("please type in CONNECT followed by ip address and port")
        userIPport = input()
        userIPport = userIPport.split( )
         #parse stuff variable -> ip address, port
         #assign ip address and port accordingly
         #IP = "192.168.1.101" #"localhost"
         #PORT = 4450
        if userIPport[0] == "CONNECT":
            IP = userIPport[1]
            PORT = int(userIPport[2])
            ADDR = (IP,PORT)

        SIZE = 1024 ## byte .. buffer size
        FORMAT = "utf-8"
        SERVER_DATA_PATH = "server_data"

        def main():

          client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
          client.connect(ADDR)
          while True:  ### multiple communications
                data = client.recv(SIZE).decode(FORMAT)
                cmd, msg = data.split("@")
                if cmd == "OK":
                    print(f"{msg}")
                elif cmd == "DISCONNECTED":
                    print(f"{msg}")
                    break

                data = input("> ")
                data = data.split(" ")
                cmd = data[0]

                if cmd == "TASK":
                    client.send(cmd.encode(FORMAT))

                elif cmd == "LOGOUT":
                    client.send(cmd.encode(FORMAT))
                    break
                elif cmd == "DIR":
                    files = os.listdir("server")
                    os.chdir("server")
                    for temp_file in files:
                        tempfilestats = os.stat(temp_file)
                        modified = os.path.getmtime(temp_file)
                        year,month,day,hour,minute,second=time.localtime(modified)[:-3]
                        dateModified = (f"  {month}/{day}/{year} {hour}:{minute}:{second}")
                        print(f"File Name: {temp_file}, Size: {tempfilestats.st_size} Bytes, Date modified: {dateModified}  \n")
                    client.send(cmd.encode(FORMAT))
                    os.chdir(r"C:\Users\Nolan\Desktop\S21\CS371\Project\Code")

                elif cmd == "CREATE":
                    print(f"{cmd}@{data[1]}")       ### two words are separated by @ character.
                    client.send(f"{cmd}@{data[1]}".encode(FORMAT))

                elif cmd == "DELETE":
                    directory = "server"
                    files = os.listdir("server")
                    os.chdir(directory)
                    if data[1] in files:
                        #if fileName == data[1]:
                        os.unlink(data[1])
                        client.send(cmd.encode(FORMAT))
                        os.chdir(r"C:\Users\Nolan\Desktop\S21\CS371\Project\Code")

                elif cmd == "UPLOAD":
                    #nd(f"{cmd}@{data[1]}".encode(FORMAT))
                    directory = "client"
                    files = os.listdir("client")
                    os.chdir(directory)
                    if data[1] in files:
                        f = open (data[1], "rb")
                        l = f.read(1024)
                    while (l):
                        client.send(l)
                        l = f.read(1024)
                        #if fileName == data[1]:
                    client.send(f"{cmd}@{data[1]}".encode(FORMAT))
                    os.chdir(r"C:\Users\Nolan\Desktop\S21\CS371\Project\Code")

        # QUESTION:
                    print("Disconnected from the server.")
                    client.close() ## close the connection

        if __name__ == "__main__":
            main()
