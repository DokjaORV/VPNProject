import tkinter as tk
from tkinter import filedialog, messagebox
import socket
import threading
import os
import heapq

# --- GRAFO DE LATENCIAS ---
graph = {
    'Alan': {'Andres': 9, 'Marlene': 50, 'Giovanni': 50},
    'Andres': {'Alan': 9, 'Giovanni': 10, 'Marlene': 25},
    'Marlene': {'Alan': 50, 'Andres': 25, 'Giovanni': 100},
    'Giovanni': {'Alan': 50, 'Andres': 10, 'Marlene': 100},
}

# --- IPs DE CADA NODO ---
ip_map = {
    'Alan': '100.113.73.88',
    'Andres': '100.124.230.9',
    'Marlene': '100.113.141.37',
    'Giovanni': '100.93.134.60',
}

# --- DIJKSTRA ---
def dijkstra(start, end):
    queue = [(0, start, [])]
    visited = set()
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node in visited:
            continue
        visited.add(node)
        path = path + [node]
        if node == end:
            return path, cost
        for adj, weight in graph.get(node, {}).items():
            if adj not in visited:
                heapq.heappush(queue, (cost + weight, adj, path))
    return None, float('inf')

# --- ENVÍO DE ARCHIVOS ---
def send_file(path, dest_ip, destino_final, port=5001):
    try:
        with socket.socket() as s:
            s.connect((dest_ip, port))
            filename = os.path.basename(path).encode()
            filename = filename[:255].ljust(256, b'\x00')
            s.send(filename)

            destino_final = destino_final.encode()
            destino_final = destino_final[:255].ljust(256, b'\x00')
            s.send(destino_final)

            with open(path, 'rb') as f:
                while True:
                    data = f.read(4096)
                    if not data:
                        break
                    s.sendall(data)
        return True
    except Exception as e:
        print("Error enviando archivo:", e)
        return False

# --- RECEPCIÓN Y POSIBLE REENVÍO ---
def start_receiver(port=5001, soy_nodo=None):
    def receiver():
        with socket.socket() as s:
            s.bind(('', port))
            s.listen(1)
            while True:
                conn, addr = s.accept()
                with conn:
                    filename = conn.recv(256).rstrip(b'\x00').decode()
                    destino_final = conn.recv(256).rstrip(b'\x00').decode()
                    full_filename = 'recv_' + filename
                    with open(full_filename, 'wb') as f:
                        while True:
                            data = conn.recv(4096)
                            if not data:
                                break
                            f.write(data)
                    print(f"Archivo recibido: {filename} de {addr}")

                    if soy_nodo and destino_final and soy_nodo != destino_final:
                        path, _ = dijkstra(soy_nodo, destino_final)
                        if soy_nodo in path:
                            idx = path.index(soy_nodo)
                            if idx + 1 < len(path):
                                siguiente_nodo = path[idx + 1]
                                siguiente_ip = ip_map[siguiente_nodo]
                                print(f"Reenviando a {siguiente_nodo} en ruta: {path}")
                                send_file(full_filename, siguiente_ip, destino_final)
    threading.Thread(target=receiver, daemon=True).start()

# --- INTERFAZ GRÁFICA ---
class FileTransferApp:
    def __init__(self, root):
        self.root = root
        root.title("Envío de Archivos entre Nodos")

        self.role = tk.StringVar(value="Emisor")
        self.me = tk.StringVar(value="Selecciona")
        self.target = tk.StringVar()
        self.use_dijkstra = tk.BooleanVar()
        self.file_path = ""

        tk.Label(root, text="Soy:").pack()
        tk.OptionMenu(root, self.me, *graph.keys()).pack()

        tk.Label(root, text="Rol:").pack()
        tk.OptionMenu(root, self.role, "Emisor", "Receptor", "Nodo intermedio").pack()

        tk.Label(root, text="Destino:").pack()
        tk.OptionMenu(root, self.target, *graph.keys()).pack()

        tk.Checkbutton(root, text="Usar ruta más rápida (Dijkstra)", variable=self.use_dijkstra).pack()

        tk.Button(root, text="Elegir archivo", command=self.select_file).pack()
        tk.Button(root, text="Iniciar", command=self.start).pack()

        self.status = tk.Label(root, text="Estado: Esperando", fg="blue")
        self.status.pack()

    def select_file(self):
        self.file_path = filedialog.askopenfilename()
        if self.file_path:
            self.status.config(text=f"Archivo seleccionado: {os.path.basename(self.file_path)}")

    def start(self):
        if self.role.get() == "Receptor":
            start_receiver()
            self.status.config(text="Receptor activo esperando archivos...", fg="green")
        elif self.role.get() == "Emisor":
            if not self.file_path:
                messagebox.showerror("Error", "Selecciona un archivo")
                return
            start = self.me.get()
            end = self.target.get()
            if self.use_dijkstra.get():
                path, total = dijkstra(start, end)
                self.status.config(text=f"Ruta: {' -> '.join(path)} | Latencia: {total}")
            else:
                path = [start, end]
            dest_ip = ip_map[path[1]] if len(path) > 1 else ip_map[end]
            ok = send_file(self.file_path, dest_ip, end)
            if ok:
                self.status.config(text=f"Archivo enviado hacia {end} vía {path[1]}", fg="green")
            else:
                self.status.config(text=f"Error al enviar archivo", fg="red")
        elif self.role.get() == "Nodo intermedio":
            start_receiver(soy_nodo=self.me.get())
            self.status.config(text="Nodo intermedio listo para recibir y reenviar...", fg="orange")

# --- EJECUCIÓN ---
if __name__ == '__main__':
    root = tk.Tk()
    app = FileTransferApp(root)
    root.mainloop()