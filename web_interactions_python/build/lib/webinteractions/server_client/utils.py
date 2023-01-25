"""Provides helper functions for other modules"""

def get_synchronous_response(request_data, client_address):
    """Function returns response data for requests in synchronous server"""
    print(request_data)
    print(f"Received data from {client_address}")

    if request_data == "ping":
        print("Ping sent back")
        response = bytes("ping received", "ascii")
    elif request_data == "get":
        print("Received a get request")
        response = bytes("html corresponding to a webpage", "ascii")
    elif request_data == "post":
        print("Received a post request")
        response = bytes("database was updated successfully", "ascii")

    return response


def get_threaded_response(request_data, thread_name, client_address):
    """Function return response data for requests in threaded server"""
    print(request_data)
    print(f"Received data from {client_address}")

    if request_data == "ping":
        print("Ping sent back")
        response = bytes(f"{thread_name}: ping received", "ascii")
    elif request_data == "get":
        print("Received a get request")
        response = bytes(f"{thread_name}: html corresponding to a webpage", "ascii")
    elif request_data == "post":
        print("Received a post request")
        response = bytes(f"{thread_name}: database was updated successfully", "ascii")

    return response
