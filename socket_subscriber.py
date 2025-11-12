import os, socket, time, sys

HOST = os.getenv("HOST", "127.0.0.1")  # set to server LAN IP, e.g. 192.168.1.50
PORT = int(os.getenv("PORT", "5000"))

def connect_with_retries():
    while True:
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((HOST, PORT))
            return s
        except Exception as e:
            print(f"connect failed: {e}; retrying in 1s", flush=True)
            time.sleep(1)

def main():
    while True:
        s = connect_with_retries()
        f = s.makefile("r")
        try:
            for line in f:
                print(line.rstrip(), flush=True)
        except Exception as e:
            print(f"read error: {e}", flush=True)
        finally:
            try: f.close()
            except: pass
            try: s.close()
            except: pass
            time.sleep(1)  # backoff before reconnect

if __name__ == "__main__":
    main()
