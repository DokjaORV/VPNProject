# README
## Actividad 06 - Optimización de Transferencia de Archivos en una VPN con Algoritmos Voraces 
-----
### Descripción
En el presente proyecto implementamos la transferencia de archivos por medio del algoritmo de Dijkstra. Para esto fue requerido la aplicación de la página web de Tailscale para obtener y conocer las IPs de cada uno de los usuarios que participaran en el proyecto. Posteriormente de haber conseguido cada una de las IPs las mismas nos sirvieron para realizar métricas, como la latencia y el ancho de banda. Seguido de esto, implementamos Dijkstra para la transferencia de archivos y Kruskal para conocer el árbol de expansión mínima (MST) con la finalidad de optimizar el uso de la red.


### Selección de metodología de trabajo
Cómo método de trabajo para este projecto decidimos trabajar con la metodología de trabajo ágil de Kanban. Este método nos permitió llevar a cabo el proyecto con un mejor flujo de trabajo, además de permitirnos visualizar el flujo de trabajo y en done había que enfocarnos y en dónde más problemas tuvimos.
Implementar esta metodología fue particularmente útil al momento  de decidir las actividades por realizar, así cómo llevar un seguimiento de las mismas.



### Parte 1: Configuración de la VPN
Para la creación de la VPN decidimos hacer uso de la herramienta Tailscale, que nos ayudó a crear rápidamente una VPN para después comenzar a agregar al resto de colaboradores y sus dispositivos.
Esta herramienta permitió interconectar cada uno de nuestros equipos facilitando muchas de las funcionalidades de nuestros programas

![Dispositivos conectados a una VPN Tailscale](https://github.com/DokjaORV/VPNProject/blob/ea74386b77771011d3322444c10ba6856bf3c79d/docs/imagenes/image.png)

Para conectarse a la red tailscale del creador de la VPN, necesitamos pagar la suscripción de tailscale ya que únicamente permite a 3 usuarios lo cual en nuestro equipo no era apto.
Seguido de ello, el Cowner de la VPN, compartirá la red ya sea por medio de correo electrónico o link para que los demás colaboradores se unan con un correo electrónico de preferencia y después seleccionen unirse a la red compartida.
Cabe mencionar, que el owner es el encargado de asignar qué roles tendrán los invitados antes de unirse a la red.

### Paso 2: Medición de las métricas de red

Para la mediciones de las métricas fue necesario dividirlo en dos partes.
La primera parte se basó únicamente en medir la latencia que se tenía al conectar cada equipo, para esto se hizo uso de un script de python, donde se utilizó la librería pythonping para poder hacer ping con cada uno de las computadoras y poder obtener valor como el mínimo, máximo y latencia promedio que se tenía entre cada conexión.

**Mediciones de latencia**
![Mediciones de latencia](https://github.com/DokjaORV/VPNProject/blob/127fc3ac13c2516bd16ba4f0bdd6d9edd8981ef1/docs/imagenes/image-7.png)

**Mediciones de Ancho de Banda**
![Mediciones de Ancho de Banda](https://github.com/DokjaORV/VPNProject/blob/127fc3ac13c2516bd16ba4f0bdd6d9edd8981ef1/docs/imagenes/image-8.png)

Para la segunda parte de las mediciones, se procedió a medir el ancho de banda, igualmente de las conexiones entre equipos

## Implementación de Algoritmos
### Paso 3: Implementación de Dijkstra
Para comenzar con la implementación tuvimos que hacer uso del grafo de latencias creado anteriormente, que fue el encargado de darnos la pauta para la elaboración.

Por medio del uso de Dijkstra, el programa se encarga de encontrar la ruta más óptima entre dos nodos para enviar un archivo, siendo capaz de utilizar nodos intermedios (dispositivos) formando así, una ruta más eficiente al momento de mandar un archivo. Asi mismo, el programa es capaz de enviar archivos directamente sin necesidad de pasar por nodos intermedios, dándole la opción al usuario por medio de una interfaz gráfica de seleccionar quien es el origen, el rol que tiene, el destino al que quiere llegar, además, de poder seleccionar el archivo de su preferencia.

![Interfaz gráfica Dijkstra](https://github.com/DokjaORV/VPNProject/blob/ebec378e10d9fa1bd14e648b1d9f4c9fc6208080/docs/imagenes/image-1.png)


Probando el algoritmo, nos dimos cuenta que el programa no está del todo diseñado para archivos demasiado grandes, por lo que se recomienda, hacer envío de archivos pequeños, esto con el fin de garantizar un correcto funcionamiento del programa.
Esta es una prueba de cómo funciona el envio buscando la ruta más rápida:

Pantalla del emisor:
![Envío del emisor](https://github.com/DokjaORV/VPNProject/blob/ea74386b77771011d3322444c10ba6856bf3c79d/docs/imagenes/image-2.png)

Pantalla del nodo intermedio:
![Nodo Intermedio](https://github.com/DokjaORV/VPNProject/blob/e51459510b8ffaaff103bca9dea6fe37539d4f11/docs/imagenes/image-3.png)

Pantalla del receptor:
![Pantalla del Receptor](https://github.com/DokjaORV/VPNProject/blob/e51459510b8ffaaff103bca9dea6fe37539d4f11/docs/imagenes/image-4.png)


En este link encontrarás el algoritmo para probarlo directamente en tu dispositivo, hay que asegurarse de que los dispositivos emisores y receptores ejecuten el archivo y en dado caso que tengas nodos intermedios, de igual manera.
[Código](https://github.com/DokjaORV/VPNProject/blob/main/src/Dijkstra.py)

### Paso 4: Análisis de Red con Algoritmo de Kruskal

Este proyecto implementa el algoritmo de Kruskal para encontrar un Árbol de Expansión Mínima (MST) en una red representada como grafo ponderado. El objetivo es optimizar el uso de la red basándose en los valores de ancho de banda entre los nodos.
Como primer paso, creamos el grafo con el ancho de banda con el fin de identificar cómo es que se armaria para posteriormente aplicar Kruskal

![Grafo de Ancho de Banda](https://github.com/DokjaORV/VPNProject/blob/127fc3ac13c2516bd16ba4f0bdd6d9edd8981ef1/docs/imagenes/image-5.png)

Una vez armado el grafo de ancho de banda con las conexiones entre 4 nodos (personas) las cuales son: **Alan, Andres, Marlene y Giovanni**
y cada arista tiene dos valores los cuales son:
- **Valor superior**: Ancho de banda de subida (Mbps)
- **Valor inferior**: Ancho de banda de bajada (Mbps)

Una vez que identificamos los valores del grafo, para los cálculos se tomó el promedio entre subida y bajada

![Kruskal](https://github.com/DokjaORV/VPNProject/blob/127fc3ac13c2516bd16ba4f0bdd6d9edd8981ef1/docs/imagenes/image-6.png)

## Comparación entre la topología original con la propuesta por Kruskal


| Enlace              | Subida | Bajada | Promedio |
|---------------------|--------|--------|----------|
| Alan – Andres       | 2.5    | 2.1    | 2.30     |
| Alan – Marlene      | 3.38   | 2.8    | 3.09     |
| Alan – Giovanni     | 3.2    | 1.27   | 2.24     |
| Andres – Marlene    | 3.12   | 2.29   | 2.71     |
| Andres – Giovanni   | 1.8    | 1.02   | 1.41     |
| Marlene – Giovanni  | 3.5    | 1.02   | 2.26     |

**Costo total de la topología original:** `13.99`

Como podemos darnos cuenta, la topología original toma todos los posibles enlaces y además, el costo total de dicha topología es elevado.

Ahora con el Árbol de Expansión Mínima (MST) con Kruskal, se seleccionaron las conexiones más eficientes que unen todos los nodos sin formar ciclos:

| Enlace              | Promedio |
|---------------------|----------|
| Andres – Giovanni   | 1.41     |
| Alan – Giovanni     | 2.24     |
| Andres – Marlene    | 2.71     |

**Costo total del MST:** `6.36`

Aquí podemos darnos cuenta de la eficiencia que tiene Kruskal, 

## Comparativa

| Topología          | Costo total |
|--------------------|-------------|
| Original           | 13.99       |
| Árbol (Kruskal)    | 6.36        |

**Ahorro total:** `7.63 Mbps` en promedio de ancho de banda.

