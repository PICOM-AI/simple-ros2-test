import os, socket, json, time, random, string, threading

HOST = "0.0.0.0"
PORT = int(os.getenv("PORT", "5000"))
INTERVAL = float(os.getenv("INTERVAL", "1.0"))
COUNT_START = int(os.getenv("COUNT_START", "1"))

clients = []
lock = threading.Lock()

def accept_loop(server_sock):
    while True:
        conn, addr = server_sock.accept()
        conn.setblocking(True)
        with lock:
            clients.append(conn)

def rand_str(n=8):
    return "".join(random.choices(string.ascii_letters + string.digits, k=n))

def main():
    srv = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    srv.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    srv.bind((HOST, PORT))
    srv.listen(8)

    threading.Thread(target=accept_loop, args=(srv,), daemon=True).start()

    count = COUNT_START
    while True:
        payload = {
            "count": count,
            "rand": rand_str(),
            "ts": time.time(),
        }
        line = json.dumps(payload) + "\n"

        with lock:
            dead = []
            for c in clients:
                try:
                    c.sendall(line.encode("utf-8"))
                except Exception:
                    dead.append(c)
            for d in dead:
                try: d.close()
                except Exception: pass
                clients.remove(d)

        count += 1
        time.sleep(INTERVAL)

if __name__ == "__main__":
    main()
