import sys
import socket

if len(sys.argv) != 2:
    print("Usage: python3 check_port.py <port>")
    sys.exit(1)

port = sys.argv[1]

server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(f"Tentative de connection dans le port {port} :")

try:
    server_socket.bind(("127.0.0.1", int(port)))

    server_socket.listen()

    print("Accès autorisé | Le port est libre")

except ValueError:
    print("Accès refusé | Entrez un nombre entier (ex : 5000)")


except PermissionError:

    print("Accès refusé | Vous n'avez pas les doits pour y accéder")
    

except OSError:

    print("Accès refusé | Le port est déjà occupé)")
   
finally:
    server_socket.close()








