import socket 
import threading

open_ports = []

def scan_port(target, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        result = sock.connect_ex(target,port)
        if result == 0:
            print(f"{port} portu açık.")
            open_ports.append(port)
        sock.close()
    except Exception as e:
        pass


def main():
    target_ip = input("Lütfen hedef İP adresini giriniz: ")
    start_port = 1
    end_port = 65535
    
    print(f"{target_ip} üzerindeki {start_port} ile {end_port} arasındaki portlar taranıyor.")

    threads = []
    for port in range(start_port, end_port +1):
        thread = threading.Thread(target=scan_port,args=(target_ip,port))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    if open_ports:
        print(f"\n açık portlar {sorted(open_ports)}")
    else:
        print("\n Açık port bulunamadı.")

if __name__ == "__main__":
    main()
