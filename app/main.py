# Uncomment this to pass the first stage
import socket
import re


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")

    # Uncomment this to pass the first stage
    #
    server_socket = socket.create_server(("localhost", 4221))#=, reuse_port=True)
    client_conn, client_addr = server_socket.accept()
    print(f"Connected by {client_addr}")
    data = client_conn.recv(1024).decode('utf-8')
    if re.search("GET /echo/", data):
        received_str = data.split("\r\n")[0].split("echo/")[1].split(" ")[0]
        content_lenght = len(received_str)
        client_conn.sendall(f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {content_lenght}\r\n\r\n{received_str}".encode())
    elif re.search("GET /user-agent", data):
        user_agent = data.split("User-Agent: ")[1].split("\r\n")[0]
        content_lenght = len(user_agent)
        client_conn.sendall(f"HTTP/1.1 200 OK\r\nContent-Type: text/plain\r\nContent-Length: {content_lenght}\r\n\r\n{user_agent}".encode())
    elif re.search("GET / ", data):
        client_conn.sendall(b"HTTP/1.1 200 OK\r\n\r\n")
    else:
        client_conn.sendall(b"HTTP/1.1 404 Not Found\r\n\r\n")

if __name__ == "__main__":
    main()
