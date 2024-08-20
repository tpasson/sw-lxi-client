import socket
import sys

def main(multimeter_ip, port=5025):
    """
    Connects to a lab multimeter via TCP/IP, sends a command to measure DC voltage,
    and prints the measured voltage.

    Parameters:
    multimeter_ip (str): The IP address of the multimeter.
    port (int, optional): The TCP port number. Default is 5025.

    Usage:
    python3 read_meter.py <multimeter_ip>
    Example:
    python3 read_meter.py 192.168.10.100
    """

    # Create a TCP/IP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect the socket to the device's IP and port
        sock.connect((multimeter_ip, port))
        
        # Send the MEAS:VOLT:DC? command
        sock.sendall(b'MEAS:VOLT:DC?\n')
        
        # Receive the response from the device
        response = sock.recv(1024)
        print(f"Measured DC Voltage: {response.decode().strip()} V")

    except socket.timeout:
        print("Socket connection timed out.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the socket connection
        sock.close()

if __name__ == "__main__":
    # Check if the IP address was provided as a command line argument
    if len(sys.argv) != 2:
        print("Usage: python read_meter.py <multimeter_ip>")
        sys.exit(1)

    # Extract the IP address from the command line arguments
    multimeter_ip = sys.argv[1]

    # Run the main function with the provided IP address
    main(multimeter_ip)
