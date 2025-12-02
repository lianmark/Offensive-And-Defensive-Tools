import socket
import select
import sys
print("Lian M C2C server Version 0.4")
recv_data = "<ADMIN_AUTH_KEY>"
recv_dataNONEADMIN = "NONEADMIN<ADMIN_AUTH_KEY>"
admin_connected = False
def start_server():
    global admin_connected
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("<SERVER_IP>", <SERVER_PORT>))

    s.listen(2)
    ...
    ...
    ...
    ...
    ...
    ...
    ...
#  IMPORTANT NOTICE – CODE REMOVED FOR SAFETY & LEGAL REASONS
#
#  The following section originally contained a fully functional
#  reverse-shell / remote-execution implementation.
#
#  I have intentionally deleted this part of the source code to
#  prevent misuse. Reverse shells are extremely dangerous, can be
#  weaponized easily, and are commonly used in illegal hacking
#  activities. I do not want to enable or facilitate any form of
#  unauthorized access, abuse, or criminal behavior.
#
#  Publishing a complete reverse shell publicly may expose me to
#  legal, ethical, and professional liability, and therefore this
#  portion is intentionally redacted.
#
#  The remaining code is provided strictly for educational,
#  research, and defensive cybersecurity purposes.
#
#  For legitimate, vetted, and lawful professional scenarios
#  (such as job interviews, security assessments, or controlled
#  training environments), I may provide the full version
#  privately upon request — but only after verifying intent and
#  ensuring proper authorization.
    ...
    ...
    ...
    ...
    ...
    ...
    ...
    ...
    ...
    print("Second user session pending — awaiting handshake.\n")
    c2, a2 = s.accept()
    print("CLIENT access granted to host " + a1[0] + ".\n")

    sockets = [c1, c2]
    print("┌─────────────────────────────────┐")
    print("│    SYSTEM NOTIFICATION          │")
    print("│  Topic: Season Protocol         │")
    print("│  Status: **Active & Ready**     │")
    print("│                                 │")
    print("│  All checks passed. The         │")
    print("│  established season is now      │")
    print("│  live and operational.          │")
    print("│  [OK] [DETAILS]                 │")
    print("└─────────────────────────────────┘")

    while True:
        readable, _, _ = select.select(sockets, [], [])
        for sock in readable:
            data = sock.recv(65536)
            if not data:
                continue

            if data.strip() == b"SDserver":
                print("Restart command received! Closing connections...")
                c1.close()
                c2.close()
                s.close()
                return

            if sock is c1:
                c2.send(data)
            else:
                c1.send(data)


while True:
    try:
        start_server()
        print("Restarting server...")
    except KeyboardInterrupt:
        print("\nServer stopped by user")
        sys.exit(0)
    except Exception as e:
        print("Error: " + str(e))
        print("Restarting in 5 seconds...")
        import time

        time.sleep(5)
