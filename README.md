# 🌐 Análisis de Red con Algoritmo de Kruskal

Este proyecto implementa el algoritmo de Kruskal para encontrar un Árbol de Expansión Mínima (MST) en una red representada como grafo ponderado. El objetivo es optimizar el uso de la red basándose en los valores de ancho de banda entre los nodos.

## 📊 Información del Grafo

El grafo representa conexiones entre 4 nodos (personas): **Alan, Andres, Marlene y Giovanni**.  
Cada arista tiene dos valores:
- **Valor superior**: Ancho de banda de subida (Mbps)
- **Valor inferior**: Ancho de banda de bajada (Mbps)

Para los cálculos, se toma el promedio entre subida y bajada.

## 🌐 Topología Original

| Enlace              | Subida | Bajada | Promedio |
|---------------------|--------|--------|----------|
| Alan – Andres       | 2.5    | 2.1    | 2.30     |
| Alan – Marlene      | 3.38   | 2.8    | 3.09     |
| Alan – Giovanni     | 3.2    | 1.27   | 2.24     |
| Andres – Marlene    | 3.12   | 2.29   | 2.71     |
| Andres – Giovanni   | 1.8    | 1.02   | 1.41     |
| Marlene – Giovanni  | 3.5    | 1.02   | 2.26     |

**Costo total de la topología original:** `13.99`

## 🌲 Árbol de Expansión Mínima (MST) con Kruskal

Se seleccionaron las conexiones más eficientes que unen todos los nodos sin formar ciclos:

| Enlace              | Promedio |
|---------------------|----------|
| Andres – Giovanni   | 1.41     |
| Alan – Giovanni     | 2.24     |
| Andres – Marlene    | 2.71     |

**Costo total del MST:** `6.36`

## ✅ Comparativa

| Topología          | Costo total |
|--------------------|-------------|
| Original           | 13.99       |
| Árbol (Kruskal)    | 6.36        |

**Ahorro total:** `7.63 Mbps` en promedio de ancho de banda.

## 🛠️ Tecnologías Utilizadas

- Python 3.x
- NetworkX
- Matplotlib

## 📁 Archivos

- `grafo.png`: Representación gráfica de la red original.
- `kruskal_mst.py`: Script en Python que calcula el MST.
- `README.md`: Documentación del proyecto.
