# This class defines the Observer of the IoT instances
import  socket
import  datetime

class Observer:
    def __init__(self, id_number):
        self.ip_address = '127.0.0.1'
        self.port_number = 65432

        self.id_number = id_number

        self.logs = []
        self.listen()

    def listen(self):
        # Print message to show server is ready
        print("Comm Centre waiting for messages...")

        # Create a TCP socket
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            # Bind socket to IP address and port
            s.bind((self.ip_address, self.port_number))
            # Start listening for incoming connections
            s.listen()

            # Keep server running to accept multiple connections
            while True:
                # Accept a connection from a client
                conn, addr = s.accept()
                # Handle the connection
                with conn:
                    # Receive data (up to 1024 bytes)
                    data = conn.recv(1024)
                    if data:
                        # Decode bytes into a string message
                        message = data.decode()
                        # Process the received message
                        self.process_message(message)
                        # Send confirmation back to client
                        conn.sendall(b"Received")

    def process_message(self, message):
        self.logs.append(str(datetime.datetime.now()) + "," + message)
        self.print_logs()

    def print_logs(self):
        print("======== LOGS ========")
        for log in self.logs:
            print(log)
        print()

def main():
    Observer('OBS0001')

if __name__ == "__main__":
    main()