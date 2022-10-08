import socket
import time
import threading
from queue import Queue


def port_scanner(port_range):
    open_ports=[]
    socket.setdefaulttimeout(0.25)
    target = "localhost"
    if len(port_range) == "" : port_range = "1-65535"
    start_port, end_port = port_range.split("-")
    start_port, end_port = int(start_port), int(end_port)
    t_IP = socket.gethostbyname(target)

    def portscan(port):
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            con = s.connect((t_IP, port))
            open_ports.append(port)
            con.close()
        except:
            pass

    def threader():
        while True:
            worker = q.get()
            portscan(worker)
            q.task_done()
        
    q = Queue()
    startTime = time.time()
    
    for x in range(200):
        t = threading.Thread(target = threader)
        t.daemon = True
        t.start()
    
    for worker in range(start_port, end_port):
        q.put(worker)
    
    q.join()
    return open_ports