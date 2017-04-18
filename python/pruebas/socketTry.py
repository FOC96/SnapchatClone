import socket
import sys

HOST = ''
PORT = 8888

# Creación del socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
print("Socket created")

try:
    s.bind((HOST,PORT))
except socket.error as msg:
    print("BIND FAILED! Error code", msg[0], "\nMessage: ", msg[1])
    sys.exit()
print("Socket bind complete")

s.listen(10)

#Function for handling connections. This will be used to create threads
def clientthread(conn):
    #Sending message to connected client
    conn.send('Welcome to the server. Type something and hit enter\n') #send only takes string

    #infinite loop so that function do not terminate and thread do not end.
    while True:

        #Receiving from client
        data = conn.recv(1024)
        reply = 'OK...' + data
        if not data:
            break

        conn.sendall(reply)

    #came out of loop
    conn.close()

#now keep talking with the client
while 1:
    #wait to accept a connection - blocking call
    conn, addr = s.accept()
    print('Connected with ' + addr[0] + ':' + str(addr[1]))

    #start new thread takes 1st argument as a function name to be run, second is the tuple of arguments to the function.
    start_new_thread(clientthread ,(conn,))

s.close()

