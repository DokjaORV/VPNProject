import subprocess

def medir_ancho_de_banda(ip_servidor, duracion=10):
    try:
        print(f"Iniciando prueba de ancho de banda hacia {ip_servidor} por {duracion} segundos...\n")
        
        # Ejecutar iperf3 con la ruta específica
        resultado = subprocess.run(
            ["C:\\Users\\Torre\\Desktop\\iperf3.18_64\\iperf3.18_64\\iperf3.exe", "-c", ip_servidor, "-t", str(duracion)],
            capture_output=True, text=True
        )
        
        # Mostrar la salida
        print(resultado.stdout)
        if resultado.stderr:
            print("Errores:")
            print(resultado.stderr)
    
    except FileNotFoundError:
        print("No se encuentra iperf3 en la ruta proporcionada o hay un error al ejecutar el comando.")

if __name__ == "__main__":
    ip_servidor = "100.113.141.37"  # Cambia esto por la IP de la PC servidor
    medir_ancho_de_banda(ip_servidor)