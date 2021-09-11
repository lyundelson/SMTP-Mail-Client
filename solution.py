from socket import *


def smtp_client(port=1025, mailserver='127.0.0.1'):
    msg = "\r\n My message"
    endmsg = "\r\n.\r\n"

    # Choose a mail server (e.g. Google mail server) if you want to verify the script beyond GradeScope

    # Create socket called clientSocket and establish a TCP connection with mailserver and port

    # Fill in start
    clientSocket = socket(AF_INET, SOCK_STREAM)
    clientSocket.connect((mailserver, port))
    # Fill in end

    recv = clientSocket.recv(1024).decode()
    #print(recv)
    #if recv[:3] != '220':
        #print('220 reply not received from server.')

    # Send HELO command and print server response.
    heloCommand = 'HELO Alice\r\n'
    clientSocket.send(heloCommand.encode())
    recv1 = clientSocket.recv(1024).decode()
    #print(recv1)
    #if recv1[:3] != '250':
        #print('250 reply not received from server.')

    # Send MAIL FROM command and print server response.
    # Fill in start
    mailFrom = 'MAIL FROM: <ly2177@nyu.edu>\r\n'
    clientSocket.send(mailFrom.encode())
    recv2 = clientSocket.recv(1024).decode()
    #print(recv2)
    #if recv2[:3] != '250':
        #print('250 reply not received from server')

    # Fill in end

    # Send RCPT TO command and print server response.
    # Fill in start
    RCPT = 'RCPT TO: <lyundelson@gmail.com>\r\n'
    clientSocket.send(RCPT.encode())
    recv3 = clientSocket.recv(1024).decode()
    #print(recv3)
    #if recv3[:3] != '250':
        #print('250 reply not received from server')
    # Fill in end

    # Send DATA command and print server response.
    # Fill in start
    DATA = 'DATA\r\n'
    clientSocket.send(DATA.encode())
    recv4 = clientSocket.recv(1024).decode()
    #print(recv4)
    #if recv4[:3] != '354':
        #print('354 reply not recieved') 
    # Fill in end

    # Send message data.
    # Fill in start

    clientSocket.send(msg.encode())

    # Fill in end

    # Message ends with a single period.
    # Fill in start

    clientSocket.send(endmsg.encode())

    # Fill in end

    # Send QUIT command and get server response.
    # Fill in start
    QUIT = 'QUIT\r\n'
    clientSocket.send(QUIT.encode())
    recv7 = clientSocket.recv(1024).decode()
    #print(recv7)
    #if recv7[:3] != '250':
        #print('250 reply not received from server')
    # Fill in end
    clientSocket.close()


if __name__ == '__main__':
    smtp_client(1025, '127.0.0.1')
