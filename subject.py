# This class defines the Subject that reports to the Observer
import socket
import sys

class Subject:
    def __init__(self, id_number, x_grid, y_grid):
        self.id_number = id_number
        self.x_grid = x_grid
        self.y_grid = y_grid
        self.status = 'ONLINE'
        self.send_message("Device is now online")

    def send_message(self, message):
        # Set the Observer's IP address and port number
        host = '127.0.0.1'  # same computer
        port = 65432  # server port
        print("Connecting to Observer...")

        # Create a TCP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Connect to the Observer
            s.connect((host, port))

            # Notify that the message is being sent
            print("Sending message...")

            # Create message in format: ID,X,Y,message
            full_message = f"{self.id_number},{self.x_grid},{self.y_grid},{message}"
            # Send the message to the Observer
            s.sendall(full_message.encode())

            # Receive response from Observer (up to 1024 bytes)
            data = s.recv(1024)

            # Print the response from the Observer
            print("Received from observer:", data.decode())

def main():
    if len(sys.argv) != 4:
        print("Usage: subject.py [SUB_ID] [X_CORD] [Y_CORD]")
        exit(1)
    subject_id = sys.argv[1]
    x_grid = sys.argv[2]
    y_grid = sys.argv[3]

    Subject(subject_id, x_grid, y_grid)

if __name__ == "__main__":
    main()