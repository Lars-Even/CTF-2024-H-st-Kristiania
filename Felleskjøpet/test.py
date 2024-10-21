import socket

# Define the host and port to listen on
HOST = '0.0.0.0'  # Listen on all interfaces
PORT = 41111

# Create a TCP/IP socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_socket.bind((HOST, PORT))
server_socket.listen(1)

print(f"Server started! Listening on {HOST}:{PORT}...")


# Store session per client
class StoreSession:
    def __init__(self):
        self.penger = 250
        self.caps = 0
        self.gjødsel = 0
        self.motorsag = 0
        self.frontklipper = 0
        self.traktor = 0
        self.flag = False


caps_pris = 10
gjødsel_pris = 100
motorsag_pris = 1000
frontklipper_pris = 10000
traktor_pris = 100000
flag_pris = 1000000


# Helper functions to handle communication over the socket
def send_message(conn, message):
    conn.sendall(message.encode())


def receive_message(conn):
    try:
        data = conn.recv(1024)
        if not data:
            raise ConnectionResetError("Client disconnected")
        return data.decode().strip()
    except ConnectionResetError:
        print("Connection lost")
        return ""


# Main store logic with socket interaction
def start(conn, session):
    send_message(conn, f"Hva skjer, kompis? Hva vil du gjøre?\nDu har {session.penger} gelter!\n")

    while True:
        send_message(conn, """
    1. Se inventory.
    2. Handle hos felleskjøpet
    3. Avslutte
    > """)

        try:
            bruker_svar = int(receive_message(conn))
        except ValueError:
            send_message(conn, "Whoooow! Du må kan kun bruke tall!\n")
            continue

        if bruker_svar < 1 or bruker_svar > 3:
            send_message(conn, "--------------------------------\n\nDu har ikke så mange valg!!! :(\n")
            continue

        if bruker_svar == 1:
            show_inventory(conn, session)
        elif bruker_svar == 2:
            felleskjopet(conn, session)
        elif bruker_svar == 3:
            send_message(conn, "Avslutter programmet... Ha det bra, takk for at du handlet hos oss!\n")
            break


def show_inventory(conn, session):
    inventory_message = "Her ser du alle tingene dine! Whoooaaw\n--------------------------------------\n"

    if session.caps == 0 and session.gjødsel == 0 and session.motorsag == 0 and session.frontklipper == 0 and session.traktor == 0:
        inventory_message += "oi, du var fattig! :-("
    if session.caps != 0:
        inventory_message += f"{session.caps} x Caps: Er du en ekte råner med så mange caps?\n"
    if session.gjødsel != 0:
        inventory_message += f"{session.gjødsel} x Gjødsel: Hva skal du med så mye gjødsel? Går det bra?\n"
    if session.motorsag != 0:
        inventory_message += f"{session.motorsag} x Motorsag: Kanskje du finner flagget inne i trærne rundt bygget!!\n"
    if session.frontklipper != 0:
        inventory_message += f"{session.frontklipper} x Frontklipere: Sjekk hvem som skal klippe plenen!\n"
    if session.traktor != 0:
        inventory_message += f"{session.traktor} x Traktor: 100% sikker på at du liker John Deere!\n"
    if session.flag:
        inventory_message += "flag{c0f517c72b78e9404c29bbdde053df82}\n"

    send_message(conn, inventory_message)


def felleskjopet(conn, session):
    while True:
        send_message(conn, f"--- DU HAR {session.penger} KRONER ---\nHva vil du kjøpe?\n")
        send_message(conn, """
    1. Caps
    2. Gjødsel
    3. Motorsag
    4. Frontklipper
    5. Traktor
    6. Flag
    7. Tilbake til menyen
    > """)

        try:
            bruker_svar = int(receive_message(conn))
        except ValueError:
            send_message(conn, "Whoooow! Du må kan kun bruke tall!\n")
            continue

        if bruker_svar == 1:
            handle_purchase(conn, session, "Caps", caps_pris, "caps")
        elif bruker_svar == 2:
            handle_purchase(conn, session, "Gjødsel", gjødsel_pris, "gjødsel")
        elif bruker_svar == 3:
            handle_purchase(conn, session, "Motorsag", motorsag_pris, "motorsag")
        elif bruker_svar == 4:
            handle_purchase(conn, session, "Frontklipper", frontklipper_pris, "frontklipper")
        elif bruker_svar == 5:
            handle_purchase(conn, session, "Traktor", traktor_pris, "traktor")
        elif bruker_svar == 6:
            handle_purchase(conn, session, "Flag", flag_pris, "flag")
        elif bruker_svar == 7:
            break


def handle_purchase(conn, session, item_name, item_price, item_var):
    if session.penger < item_price:
        send_message(conn,
                     f"Du har ikke nok penger til å kjøpe {item_name.lower()}.\n!-- DU HAR {session.penger} KRONER --!\n")
        return

    while True:
        try:
            send_message(conn, f"{item_name} koster {item_price} kroner. Hvor mange ønsker du å kjøpe?\n    > ")
            item_input = receive_message(conn)
            if not item_input:
                raise ValueError("Du må skrive inn et tall.")
            item_count = int(item_input)

            if session.penger < (item_price * item_count):
                send_message(conn,
                             f"Du har ikke nok penger til å kjøpe {item_count} {item_name.lower()} til {item_price * item_count} kroner!\n")
                return
            else:
                # Deduct money and add the purchased items to inventory
                session.penger -= (item_count * item_price)
                send_message(conn,
                             f"Gratulerer! Du har kjøpt {item_count} {item_name.lower()} for {item_count * item_price} kroner!\n")

                # Add the purchased item to the inventory
                if item_var == "caps":
                    session.caps += item_count
                elif item_var == "gjødsel":
                    session.gjødsel += item_count
                elif item_var == "motorsag":
                    session.motorsag += item_count
                elif item_var == "frontklipper":
                    session.frontklipper += item_count
                elif item_var == "traktor":
                    session.traktor += item_count
                elif item_var == "flag":
                    session.flag = True  # Set the flag to True
                    send_message(conn, "Gratulerer! Du har kjøpt flagget!\n")

                break
        except ValueError:
            send_message(conn, "Kun tall! Prøv på nytt?\n")


# Start the server and handle incoming connections
while True:
    conn, addr = server_socket.accept()
    print(f"Connected by {addr}")
    conn.settimeout(60)  # Optional: Set a timeout of 60 seconds for each connection
    session = StoreSession()  # Each client gets its own session
    start(conn, session)
    conn.close()
