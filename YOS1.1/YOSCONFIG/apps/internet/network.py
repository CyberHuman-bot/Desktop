import socket

# Placeholder for basic internet functionality
def check_internet():
    try:
        socket.create_connection(("8.8.8.8", 53))
        return True
    except OSError:
        return False

if __name__ == '__main__':
    if check_internet():
        print("Internet is working.")
    else:
        print("No internet connection.")
        