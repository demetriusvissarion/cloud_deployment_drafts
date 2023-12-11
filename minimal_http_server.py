# Noe: this is a minimal example for educational purposes, and it does not adhere to best practices for building a production-ready HTTP server. It's important to use established libraries or frameworks in real-world scenarios for reliability, security, and maintainability.

# import os
import re
import threading
import subprocess

def handle_request(request):
    # Extract the path from the request
    match = re.match(r'GET /([^ ]+)', request)
    if match:
        path = match.group(1)
    else:
        path = "index.html"

    # Generate a simple response
    response_body = f"Hello, you requested: {path}"

    # Send the HTTP response
    response = (
        "HTTP/1.1 200 OK\r\n"
        "Content-Type: text/plain\r\n"
        f"Content-Length: {len(response_body)}\r\n"
        "\r\n"  # Empty line to separate headers from the body
        f"{response_body}"
    )

    return response.encode('utf-8')

def handle_client(client_socket):
    # Receive data from the client (browser)
    request_data = client_socket.recv(1024)
    if not request_data:
        return

    # Convert bytes to string and handle the request
    request = request_data.decode('utf-8')
    response = handle_request(request)

    # Send the response back to the client
    client_socket.sendall(response)
    client_socket.close()

def start_server():
    server_socket = subprocess.Popen(
        ["nc", "-l", "-p", "8080", "-c", "cat"],
        stdin=subprocess.PIPE,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
        text=True,
        bufsize=1,
    )
    
    print("Server listening on http://localhost:8080")

    while True:
        # Accept connections in a loop
        client_socket, _ = server_socket.communicate()
        print("Accepted connection")

        # Handle each request in a separate thread
        client_handler = threading.Thread(target=handle_client, args=(client_socket,))
        client_handler.start()

if __name__ == "__main__":
    start_server()
