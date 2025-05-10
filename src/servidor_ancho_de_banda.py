import subprocess

def iniciar_servidor_iperf3():
    try:
        print("Iniciando iperf3 en modo servidor...\n")
        
        # Ejecutar iperf3 en modo servidor
        resultado = subprocess.run(
            ["C:\\Users\\Torre\\Desktop\\iperf3.18_64\\iperf3.18_64\\iperf3.exe", "-s"],
            capture_output=True, text=True
        )
        
        # Mostrar la salida del servidor
        print(resultado.stdout)
        if resultado.stderr:
            print("Errores:")
            print(resultado.stderr)
    
    except FileNotFoundError:
        print("No se encuentra iperf3 en la ruta proporcionada o hay un error al ejecutar el comando.")

if __name__ == "__main__":
    iniciar_servidor_iperf3()