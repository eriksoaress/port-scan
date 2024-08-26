import tkinter as tk
from tkinter import messagebox
import socket
from PIL import Image, ImageTk
from concurrent.futures import ThreadPoolExecutor, as_completed

def scan_port(host, port):
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(0.5)
        result = sock.connect_ex((host, port))
        if result == 0:
            return port, True
        else:
            return port, False
    except Exception as e:
        return port, False
    finally:
        sock.close()

def well_known_ports():
    return {
        20: "FTP",
        21: "FTP",
        22: "SSH",
        23: "Telnet",
        25: "SMTP",
        53: "DNS",
        80: "HTTP",
        110: "POP3",
        113: "NTP",
        135: "MSRPC",
        143: "IMAP",
        443: "HTTPS",
        445: "SMB",
        631: "IPP",
        993: "IMAPS",
        995: "POP3S",
        3306: "MySQL",
        3389: "RDP",
        5900: "VNC"
    }

def scan_range(host, port_range):
    open_ports = []
    with ThreadPoolExecutor(max_workers=100) as executor:  # Escaneia até 100 portas simultaneamente
        futures = {executor.submit(scan_port, host, port): port for port in range(port_range[0], port_range[1] + 1)}
        for future in as_completed(futures):
            port, is_open = future.result()
            if is_open:
                service = well_known_ports().get(port, "Unknown Service")
                open_ports.append((port, service))
    return open_ports

def start_scan():
    host = entry_host.get()
    try:
        port_range_initial = int(entry_port_initial.get())
        port_range_final = int(entry_port_final.get())
        port_range = (port_range_initial, port_range_final)
        
        scanning_label.config(text="Escaneando...")
        scanning_label.update_idletasks()  
        
        open_ports = scan_range(host, port_range)
        result = "\n".join([f"Porta {port}: {service}" for port, service in open_ports])
        
        scanning_label.config(text="")
        if result == "":
            result = "Nenhuma porta aberta foi encontrada."
        messagebox.showinfo("Resultado", result)
    except Exception as e:
        scanning_label.config(text="")
        messagebox.showerror("Erro", str(e))

root = tk.Tk()
root.title("Port Scanner")
root.geometry("1200x800")

bg_image = Image.open("mp10.webp")
bg_image = bg_image.resize((1200, 800)) 
bg_photo = ImageTk.PhotoImage(bg_image)

background_label = tk.Label(root, image=bg_photo)
background_label.place(relwidth=1, relheight=1)

font_label = ('Arial', 16)  
font_button = ('Arial', 16) 

tk.Label(root, text="Host:", font=font_label).pack(pady=10)
entry_host = tk.Entry(root, font=font_label)
entry_host.pack(pady=10)

tk.Label(root, text="Início do Range:", font=font_label).pack(pady=10)
entry_port_initial = tk.Entry(root, font=font_label)
entry_port_initial.pack(pady=10)

tk.Label(root, text="Final do Range:", font=font_label).pack(pady=10)
entry_port_final = tk.Entry(root, font=font_label)
entry_port_final.pack(pady=10)

tk.Button(root, text="Iniciar Escaneamento", command=start_scan, font=font_button).pack(pady=20)

scanning_label = tk.Label(root, text="", fg="black", font=font_label) 
scanning_label.pack(pady=10)

root.mainloop()
