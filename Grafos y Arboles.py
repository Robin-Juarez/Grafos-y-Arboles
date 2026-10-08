# -*- coding: utf-8 -*-
"""
=====================================================================
 PROGRAMA: ESTRUCTURAS DE DATOS - GRAFOS y ARBOLES
=====================================================================
 QUE HACE (resumen):
   Al ejecutarlo muestra el MENU DE ESTRUCTURAS:
      1. GRAFOS  (matriz de adyacencia, recorridos, mejor ruta)
      2. ARBOLES (recorrido preorden, inorden y postorden)
   Al elegir una estructura aparece su menu con 3 opciones:
      1. Escribir el PROBLEMA COMPLETO (el programa lo interpreta).
      2. Ingresar DATOS CONOCIDOS (nodos y conexiones ya definidos).
      3. Usar un EJEMPLO (4 problemas de Matematica Discreta):
            - Grupo de alumnos (amistades)
            - Alumnos becados (alumnos y destinos)
            - Red de ordenadores
            - Urbanizacion (calles de un solo sentido)
   Con los datos arma el grafo completo y muestra:
      matriz de adyacencia, lista de adyacencia, grado de cada nodo,
      conectividad, recorrido en anchura (BFS), recorrido en
      profundidad (DFS), mejor ruta (Dijkstra) y el DIBUJO del grafo
      (circulos = nodos, lineas/flechas = conexiones) junto a la matriz.

 LIBRERIAS NECESARIAS (instalar una sola vez en la terminal):
      python -m pip install matplotlib networkx
   (networkx solo se usa para DIBUJAR; los algoritmos BFS, DFS y
    Dijkstra estan programados a mano para ver como funcionan)

 PARTE DE ARBOLES (arbol binario):
   Con los datos arma el arbol y muestra: nodos, hojas, altura, el arbol
   en texto, los recorridos PREORDEN, INORDEN, POSTORDEN y por niveles, y
   el DIBUJO del arbol (3 veces, con el orden de visita en rojo).
   Ejemplos de la opcion 3: arbol de busqueda, arbol por relaciones y
   arbol de expresion aritmetica.
   Como escribir un problema de arboles en la opcion 1:
      Insertar 50, 30, 70, 20, 40, 60, 80
      A tiene hijos B y C. B tiene hijos D y E. C tiene hijo derecho F.
      D es hijo izquierdo de B

 REPORTE EN HTML:
   Despues de resolver, el programa pregunta si quiere guardar un reporte
   .html (reporte_grafo.html / reporte_arbol.html) y lo abre en el navegador
   con el dibujo, la matriz y los recorridos.

 COMO ESCRIBIR UN PROBLEMA EN LA OPCION 1 (lenguaje natural):
   Escriba SOLO las relaciones, como en estos ejemplos:
      Marta es amiga de Sergio, Eloy e Irene. Sergio es amigo de Lidia...
      Sergio elige Mexico, Chile y Colombia, Eloy elige Argentina...
      1 con el 2,4,5   /   2 con el 1,3,5,6   /   3 con el 2,7 ...
      de la P.1 hacia la 2 y la 9, de la P.2 hacia la 3 ...
   Tambien acepta lineas con peso:   A B 4    |    A-B:4
   Termine con una linea vacia (ENTER).  No deje lineas vacias en medio.

 PROBLEMAS MATEMATICOS QUE SE RESUELVEN:
   - Modelado: un grafo G = (V, E). V = nodos (personas, ordenadores,
     plazas...), E = aristas (amistad, cable, calle...).
       * NO dirigido: la arista va en ambos sentidos (amistad, cable).
       * DIRIGIDO: la arista tiene sentido A->B (calles de un sentido).
       * BIPARTITO: los nodos se separan en 2 grupos y solo hay aristas
         entre grupos (alumnos <-> destinos de las becas).
   - Matriz de adyacencia A (n x n):
         sin pesos: A[i][j] = 1 si hay arista i->j, 0 si no.
         con pesos: A[i][j] = peso, "-" si no hay arista.
         En grafos NO dirigidos la matriz es SIMETRICA.
   - Grado de un nodo = cantidad de conexiones. En un grafo no dirigido
     se cumple el LEMA DEL APRETON DE MANOS:
         suma de los grados = 2 * (numero de aristas).
   - Conectividad: se cuentan las COMPONENTES CONEXAS con BFS.
   - BFS (anchura): visita por niveles con una COLA. Costo O(V + E).
   - DFS (profundidad): baja lo mas posible por un camino y retrocede
     (recursion = PILA). Costo O(V + E).
   - Camino minimo (Dijkstra): dist[v] = min(dist[v], dist[u] + w(u,v)).
     Costo O((V + E) log V). No funciona con pesos NEGATIVOS, por eso se
     rechazan. Si el grafo no tiene pesos cada arista cuesta 1, y la
     "mejor ruta" es la que usa MENOS conexiones.

   MATEMATICAS DE LOS ARBOLES:
   - Un arbol es un grafo conexo sin ciclos: aristas = nodos - 1.
   - Arbol binario: cada nodo tiene como maximo 2 hijos (izquierdo, derecho).
   - Altura = aristas del camino mas largo desde la raiz hasta una hoja.
   - Recorridos (costo O(n), cada nodo se visita una vez):
       PREORDEN  = raiz, izquierdo, derecho
       INORDEN   = izquierdo, raiz, derecho
       POSTORDEN = izquierdo, derecho, raiz
   - Arbol de busqueda: menores a la izquierda, mayores a la derecha;
     su INORDEN da los valores ordenados. Insertar cuesta O(altura).
   - Arbol de expresion: preorden = notacion prefija, inorden = infija,
     postorden = posfija.

 LIBRERIAS QUE USA (y para que sirve cada una):
   heapq              cola de prioridad (monton): en Dijkstra entrega siempre el nodo
                      pendiente de menor distancia, en O(log n).
   re                 expresiones regulares: separan palabras y detectan formatos
                      al leer el problema escrito.
   unicodedata        quita acentos para comparar "Mexico" y "México" como iguales.
   collections.deque  cola FIFO (el primero que entra es el primero que sale): se usa
                      en BFS, en el recorrido por niveles y en las componentes conexas.
   html               html.escape: evita que el texto rompa el HTML del reporte.
   math               seno y coseno para ubicar los nodos en circulo (dibujo SVG).
   os                 rutas de archivos: guarda el reporte junto al programa.
   webbrowser         abre el reporte HTML en el navegador.
   pathlib.Path       convierte la ruta del archivo en un enlace file:// para el navegador.
   matplotlib.pyplot  ventana grafica: dibuja el grafo, la matriz y los arboles.
   networkx           solo calcula posiciones y dibuja el grafo; los algoritmos
                      (BFS, DFS, Dijkstra, recorridos) estan programados a mano.
   (matplotlib y networkx se instalan con: python -m pip install matplotlib networkx;
    las demas librerias ya vienen con Python.)

 FLUJO GENERAL DEL PROGRAMA (ENTRADA -> PROCESO -> SALIDA):
   ENTRADA : la persona elige la estructura (grafos o arboles), el modo (problema
             escrito, datos conocidos o ejemplo) y escribe o elige los datos.
   PROCESO : 1) interpretar_texto / interpretar_arbol_texto convierten el texto en
                conexiones; 2) se arma el Grafo o el Arbol; 3) se calculan la matriz,
                los grados, la conectividad, los recorridos y la mejor ruta (o los
                recorridos preorden, inorden y postorden del arbol).
   SALIDA  : resultados en consola + ventana grafica (dibujo) + reporte HTML opcional.

 INDICE DE FUNCIONES (en el orden del archivo):
   Texto        : sin_acentos, clave_natural, formatear
   Grafos       : clase Grafo (nodos, aristas, matriz, grados, componentes, bfs, dfs,
                  dijkstra, mejor_ruta)
   Interprete   : interpretar_texto, interpretar_linea_con_peso, construir_grafo
   Entrada      : modo_problema_completo, modo_datos_conocidos, ejemplo_precargado
   Salida       : mostrar_conexiones, mostrar_matriz, mostrar_lista,
                  mostrar_grados_y_conexidad, dibujar, resolver, menu_grafos
   Arboles      : clases Nodo y Arbol, armar_abb, armar_arbol_relaciones,
                  interpretar_arbol_texto, texto_arbol, estadisticas_arbol,
                  mostrar_arbol, modos 1/2/3 de arboles, dibujar_arbol, resolver_arbol
   Reporte HTML : guardar_y_abrir_html, tabla_html, svg_grafo, reporte_grafo_html,
                  svg_arbol, reporte_arbol_html
   Menus        : menu_arboles, menu_principal
=====================================================================
"""

import heapq                      # cola de prioridad (monton): nodo de menor distancia en Dijkstra
import re                         # expresiones regulares: separar palabras y detectar formatos
import unicodedata                # quitar acentos al comparar palabras
import html                       # escapar texto para que no rompa el reporte HTML
import math                       # seno y coseno para ubicar los nodos en circulo (SVG)
import os                         # rutas de archivos (guardar el reporte junto al programa)
import webbrowser                 # abrir el reporte HTML en el navegador
from pathlib import Path          # convertir una ruta en enlace file:// para el navegador
from collections import deque     # cola FIFO: BFS, recorrido por niveles, componentes

import matplotlib.pyplot as plt   # ventana grafica (dibujo del grafo, matriz y arboles)
import networkx as nx             # solo para calcular posiciones y dibujar el grafo

INF = float("inf")                # "infinito": nodo inalcanzable


# ===================================================================
#  FUNCIONES AUXILIARES DE TEXTO
# ===================================================================
def sin_acentos(texto):
    """
    QUE HACE: pasa un texto a minusculas y le quita los acentos.
    COMO FUNCIONA: unicodedata.normalize("NFD") separa cada letra de su acento
                   (e + ´) y despues se descartan las marcas de acento (categoria "Mn").
    ENTRADA : texto (ej. "México").
    PROCESO : normalizar -> quitar las marcas de acento -> pasar a minusculas.
    SALIDA  : texto (ej. "mexico").
    PARA QUE: comparar "Mexico" y "México" como si fueran la misma palabra.
    """
    base = unicodedata.normalize("NFD", texto)
    return "".join(c for c in base if unicodedata.category(c) != "Mn").lower()


def clave_natural(texto):
    """
    QUE HACE: crea una clave de orden "natural": P2 va antes que P10 y 2 antes que 10
              (el orden normal de texto pondria "10" antes que "2").
    COMO FUNCIONA: re.split separa letras y numeros ("P10" -> ["P","10",""]);
                   los pedazos numericos se vuelven int para compararse como numeros.
    ENTRADA : texto (nombre de un nodo).
    PROCESO : separar letras y numeros -> numeros a int -> letras a minusculas.
    SALIDA  : lista que se usa como sorted(..., key=clave_natural).
    """
    partes = re.split(r"(\d+)", texto)
    return [int(p) if i % 2 else p.lower() for i, p in enumerate(partes)]


def formatear(numero):
    """
    QUE HACE: muestra 4.0 como 4 y 2.5 como 2.5 (solo presentacion).
    ENTRADA : numero (int o float).
    PROCESO : si float(numero).is_integer() es True se convierte a int.
    SALIDA  : el numero sin ".0" cuando es entero.
    """
    return int(numero) if float(numero).is_integer() else numero


# ===================================================================
#  CLASE GRAFO
#  Guarda el grafo y contiene todos los algoritmos.
# ===================================================================
class Grafo:
    """
    QUE ES: la estructura de datos GRAFO G = (V, E) y todos sus algoritmos.
    REPRESENTACION: LISTA DE ADYACENCIA = diccionario  nodo -> {vecino: peso}.
       Ocupa O(V + E) de memoria (una matriz de adyacencia ocuparia O(V^2)).
    METODOS: agregar_nodo, agregar_arista, nodos, vecinos, es_ponderado, aristas,
       matriz_adyacencia, grados, componentes, bfs, dfs, dijkstra, mejor_ruta.
    PROBLEMAS MATEMATICOS QUE RESUELVE: matriz de adyacencia, grado de los nodos
       (lema del apreton de manos), conectividad, recorridos BFS y DFS y camino
       minimo (Dijkstra). Cada metodo explica su calculo.
    """
    def __init__(self, dirigido=False, izquierda=None):
        """
        QUE HACE: crea un grafo vacio.
        ENTRADA : dirigido  (True = aristas con sentido A->B).
                  izquierda (conjunto de nodos del grupo izquierdo si el
                             grafo es bipartito, solo para dibujarlo).
        PROCESO : crea el diccionario  nodo -> {vecino: peso}
                  (la LISTA DE ADYACENCIA).
        SALIDA  : objeto Grafo listo para agregar aristas.
        """
        self.dirigido = dirigido
        self.izquierda = izquierda
        self.ady = {}

    # ---------------------------------------------------------------
    def agregar_nodo(self, nodo):
        """
        QUE HACE: agrega un nodo si todavia no existe.
        ENTRADA : nombre del nodo (texto).
        PROCESO : si el nombre no esta en el diccionario, crea su entrada con un
                  diccionario de vecinos vacio.
        SALIDA  : ninguna (modifica el grafo).
        """
        if nodo not in self.ady:
            self.ady[nodo] = {}

    # ---------------------------------------------------------------
    def agregar_arista(self, origen, destino, peso=1.0):
        """
        QUE HACE: conecta dos nodos con un peso (1 si el problema no tiene).
        ENTRADA : origen, destino y peso (>= 0).
        PROCESO : crea los nodos si faltan y guarda el peso. Si el grafo NO
                  es dirigido guarda tambien destino->origen. Si la arista
                  ya existia, conserva el peso menor.
        SALIDA  : ninguna (modifica el grafo).
        """
        self.agregar_nodo(origen)
        self.agregar_nodo(destino)
        if destino not in self.ady[origen] or peso < self.ady[origen][destino]:
            self.ady[origen][destino] = peso
        if not self.dirigido:
            if origen not in self.ady[destino] or peso < self.ady[destino][origen]:
                self.ady[destino][origen] = peso

    # ---------------------------------------------------------------
    def nodos(self):
        """
        QUE HACE: devuelve los nodos ordenados.
        ENTRADA : ninguna (usa el grafo).
        PROCESO : toma las llaves del diccionario y las ordena con clave_natural
                  (asi la matriz y los recorridos siempre salen en el mismo orden).
        SALIDA  : lista de nombres de nodos.
        """
        return sorted(self.ady.keys(), key=clave_natural)

    # ---------------------------------------------------------------
    def vecinos(self, nodo):
        """
        QUE HACE: devuelve los vecinos de un nodo (los nodos a los que llega una arista).
        ENTRADA : nombre del nodo.
        PROCESO : toma las llaves de su diccionario de vecinos y las ordena (orden natural).
        SALIDA  : lista de vecinos. Su largo es el grado de salida del nodo.
        """
        return sorted(self.ady[nodo], key=clave_natural)

    # ---------------------------------------------------------------
    def es_ponderado(self):
        """
        QUE HACE: indica si el grafo tiene pesos (distancias, costos...).
        ENTRADA : ninguna (usa el grafo).
        PROCESO : revisa todas las aristas; si alguna tiene un peso distinto de 1 es ponderado.
        SALIDA  : True / False. Decide como se muestran la matriz (1/0 o pesos), las
                  etiquetas del dibujo y las unidades ("conexiones") de la mejor ruta.
        """
        return any(p != 1 for v in self.ady.values() for p in v.values())

    # ---------------------------------------------------------------
    def aristas(self):
        """
        QUE HACE: lista las aristas SIN repetir.
        ENTRADA : ninguna (usa el grafo).
        PROCESO : en un grafo no dirigido (A,B) y (B,A) son la misma arista, por eso solo
                  se guarda cuando clave(A) < clave(B). En uno dirigido se guardan todas.
        SALIDA  : lista de tuplas (origen, destino, peso).
        MATEMATICA: |E| = numero de aristas; se usa en el lema del apreton de manos.
        """
        lista = []
        for u in self.nodos():
            for v in self.vecinos(u):
                if self.dirigido or clave_natural(u) < clave_natural(v):
                    lista.append((u, v, self.ady[u][v]))
        return lista

    # ---------------------------------------------------------------
    def matriz_adyacencia(self):
        """
        QUE HACE: construye la MATRIZ DE ADYACENCIA A de tamano n x n.
        ENTRADA : ninguna (usa el grafo).
        PROCESO : fila i, columna j -> arista i->j.
                  Sin pesos: A[i][j] = 1 si existe, 0 si no.
                  Con pesos: A[i][j] = peso si existe, "-" si no. La diagonal es 0.
        SALIDA  : (lista_de_nodos, matriz como lista de listas).
        MATEMATICA: en un grafo NO dirigido la matriz es SIMETRICA (A[i][j] = A[j][i]);
                  en uno dirigido no tiene por que serlo.
        """
        ponderado = self.es_ponderado()
        lista = self.nodos()
        matriz = []
        for i in lista:
            fila = []
            for j in lista:
                if i == j:
                    fila.append(0)
                elif j in self.ady[i]:
                    fila.append(self.ady[i][j] if ponderado else 1)
                else:
                    fila.append("-" if ponderado else 0)
            matriz.append(fila)
        return lista, matriz

    # ---------------------------------------------------------------
    def grados(self):
        """
        QUE HACE: calcula el grado de cada nodo.
        ENTRADA : ninguna (usa el grafo).
        PROCESO : salida = aristas que salen del nodo (largo de su lista de vecinos);
                  entrada = aristas que llegan a el (se cuentan recorriendo todas las listas).
        SALIDA  : diccionario nodo -> (entrada, salida). En no dirigidos ambos valores son iguales.
        MATEMATICA: LEMA DEL APRETON DE MANOS: en un grafo no dirigido
                  suma de los grados = 2 * (numero de aristas).
        """
        entrada = {n: 0 for n in self.ady}
        for u in self.ady:
            for v in self.ady[u]:
                entrada[v] += 1
        return {n: (entrada[n], len(self.ady[n])) for n in self.ady}

    # ---------------------------------------------------------------
    def componentes(self):
        """
        QUE HACE: separa el grafo en COMPONENTES CONEXAS (grupos de nodos alcanzables entre si).
        ENTRADA : ninguna (usa el grafo).
        PROCESO : ignora el sentido de las aristas y hace un BFS desde cada nodo todavia no
                  visitado; cada BFS descubre una componente completa.
        SALIDA  : lista de listas de nodos. Si hay una sola, el grafo es CONEXO.
        MATEMATICA: costo O(V + E).
        """
        vec = {n: set() for n in self.ady}
        for u in self.ady:
            for v in self.ady[u]:
                vec[u].add(v)
                vec[v].add(u)
        visitados, comps = set(), []
        for n in self.nodos():
            if n in visitados:
                continue
            comp, cola = [], deque([n])
            visitados.add(n)
            while cola:
                x = cola.popleft()
                comp.append(x)
                for y in vec[x]:
                    if y not in visitados:
                        visitados.add(y)
                        cola.append(y)
            comps.append(sorted(comp, key=clave_natural))
        return comps

    # ---------------------------------------------------------------
    def bfs(self, inicio):
        """
        QUE HACE: recorre el grafo en ANCHURA desde un nodo y devuelve el orden de visita.
        RECORRIDO EN ANCHURA (Breadth First Search).
        ENTRADA : nodo de inicio.
        PROCESO : mete el inicio en una cola; saca el primero, lo agrega al
                  recorrido y mete sus vecinos no visitados; repite hasta
                  vaciar la cola. Se visita por niveles (saltos).
        SALIDA  : lista con el orden de visita.
        MATEMATICA: BFS recorre por NIVELES (distancia en saltos desde el inicio). Cada nodo y
           cada arista se revisan una vez: costo O(V + E). La estructura clave es la COLA (FIFO).
        """
        visitados = {inicio}
        cola = deque([inicio])
        orden = []
        while cola:
            actual = cola.popleft()          # saca el primero (FIFO)
            orden.append(actual)
            for vecino in self.vecinos(actual):
                if vecino not in visitados:
                    visitados.add(vecino)
                    cola.append(vecino)
        return orden

    # ---------------------------------------------------------------
    def dfs(self, inicio):
        """
        QUE HACE: recorre el grafo en PROFUNDIDAD desde un nodo y devuelve el orden de visita.
        RECORRIDO EN PROFUNDIDAD (Depth First Search).
        ENTRADA : nodo de inicio.
        PROCESO : visita el nodo y se mete recursivamente en el primer
                  vecino no visitado; al no poder avanzar, retrocede
                  (backtracking) y prueba el siguiente.
        SALIDA  : lista con el orden de visita.
        MATEMATICA: DFS baja lo mas posible por un camino y retrocede (backtracking). Costo
           O(V + E). La recursion usa la PILA de llamadas (LIFO).
        """
        visitados = set()
        orden = []

        def visitar(nodo):
            """
            QUE HACE: visita un nodo y se mete recursivamente en sus vecinos.
            ENTRADA : nodo actual.
            PROCESO : lo marca como visitado, lo agrega al recorrido y llama a visitar() con
                      cada vecino aun no visitado; al terminar con ellos retrocede.
            SALIDA  : ninguna (llena las listas 'visitados' y 'orden').
            """
            visitados.add(nodo)
            orden.append(nodo)
            for vecino in self.vecinos(nodo):
                if vecino not in visitados:
                    visitar(vecino)          # llamada recursiva = bajar un nivel

        visitar(inicio)
        return orden

    # ---------------------------------------------------------------
    def dijkstra(self, origen):
        """
        QUE HACE: calcula la distancia minima desde un origen hasta todos los nodos.
        CAMINO MINIMO DESDE UN ORIGEN (algoritmo de Dijkstra).
        ENTRADA : nodo origen.
        PROCESO : 1) dist[origen] = 0, los demas = infinito.
                  2) con un heap se toma el nodo pendiente de menor
                     distancia conocida (u).
                  3) relajacion: para cada vecino v de u, si
                     dist[u] + peso(u,v) < dist[v] se actualiza dist[v]
                     y se anota previo[v] = u.
                  4) se repite hasta vaciar el heap.
        SALIDA  : (dist, previo)  distancia minima a cada nodo y el nodo
                  anterior en la mejor ruta (para reconstruirla).
        MATEMATICA: resuelve el problema del CAMINO MINIMO desde un origen en un grafo con
           pesos >= 0. Relajacion: dist[v] = min(dist[v], dist[u] + w(u,v)). Con heap cuesta
           O((V + E) log V). Con pesos negativos podria dar resultados incorrectos; por eso
           el programa los rechaza al leer los datos.
        """
        dist = {n: INF for n in self.ady}
        previo = {n: None for n in self.ady}
        dist[origen] = 0
        heap = [(0, origen)]
        while heap:
            d, u = heapq.heappop(heap)
            if d > dist[u]:                  # entrada vieja, ya hay una mejor
                continue
            for v, peso in self.ady[u].items():
                nueva = d + peso
                if nueva < dist[v]:          # relajacion de la arista u->v
                    dist[v] = nueva
                    previo[v] = u
                    heapq.heappush(heap, (nueva, v))
        return dist, previo

    # ---------------------------------------------------------------
    def mejor_ruta(self, origen, destino):
        """
        QUE HACE: obtiene la mejor ruta (la de menor costo) entre dos nodos.
        ENTRADA : nodo origen y nodo destino.
        PROCESO : ejecuta Dijkstra desde el origen y reconstruye el camino yendo hacia atras
                  desde el destino con el diccionario 'previo' (previo[v] = nodo anterior).
        SALIDA  : (ruta, costo). Si no hay camino devuelve ([], inf).
        """
        dist, previo = self.dijkstra(origen)
        if dist[destino] == INF:
            return [], INF
        ruta = []
        actual = destino
        while actual is not None:
            ruta.append(actual)
            actual = previo[actual]
        ruta.reverse()
        return ruta, dist[destino]


# ===================================================================
#  INTERPRETE DE PROBLEMAS ESCRITOS EN TEXTO
# ===================================================================
# Palabras que indican "el nodo anterior se conecta con los siguientes"
PALABRAS_RELACION = {"de", "con", "hacia", "elige", "eligen", "eligio",
                     "conecta", "conectado", "conectada", "unido", "unida"}

# Palabras de relleno que se ignoran (no son nodos)
PALABRAS_RELLENO = {"es", "son", "ser", "esta", "estan", "amigo", "amiga",
                    "amigos", "amigas", "el", "la", "los", "las", "un", "una",
                    "y", "e", "o", "u", "a", "al", "del", "finalmente",
                    "ademas", "tambien", "luego", "despues", "se", "que",
                    "en", "por", "para", "pero", "ya", "su", "sus", "tiene",
                    "tienen", "entre", "amistad", "conexion", "conexiones"}


def interpretar_texto(texto):
    """
    QUE HACE: convierte un problema escrito en lenguaje natural en una
              lista de conexiones.
    ENTRADA : texto, por ejemplo
              "Marta es amiga de Sergio, Eloy e Irene, Sergio de Lidia..."
    PROCESO : 1) limpia el texto ("P.1" -> "P1"; "de la P1 hacia" -> "P1 hacia").
              2) lo corta en palabras y descarta las de relleno (es, la, y...).
              3) recorre las palabras guardando los nombres en 'pendiente'.
              4) cuando aparece una palabra de relacion (de, con, hacia,
                 elige...), el ULTIMO nombre pendiente es el nuevo SUJETO y
                 los nombres anteriores son los destinos del sujeto previo.
                 Ejemplo: [Sergio, Eloy, Irene, Sergio] + "de"
                          -> Marta se conecta con Sergio, Eloy, Irene
                             y el nuevo sujeto es Sergio.
              5) si hay una sola letra de prefijo (P1, P2...) los numeros
                 sueltos de los destinos se completan (la 2 -> P2).
              6) "hacia" indica grafo DIRIGIDO; "elige" indica grafo
                 BIPARTITO (alumnos a la izquierda, destinos a la derecha).
    SALIDA  : (aristas, dirigido, izquierda)
              aristas   = lista de pares (origen, destino)
              dirigido  = True/False
              izquierda = conjunto de nodos del grupo izquierdo o None
    MATEMATICA: es el MODELADO del problema: personas/ordenadores/plazas = nodos (V) y
       amistades/cables/calles = aristas (E). "hacia" produce un grafo dirigido; "elige"
       produce un grafo bipartito (dos grupos y solo aristas entre grupos).
    """
    texto = re.sub(r"\b([A-Za-z])\.(\d+)", r"\1\2", texto)          # P.1 -> P1
    texto = re.sub(r"\bde\s+(?:la\s+|el\s+)?(\w+)\s+hacia", r"\1 hacia",
                   texto, flags=re.IGNORECASE)                     # de la P1 hacia
    palabras = re.findall(r"\w+", texto)

    # Si el problema usa nodos de una letra (A, B, C...) esas letras SON nodos;
    # si no, una "Y" o "E" mayuscula solo es la conjuncion "y" / "e".
    letras = [p for p in palabras if len(p) == 1 and p.isalpha() and p.isupper()]
    usa_letras = any(l not in "YEAOU" for l in letras)

    nombres = {}          # clave sin acentos -> nombre mostrado
    aristas = []          # resultado: pares (origen, destino)
    sujetos = []          # nodos que tuvieron destinos
    dirigido = False
    elige = False
    sujeto = None
    pendiente = []

    def unificar(pal):
        """
        QUE HACE: usa siempre la misma escritura para un nombre (Mexico = México = mexico).
        ENTRADA : palabra tal como la escribio la persona.
        PROCESO : busca su version sin acentos en el diccionario 'nombres'; si no esta, guarda
                  la palabra con la primera letra en mayuscula.
        SALIDA  : el nombre unificado.
        """
        k = sin_acentos(pal)
        if k not in nombres:
            nombres[k] = pal[:1].upper() + pal[1:]
        return nombres[k]

    def guardar(suj, destinos):
        """
        QUE HACE: guarda las conexiones del sujeto actual.
        ENTRADA : sujeto y lista de destinos.
        PROCESO : agrega la arista (sujeto, destino) por cada destino (sin lazos a si mismo)
                  y recuerda al sujeto si tuvo destinos.
        SALIDA  : ninguna (agrega a las listas 'aristas' y 'sujetos').
        """
        if suj is None:
            return
        for d in destinos:
            if d != suj:
                aristas.append((suj, d))
        if destinos and suj not in sujetos:
            sujetos.append(suj)

    for pal in palabras:
        k = sin_acentos(pal)
        letra_nodo = usa_letras and len(pal) == 1 and pal.isalpha() and pal.isupper()
        if k in PALABRAS_RELACION:
            if k == "hacia":
                dirigido = True
            if k in ("elige", "eligen", "eligio"):
                elige = True
            if pendiente:
                nuevo = pendiente.pop()      # el ultimo nombre pasa a ser sujeto
                guardar(sujeto, pendiente)
                sujeto = nuevo
                pendiente = []
            continue
        if k in PALABRAS_RELLENO and not letra_nodo:
            continue
        pendiente.append(unificar(pal))
    guardar(sujeto, pendiente)

    # Completar prefijos: si hay P1, P2... y numeros sueltos, "2" pasa a "P2"
    prefijos = {re.match(r"([A-Za-z]+)\d+$", n).group(1)
                for n in nombres.values() if re.match(r"[A-Za-z]+\d+$", n)}
    if len(prefijos) == 1:
        pref = prefijos.pop()
        def completar(n):
            """
            QUE HACE: completa un numero suelto con el prefijo de las plazas (2 -> P2).
            ENTRADA : nombre de nodo.
            PROCESO : si es solo un numero le antepone el prefijo unico encontrado (P).
            SALIDA  : el nombre completo.
            """
            return pref + n if n.isdigit() else n
        aristas = [(completar(a), completar(b)) for a, b in aristas]
        sujetos = [completar(s) for s in sujetos]

    izquierda = set(sujetos) if elige else None
    return aristas, dirigido, izquierda


def interpretar_linea_con_peso(linea):
    """
    QUE HACE: reconoce una linea con peso como "A B 4", "A-B:4" o "A->B 4".
    ENTRADA : linea de texto.
    PROCESO : cambia los separadores por espacios; si quedan exactamente
              3 palabras y la tercera es un numero, es una arista con peso.
    SALIDA  : (origen, destino, peso), "NEGATIVO" si el peso es negativo,
              o None si la linea no tiene ese formato.
    """
    if re.search(r"\s-\d+(\.\d+)?\s*$", linea):
        return "NEGATIVO"
    limpia = linea
    for simbolo in ["->", "-", ">", ",", ":", ";", "=", "|"]:
        limpia = limpia.replace(simbolo, " ")
    p = limpia.split()
    if len(p) != 3:
        return None
    try:
        peso = float(p[2])
    except ValueError:
        return None
    if sin_acentos(p[0]) in PALABRAS_RELACION or sin_acentos(p[1]) in PALABRAS_RELACION:
        return None
    return p[0], p[1], peso


# ===================================================================
#  CONSTRUCCION Y PRESENTACION DEL GRAFO
# ===================================================================
def construir_grafo(aristas, dirigido, izquierda=None, pesadas=()):
    """
    QUE HACE: arma el objeto Grafo con las conexiones interpretadas.
    ENTRADA : aristas sin peso [(a,b)], dirigido, grupo izquierdo (bipartito) y
              aristas con peso [(a,b,peso)].
    PROCESO : crea el Grafo y agrega cada arista (peso 1 si no tiene peso).
    SALIDA  : objeto Grafo.
    """
    g = Grafo(dirigido, izquierda)
    for a, b in aristas:
        g.agregar_arista(a, b, 1.0)
    for a, b, w in pesadas:
        g.agregar_arista(a, b, w)
    return g


def mostrar_conexiones(grafo):
    """
    QUE HACE: imprime como entendio el programa el problema, para que la persona
              verifique que los datos quedaron bien.
    ENTRADA : grafo.
    PROCESO : indica el tipo (dirigido o no), cuenta nodos y conexiones y las muestra de
              4 en 4 con "->" (dirigido) o "--" (no dirigido), con su peso si lo hay.
    SALIDA  : texto en pantalla.
    """
    tipo = "DIRIGIDO" if grafo.dirigido else "NO DIRIGIDO"
    lista = grafo.aristas()
    simbolo = "->" if grafo.dirigido else "--"
    print(f"\nGrafo {tipo}: {len(grafo.ady)} nodos y {len(lista)} conexiones.")
    texto = [f"{a} {simbolo} {b}" + (f" ({formatear(p)})" if grafo.es_ponderado() else "")
             for a, b, p in lista]
    for i in range(0, len(texto), 4):
        print("   " + "   |   ".join(texto[i:i + 4]))


def pedir_si_no(pregunta):
    """
    QUE HACE: hace una pregunta de si/no y repite hasta que respondan bien.
    ENTRADA : texto de la pregunta.
    PROCESO : lee la respuesta; si empieza con 's' o 'n' termina, si no vuelve a preguntar.
    SALIDA  : True si la respuesta empieza con 's', False si con 'n'.
    """
    while True:
        r = input(pregunta + " (s/n): ").strip().lower()
        if r.startswith("s"):
            return True
        if r.startswith("n"):
            return False
        print("   Responda s o n.")


# ===================================================================
#  OPCION 1 - PROBLEMA COMPLETO
# ===================================================================
def modo_problema_completo():
    """
    QUE HACE: lee el problema de grafos escrito por la persona y lo convierte en un Grafo.
    OPCION 1 - MODO PROBLEMA COMPLETO.
    ENTRADA : la persona escribe el problema (varias lineas) y termina con
              una linea vacia.
    PROCESO : las lineas con formato "A B 4" se toman como aristas con peso;
              el resto se junta y lo interpreta interpretar_texto().
              Muestra las conexiones entendidas y pide confirmacion.
    SALIDA  : objeto Grafo, o None si no se escribio nada.
    """
    print("\n--- MODO PROBLEMA COMPLETO ---")
    print("Escriba SOLO las relaciones del problema, por ejemplo:")
    print("   Marta es amiga de Sergio, Eloy e Irene. Sergio es amigo de Lidia y Marta.")
    print("   1 con el 2,4,5     |     de la P.1 hacia la 2 y la 9     |     A B 4")
    print("Al terminar presione ENTER en una linea vacia.\n")
    while True:
        lineas = []
        while True:
            linea = input("  > ").strip()
            if linea == "":
                break
            lineas.append(linea)
        if not lineas:
            return None

        pesadas, texto = [], []
        for linea in lineas:
            dato = interpretar_linea_con_peso(linea)
            if dato == "NEGATIVO":
                print("    Peso negativo no permitido (Dijkstra requiere pesos >= 0):", linea)
            elif dato is not None:
                pesadas.append(dato)
            else:
                texto.append(linea)

        aristas, dirigido, izquierda = interpretar_texto("\n".join(texto))
        if pesadas and not aristas and not dirigido:
            dirigido = pedir_si_no("Las conexiones son de un solo sentido (dirigido)?")
        grafo = construir_grafo(aristas, dirigido, izquierda, pesadas)

        if len(grafo.ady) < 2:
            print("No pude encontrar conexiones. Intente de nuevo.\n")
            continue
        mostrar_conexiones(grafo)
        if pedir_si_no("Esta bien interpretado el problema?"):
            return grafo
        print("\nEscriba el problema de nuevo (ENTER vacio para cancelar):")


# ===================================================================
#  OPCION 2 - DATOS CONOCIDOS
# ===================================================================
def modo_datos_conocidos():
    """
    QUE HACE: arma un Grafo con datos ya conocidos (nodos y conexiones) ingresados paso a paso.
    OPCION 2 - MODO DATOS CONOCIDOS.
    ENTRADA : tipo de grafo (dirigido, con pesos), nombres de los nodos y
              las conexiones, una por linea:
                  sin pesos: ORIGEN DESTINO1 DESTINO2 ...
                  con pesos: ORIGEN DESTINO PESO
    PROCESO : valida que los nodos existan y que el peso sea >= 0.
    SALIDA  : objeto Grafo armado.
    """
    print("\n--- MODO DATOS CONOCIDOS ---")
    dirigido = pedir_si_no("Las conexiones tienen un solo sentido (grafo dirigido)?")
    ponderado = pedir_si_no("Las conexiones tienen peso (distancia, costo, tiempo)?")

    while True:                              # nombres de los nodos
        entrada = input("Nombres de los nodos (separados por coma o espacio): ")
        nombres = [p for p in re.split(r"[,\s]+", entrada.strip()) if p]
        claves = [sin_acentos(n) for n in nombres]
        if len(nombres) >= 2 and len(set(claves)) == len(claves):
            break
        print("   Escriba al menos 2 nodos y sin repetir nombres.")

    grafo = Grafo(dirigido)
    for n in nombres:
        grafo.agregar_nodo(n)
    real = {sin_acentos(n): n for n in nombres}

    if ponderado:
        print("\nEscriba cada conexion:  ORIGEN DESTINO PESO   (ej: A B 4)")
    else:
        print("\nEscriba cada conexion:  ORIGEN DESTINO1 DESTINO2 ...   (ej: 1 2 4 5)")
    print("Cuando termine presione ENTER en una linea vacia.")

    while True:
        linea = input("  > ").strip()
        if linea == "":
            break
        if ponderado and re.search(r"\s-\d+(\.\d+)?\s*$", linea):
            print("    Peso negativo no permitido (Dijkstra requiere pesos >= 0).")
            continue
        limpia = linea
        for simbolo in ["->", "-", ">", ",", ":", ";", "=", "|"]:
            limpia = limpia.replace(simbolo, " ")
        p = limpia.split()
        if len(p) < 2:
            print("    Faltan datos en esa linea.")
            continue
        try:
            if ponderado:
                if len(p) != 3:
                    raise ValueError
                destinos, peso = [p[1]], float(p[2])
            else:
                destinos, peso = p[1:], 1.0
        except ValueError:
            print("    Formato incorrecto (revise el peso).")
            continue
        usados = [p[0]] + destinos
        if any(sin_acentos(u) not in real for u in usados):
            print("    Algun nodo no existe. Nodos:", ", ".join(nombres))
            continue
        for d in destinos:
            if sin_acentos(d) != sin_acentos(p[0]):
                grafo.agregar_arista(real[sin_acentos(p[0])], real[sin_acentos(d)], peso)

    mostrar_conexiones(grafo)
    return grafo


# ===================================================================
#  OPCION 3 - EJEMPLOS (problemas de Matematica Discreta)
# ===================================================================
EJEMPLOS = [
    ("Grupo de alumnos (amistades)",
     "Marta es amiga de Sergio, Eloy e Irene. Sergio es amigo de Lidia, Alicia, "
     "Marta y Guille. Lidia de Sergio y Alicia. Alicia de Lidia, Sergio y Guille. "
     "Eloy de Marta, Irene, Carlos y Guille. Carlos de Eloy, Guille y Francisco. "
     "Guille de Sergio, Alicia, Francisco, Carlos y Eloy. Francisco de Guille y Carlos."),
    ("Alumnos becados (alumnos y destinos)",
     "Sergio elige México, Chile y Colombia, Eloy elige Argentina, "
     "Alba elige México y Colombia y finalmente Marta elige Argentina."),
    ("Red de ordenadores",
     "1 con el 2,4,5\n2 con el 1,3,5,6\n3 con el 2,7\n4 con el 1,5\n"
     "5 con el 1,2,6 y 8\n6 con el 2,5,7\n7 con el 3,6,9\n9 con el 6,7,8\n"
     "8 con el 5,9,10\n10 con el 8"),
    ("Urbanizacion (calles de un solo sentido)",
     "de la P.1 hacia la 2 y la 9, de la P.2 hacia la 3, de la P.3 hacia la 4 y la 6, "
     "de la P.4 hacia la 3, de la P.5 hacia la 4, de la P.6 hacia la 7 y la 5, "
     "de la P.7 hacia la 2 y la 8 y finalmente de la P.9 hacia la 2 y la 8."),
]


def ejemplo_precargado():
    """
    QUE HACE: arma un Grafo a partir de uno de los 4 problemas de ejemplo.
    OPCION 3 - EJEMPLOS.
    ENTRADA : numero del ejemplo (1 a 4).
    PROCESO : toma el texto del problema y lo interpreta con
              interpretar_texto(), igual que si la persona lo escribiera.
    SALIDA  : objeto Grafo, o None si elige volver.
    """
    print("\n--- EJEMPLOS ---")
    for i, (titulo, _) in enumerate(EJEMPLOS, 1):
        print(f"{i}. {titulo}")
    print("0. Volver")
    while True:
        op = input("Ejemplo: ").strip()
        if op == "0":
            return None
        if op.isdigit() and 1 <= int(op) <= len(EJEMPLOS):
            titulo, texto = EJEMPLOS[int(op) - 1]
            print(f"\nPROBLEMA: {titulo}\n{texto}")
            aristas, dirigido, izquierda = interpretar_texto(texto)
            grafo = construir_grafo(aristas, dirigido, izquierda)
            mostrar_conexiones(grafo)
            return grafo
        print("   Opcion no valida.")


# ===================================================================
#  PRESENTACION DE RESULTADOS EN CONSOLA
# ===================================================================
def mostrar_matriz(grafo):
    """
    QUE HACE: imprime la matriz de adyacencia alineada en la consola.
    ENTRADA : grafo.
    PROCESO : obtiene la matriz con grafo.matriz_adyacencia() y alinea las columnas segun
              el nombre de nodo mas largo; escribe la leyenda (1/0 o "-" = sin conexion).
    SALIDA  : texto en pantalla.
    """
    nombres, matriz = grafo.matriz_adyacencia()
    ancho = max(4, max(len(n) for n in nombres) + 1)
    leyenda = "'-' = no hay conexion" if grafo.es_ponderado() else "1 = hay conexion, 0 = no hay"
    print(f"\nMATRIZ DE ADYACENCIA ({leyenda}):")
    print(" " * ancho + "".join(n.rjust(ancho) for n in nombres))
    for nombre, fila in zip(nombres, matriz):
        print(nombre.rjust(ancho) + "".join(str(formatear(x) if x != "-" else x).rjust(ancho) for x in fila))


def mostrar_lista(grafo):
    """
    QUE HACE: imprime la lista de adyacencia (cada nodo y sus vecinos).
    ENTRADA : grafo.
    PROCESO : para cada nodo escribe sus vecinos, con el peso entre parentesis si el
              grafo es ponderado.
    SALIDA  : texto en pantalla.
    """
    print("\nLISTA DE ADYACENCIA:")
    for n in grafo.nodos():
        if grafo.es_ponderado():
            vec = ", ".join(f"{v}({formatear(grafo.ady[n][v])})" for v in grafo.vecinos(n))
        else:
            vec = ", ".join(grafo.vecinos(n))
        print(f"  {n} -> {vec if vec else '(sin conexiones salientes)'}")


def mostrar_grados_y_conexidad(grafo):
    """
    QUE HACE: muestra el grado de cada nodo y si el grafo es conexo.
    ENTRADA : grafo.
    PROCESO : usa grafo.grados() y grafo.componentes(). En no dirigidos verifica el
              lema del apreton de manos (suma de grados = 2 * aristas).
    SALIDA  : texto en pantalla (grados, comprobacion del lema y componentes).
    """
    print("\nGRADO DE CADA NODO:")
    gr = grafo.grados()
    for n in grafo.nodos():
        entrada, salida = gr[n]
        if grafo.dirigido:
            print(f"  {n}: sale {salida}, entra {entrada}")
        else:
            print(f"  {n}: {salida} conexiones")
    if not grafo.dirigido:
        suma = sum(s for _, s in gr.values())
        print(f"  Suma de grados = {suma} = 2 x {len(grafo.aristas())} aristas (apreton de manos)")
    comps = grafo.componentes()
    if len(comps) == 1:
        print("\nEl grafo es CONEXO (todos los nodos se alcanzan entre si).")
    else:
        print(f"\nEl grafo NO es conexo: tiene {len(comps)} componentes:")
        for c in comps:
            print("   ", ", ".join(c))


# ===================================================================
#  DIBUJO DEL GRAFO Y DE LA MATRIZ (MODO GRAFICO)
# ===================================================================
def dibujar(grafo, ruta=None, titulo="Grafo"):
    """
    QUE HACE: abre una ventana con el GRAFO (circulos = nodos, lineas o
              flechas = conexiones) y la MATRIZ DE ADYACENCIA al lado.
    ENTRADA : grafo y, opcionalmente, la ruta (lista de nodos) a resaltar.
    PROCESO : convierte el Grafo a networkx, calcula posiciones (circulo,
              o dos columnas si es bipartito), dibuja nodos, conexiones y
              pesos (solo si hay pesos) y pinta la mejor ruta de ROJO.
    SALIDA  : ventana grafica (se cierra para continuar el programa).
    EXPLICACION: networkx solo se usa aqui para calcular posiciones y dibujar; matplotlib
       muestra la ventana. Posiciones: circulo (<= 12 nodos), dos columnas si es bipartito,
       spring_layout si hay mas nodos.
    """
    G = nx.DiGraph() if grafo.dirigido else nx.Graph()
    for u in grafo.nodos():
        G.add_node(u)
    for u, v, p in grafo.aristas():
        G.add_edge(u, v, weight=formatear(p))

    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 7),
                                   gridspec_kw={"width_ratios": [3, 2]})
    fig.suptitle(titulo, fontsize=14, fontweight="bold")

    # --- posiciones de los nodos ---
    izq = grafo.izquierda
    if izq:
        pos = nx.bipartite_layout(G, nodes=[n for n in G if n in izq], align="vertical")
    elif len(G) <= 12:
        pos = nx.circular_layout(G)
    else:
        pos = nx.spring_layout(G, seed=7, k=1.2)

    tam = 700 + 180 * max(len(n) for n in G)            # circulo segun largo del nombre
    colores = ["#ffe0b3" if (izq and n not in izq) else "#cfe8ff" for n in G]
    # las flechas (y su curvatura) solo aplican a grafos dirigidos
    extra = {"arrowsize": 20, "connectionstyle": "arc3,rad=0.1"} if grafo.dirigido else {}

    nx.draw_networkx_edges(G, pos, edge_color="#888888", width=1.6, ax=ax1,
                           node_size=tam, arrows=grafo.dirigido, **extra)
    nx.draw_networkx_nodes(G, pos, node_color=colores, edgecolors="#1f4e79",
                           node_size=tam, ax=ax1)
    nx.draw_networkx_labels(G, pos, font_size=9, font_weight="bold", ax=ax1)
    if grafo.es_ponderado():
        nx.draw_networkx_edge_labels(G, pos, nx.get_edge_attributes(G, "weight"),
                                     font_size=9, ax=ax1)
    if ruta and len(ruta) > 1:                           # resaltar la mejor ruta
        nx.draw_networkx_edges(G, pos, edgelist=list(zip(ruta, ruta[1:])),
                               edge_color="red", width=4, ax=ax1, node_size=tam,
                               arrows=grafo.dirigido, **extra)
        nx.draw_networkx_nodes(G, pos, nodelist=ruta, node_color="#ffb3b3",
                               edgecolors="red", node_size=tam, ax=ax1)
    ax1.set_title("Grafo (la mejor ruta va en rojo)")
    ax1.axis("off")

    # --- matriz de adyacencia como tabla ---
    nombres, matriz = grafo.matriz_adyacencia()
    celdas = [[formatear(x) if x != "-" else "-" for x in fila] for fila in matriz]
    ax2.axis("off")
    tabla = ax2.table(cellText=celdas, rowLabels=nombres, colLabels=nombres,
                      loc="center", cellLoc="center")
    tabla.auto_set_font_size(False)
    tabla.set_fontsize(8)
    tabla.scale(1, 1.6)
    ax2.set_title("Matriz de adyacencia")

    plt.tight_layout()
    plt.show()


# ===================================================================
#  ANALISIS COMPLETO DE UN GRAFO
# ===================================================================
def resolver(grafo):
    """
    QUE HACE: con el grafo armado muestra TODOS los resultados.
    ENTRADA : grafo; luego se pide un nodo de inicio (recorridos) y un
              origen/destino (mejor ruta). ENTER usa el primer nodo.
    PROCESO : matriz, lista, grados, conectividad, BFS, DFS, Dijkstra,
              mejor ruta y dibujo.
    SALIDA  : resultados en consola + ventana grafica; devuelve
              (inicio, origen, destino) para el reporte HTML.
    """
    nombres = grafo.nodos()
    real = {sin_acentos(n): n for n in nombres}
    print("\nNodos del grafo:", ", ".join(nombres))
    mostrar_matriz(grafo)
    mostrar_lista(grafo)
    mostrar_grados_y_conexidad(grafo)

    def pedir_nodo(texto, defecto):
        """
        QUE HACE: pide un nodo y comprueba que exista.
        ENTRADA : texto de la pregunta y nodo por defecto (se usa con solo presionar ENTER).
        PROCESO : compara lo escrito sin acentos ni mayusculas con los nodos del grafo y
                  repite si no existe.
        SALIDA  : el nombre real del nodo.
        """
        while True:
            n = sin_acentos(input(f"{texto} (ENTER = {defecto}): ").strip())
            if n == "":
                return defecto
            if n in real:
                return real[n]
            print("   Ese nodo no existe. Opciones:", ", ".join(nombres))

    inicio = pedir_nodo("\nNodo de INICIO para los recorridos", nombres[0])
    print("\nRECORRIDO EN ANCHURA (BFS)     :", " -> ".join(grafo.bfs(inicio)))
    print("RECORRIDO EN PROFUNDIDAD (DFS) :", " -> ".join(grafo.dfs(inicio)))

    origen = pedir_nodo("\nMEJOR RUTA - nodo ORIGEN ", nombres[0])
    destino = pedir_nodo("MEJOR RUTA - nodo DESTINO", nombres[-1])
    ruta, costo = grafo.mejor_ruta(origen, destino)

    dist, _ = grafo.dijkstra(origen)
    unidad = "" if grafo.es_ponderado() else " conexiones"
    print(f"\nDISTANCIAS MINIMAS desde {origen}:")
    for n in nombres:
        print(f"   {origen} -> {n}: " + (f"{formatear(dist[n])}{unidad}" if dist[n] != INF else "sin ruta"))

    if ruta:
        print(f"\nMEJOR RUTA {origen} -> {destino}: {' -> '.join(ruta)}")
        print(f"COSTO TOTAL: {formatear(costo)}{unidad}")
    else:
        print(f"\nNo existe ruta de {origen} a {destino}.")

    print("\nAbriendo ventana grafica... (cierrela para continuar)")
    dibujar(grafo, ruta, f"Grafo - mejor ruta {origen} a {destino}")
    return inicio, origen, destino


# ===================================================================
#  MENU DE GRAFOS (se abre desde el menu principal)
# ===================================================================
def menu_grafos():
    """
    QUE HACE: muestra el menu de GRAFOS (problema completo, datos conocidos, ejemplo) y resuelve.
    MENU DE GRAFOS.
    ENTRADA : opcion elegida (1, 2, 3 o 0).
    PROCESO : arma el grafo segun el modo elegido y llama a resolver().
    SALIDA  : vuelve al menu principal con la opcion 0.
    """
    while True:
        print("\n========== GRAFOS ==========")
        print("1. Escribir el PROBLEMA COMPLETO (el programa lo interpreta)")
        print("2. Ingresar DATOS CONOCIDOS")
        print("3. Usar un EJEMPLO")
        print("0. Volver al menu principal")
        op = input("Opcion: ").strip()
        if op == "1":
            g = modo_problema_completo()
        elif op == "2":
            g = modo_datos_conocidos()
        elif op == "3":
            g = ejemplo_precargado()
        elif op == "0":
            return
        else:
            print("Opcion no valida.")
            continue
        if g is None or len(g.ady) < 2:
            print("No hay suficientes datos para armar el grafo.")
            continue
        datos = resolver(g)
        if pedir_si_no("Guardar el reporte en HTML y abrirlo en el navegador?"):
            reporte_grafo_html(g, *datos)


# ===================================================================
#  ARBOLES (punto 6): recorridos PREORDEN, INORDEN y POSTORDEN
# ===================================================================
# Palabras que se ignoran al leer el problema de un arbol
RELLENO_ARBOL = PALABRAS_RELLENO | {
    "de", "del", "tiene", "tienen", "como", "arbol", "binario", "raiz", "nodo",
    "nodos", "insertar", "inserte", "valores", "valor", "numeros", "numero",
    "elementos", "elemento", "orden", "siguiente", "busqueda", "dato", "datos",
    "lo", "si", "no", "hay", "lado"}
# Palabras que indican "el nodo anterior es PADRE de los siguientes"
CONECTORES_ARBOL = {"hijo", "hijos", "padre", "con"}


def normalizar_valor(v):
    """
    QUE HACE: unifica como se escribe un valor (4.0 -> "4"; el texto no cambia).
    ENTRADA : valor escrito por la persona.
    PROCESO : intenta convertirlo a numero y formatearlo; si no es numero lo deja igual.
    SALIDA  : texto.
    """
    try:
        return str(formatear(float(v)))
    except ValueError:
        return str(v)


def clave_valor(v):
    """
    QUE HACE: crea la clave para COMPARAR valores en el arbol de busqueda.
    ENTRADA : valor (texto).
    PROCESO : los numeros se comparan como numeros y el texto en orden alfabetico
              natural; los numeros van antes que el texto.
    SALIDA  : tupla comparable con < y ==.
    """
    try:
        return (0, float(v), [])
    except ValueError:
        return (1, 0.0, clave_natural(v))


class Nodo:
    """
    QUE ES: un nodo del arbol binario: guarda un valor y sus hijos izquierdo y derecho.
    ENTRADA : valor del nodo (en __init__).
    PROCESO : izq y der empiezan en None (= sin hijo).
    SALIDA  : objeto Nodo.
    """

    def __init__(self, valor):
        """
        QUE HACE: crea un nodo.
        ENTRADA : valor.
        PROCESO : guarda el valor y deja los dos hijos en None.
        SALIDA  : nodo listo para enlazarse en el arbol.
        """
        self.valor = valor
        self.izq = None
        self.der = None


class Arbol:
    """
    QUE ES: un ARBOL BINARIO (cada nodo tiene como maximo 2 hijos) y sus recorridos.
    METODOS: insertar, preorden, inorden, postorden, por_niveles, lista_nodos, altura,
       posiciones.
    PROBLEMAS MATEMATICOS QUE RESUELVE: insercion en arbol de busqueda, recorridos
       PREORDEN / INORDEN / POSTORDEN / por niveles, altura y conteo de nodos y hojas.
    MATEMATICA: un arbol es un grafo conexo sin ciclos, por eso aristas = nodos - 1.
    """
    def __init__(self, es_abb=False):
        """
        QUE HACE: crea un arbol binario vacio.
        ENTRADA : es_abb (True si se arma como ARBOL BINARIO DE BUSQUEDA).
        PROCESO : guarda la raiz (None = arbol vacio).
        SALIDA  : objeto Arbol.
        """
        self.raiz = None
        self.es_abb = es_abb

    # ---------------------------------------------------------------
    def insertar(self, valor):
        """
        QUE HACE: inserta un valor siguiendo la regla del arbol de busqueda.
        ENTRADA : valor a insertar.
        PROCESO : desde la raiz, si el valor es MENOR se baja por la izquierda y si es MAYOR
                  por la derecha, hasta encontrar un lugar vacio donde se coloca el nodo nuevo.
        SALIDA  : True si se inserto, False si el valor ya existia (no se permiten repetidos).
        MATEMATICA: costo O(altura): O(log n) si el arbol esta balanceado, O(n) en el peor caso.
        """
        nuevo = Nodo(valor)
        if self.raiz is None:
            self.raiz = nuevo
            return True
        k = clave_valor(valor)
        actual = self.raiz
        while True:
            kc = clave_valor(actual.valor)
            if k == kc:
                return False
            if k < kc:
                if actual.izq is None:
                    actual.izq = nuevo
                    return True
                actual = actual.izq
            else:
                if actual.der is None:
                    actual.der = nuevo
                    return True
                actual = actual.der

    # ---------------------------------------------------------------
    def preorden(self):
        """
        QUE HACE: recorre el arbol en PREORDEN y devuelve el orden de visita.
        RECORRIDO PREORDEN: RAIZ -> izquierdo -> derecho.
        ENTRADA : ninguna (usa el arbol).
        PROCESO : recursivo; primero se anota el nodo y luego se recorre su hijo izquierdo y
                  despues el derecho.
        SALIDA  : lista de valores en el orden de visita.
        MATEMATICA: costo O(n), cada nodo se visita una vez. En un arbol de expresion da la
                  notacion PREFIJA.
        """
        res = []

        def rec(n):
            """
            QUE HACE: recorre un subarbol en preorden.
            ENTRADA : nodo (puede ser None).
            PROCESO : si existe, anota su valor y recorre el hijo izquierdo y luego el derecho.
            SALIDA  : ninguna (llena la lista 'res').
            """
            if n is None:
                return
            res.append(n.valor)
            rec(n.izq)
            rec(n.der)

        rec(self.raiz)
        return res

    def inorden(self):
        """
        QUE HACE: recorre el arbol en INORDEN y devuelve el orden de visita.
        RECORRIDO INORDEN: izquierdo -> RAIZ -> derecho.
        ENTRADA : ninguna (usa el arbol).
        PROCESO : recursivo; primero se recorre todo el hijo izquierdo, luego se anota el nodo
                  y al final se recorre el hijo derecho.
        SALIDA  : lista de valores en el orden de visita.
        MATEMATICA: costo O(n). En un arbol de busqueda entrega los valores ORDENADOS; en un
                  arbol de expresion da la notacion INFIJA.
        """
        res = []

        def rec(n):
            """
            QUE HACE: recorre un subarbol en inorden.
            ENTRADA : nodo (puede ser None).
            PROCESO : recorre el hijo izquierdo, anota el valor del nodo y recorre el derecho.
            SALIDA  : ninguna (llena la lista 'res').
            """
            if n is None:
                return
            rec(n.izq)
            res.append(n.valor)
            rec(n.der)

        rec(self.raiz)
        return res

    def postorden(self):
        """
        QUE HACE: recorre el arbol en POSTORDEN y devuelve el orden de visita.
        RECORRIDO POSTORDEN: izquierdo -> derecho -> RAIZ.
        ENTRADA : ninguna (usa el arbol).
        PROCESO : recursivo; cada nodo se anota DESPUES de recorrer sus dos hijos.
        SALIDA  : lista de valores en el orden de visita.
        MATEMATICA: costo O(n). En un arbol de expresion da la notacion POSFIJA.
        """
        res = []

        def rec(n):
            """
            QUE HACE: recorre un subarbol en postorden.
            ENTRADA : nodo (puede ser None).
            PROCESO : recorre el hijo izquierdo y el derecho y al final anota el valor del nodo.
            SALIDA  : ninguna (llena la lista 'res').
            """
            if n is None:
                return
            rec(n.izq)
            rec(n.der)
            res.append(n.valor)

        rec(self.raiz)
        return res

    def por_niveles(self):
        """
        QUE HACE: recorre el arbol por NIVELES y devuelve el orden de visita.
        RECORRIDO POR NIVELES (en anchura), igual que el BFS de los grafos.
        ENTRADA : ninguna (usa el arbol).
        PROCESO : mete la raiz en una COLA; saca el primero, lo anota y mete sus hijos
                  (izquierdo y luego derecho); repite hasta vaciar la cola.
        SALIDA  : lista de valores nivel por nivel, de izquierda a derecha.
        MATEMATICA: costo O(n).
        """
        res, cola = [], deque([self.raiz] if self.raiz else [])
        while cola:
            n = cola.popleft()
            res.append(n.valor)
            for h in (n.izq, n.der):
                if h:
                    cola.append(h)
        return res

    # ---------------------------------------------------------------
    def lista_nodos(self):
        """
        QUE HACE: devuelve todos los objetos Nodo del arbol.
        ENTRADA : ninguna (usa el arbol).
        PROCESO : recorrido en preorden con una PILA (sin recursion).
        SALIDA  : lista de Nodo (sirve para contar nodos, hojas y dibujar las lineas).
        """
        res, pila = [], [self.raiz] if self.raiz else []
        while pila:
            n = pila.pop()
            res.append(n)
            for h in (n.der, n.izq):
                if h:
                    pila.append(h)
        return res

    def altura(self):
        """
        QUE HACE: calcula la ALTURA = aristas del camino mas largo desde la raiz hasta
                  una hoja (un arbol de 1 nodo tiene altura 0).
        ENTRADA : ninguna (usa el arbol).
        PROCESO : recursivo: altura(nodo) = 1 + max(altura(izq), altura(der)); un arbol
                  vacio vale -1.
        SALIDA  : numero entero.
        """
        def rec(n):
            """
            QUE HACE: calcula la altura de un subarbol.
            ENTRADA : nodo (None = arbol vacio).
            PROCESO : un arbol vacio vale -1; si no, 1 + el maximo de las alturas de sus hijos.
            SALIDA  : numero entero.
            """
            return -1 if n is None else 1 + max(rec(n.izq), rec(n.der))
        return rec(self.raiz)

    def posiciones(self):
        """
        QUE HACE: calcula donde dibujar cada nodo.
        ENTRADA : ninguna (usa el arbol).
        PROCESO : x = posicion del nodo en el recorrido INORDEN (asi los nodos no se
                  encimen); y = -profundidad (la raiz queda arriba).
        SALIDA  : diccionario valor -> (x, y).
        """
        pos, cont = {}, [0]

        def rec(n, prof):
            """
            QUE HACE: calcula las posiciones (x, y) de un subarbol.
            ENTRADA : nodo y su profundidad.
            PROCESO : recorre en inorden; x aumenta de 1 en 1 en ese orden y y = -profundidad.
            SALIDA  : ninguna (llena el diccionario 'pos').
            """
            if n is None:
                return
            rec(n.izq, prof + 1)
            pos[n.valor] = (cont[0], -prof)
            cont[0] += 1
            rec(n.der, prof + 1)

        rec(self.raiz, 0)
        return pos


# ===================================================================
#  ARBOLES: ARMAR EL ARBOL A PARTIR DE LOS DATOS
# ===================================================================
def armar_abb(valores):
    """
    QUE HACE: arma un ARBOL BINARIO DE BUSQUEDA insertando los valores en el orden dado.
    ENTRADA : lista de valores (numeros o texto).
    PROCESO : normaliza cada valor y lo inserta con Arbol.insertar; los repetidos se
              ignoran y se anotan.
    SALIDA  : (arbol, lista de valores repetidos que se ignoraron).
    """
    a, repetidos = Arbol(es_abb=True), []
    for v in valores:
        v = normalizar_valor(v)
        if not a.insertar(v):
            repetidos.append(v)
    return a, repetidos


def armar_arbol_relaciones(pares):
    """
    QUE HACE: arma el arbol a partir de relaciones PADRE -> HIJO.
    ENTRADA : lista de (padre, hijo, lado) con lado 'L' (izquierdo),
              'R' (derecho) o None (se acomoda: primero izquierdo).
    PROCESO : valida que cada nodo tenga un solo padre, maximo 2 hijos,
              una sola raiz (nodo sin padre) y que no haya ciclos.
    SALIDA  : objeto Arbol. Si hay un error lanza ValueError con el motivo.
    MATEMATICA: comprueba las propiedades de un arbol binario: cada nodo (menos la raiz)
       tiene exactamente 1 padre, maximo 2 hijos, hay una sola raiz y no hay ciclos
       (todos los nodos se alcanzan desde la raiz).
    """
    nombres, padre_de, hijos = [], {}, {}
    for p, h, l in pares:
        for n in (p, h):
            if n not in nombres:
                nombres.append(n)
        if h in padre_de:
            if padre_de[h] != p:
                raise ValueError(f"{h} tiene dos padres ({padre_de[h]} y {p}). "
                                 "En un arbol cada nodo tiene un solo padre.")
            continue                                      # relacion repetida
        padre_de[h] = p
        hijos.setdefault(p, []).append((h, l))
    raices = [n for n in nombres if n not in padre_de]
    if len(raices) != 1:
        raise ValueError("Un arbol debe tener una sola raiz (nodo sin padre). Encontre: "
                         + (", ".join(raices) if raices else "ninguna (hay un ciclo)"))
    nodos = {n: Nodo(n) for n in nombres}
    for p, lista in hijos.items():
        if len(lista) > 2:
            raise ValueError(f"{p} tiene {len(lista)} hijos; un arbol BINARIO permite maximo 2.")
        izq = der = None
        for h, l in lista:                                # primero los lados indicados
            if l == "L":
                if izq:
                    raise ValueError(f"{p} tiene dos hijos izquierdos.")
                izq = h
            elif l == "R":
                if der:
                    raise ValueError(f"{p} tiene dos hijos derechos.")
                der = h
        for h, l in lista:                                # luego los que no indican lado
            if l is None:
                if izq is None:
                    izq = h
                else:
                    der = h
        nodos[p].izq = nodos[izq] if izq else None
        nodos[p].der = nodos[der] if der else None
    arbol = Arbol()
    arbol.raiz = nodos[raices[0]]
    if len(arbol.lista_nodos()) != len(nombres):
        raise ValueError("Hay nodos que no se alcanzan desde la raiz (revise las relaciones).")
    return arbol


def interpretar_arbol_texto(texto):
    """
    QUE HACE: interpreta un problema de arboles escrito en lenguaje natural.
    ENTRADA : texto, por ejemplo
              "Insertar 50, 30, 70, 20"
              "A tiene hijos B y C. B tiene hijos D y E. C tiene hijo derecho F."
              "D es hijo izquierdo de B"
    PROCESO : 1) "X es hijo de Y" se convierte en "Y tiene hijo X".
              2) Si aparece la palabra hijo/hijos/padre se leen RELACIONES:
                 el ultimo nombre antes de la palabra es el padre y los
                 siguientes son sus hijos (izquierdo / derecho si se indica).
              3) Si no, todos los valores se insertan en un ARBOL DE BUSQUEDA.
    SALIDA  : ("abb", [valores])  o  ("rel", [(padre, hijo, lado), ...])
    """
    texto = re.sub(r"(\w+)\s+es\s+hij[oa]\s*(izquierd[oa]|derech[oa])?\s+de\s+(\w+)",
                   r"\3 tiene hijo \2 \1", texto, flags=re.IGNORECASE)
    palabras = re.findall(r"-?\d+(?:\.\d+)?|\w+", texto)
    letras = [p for p in palabras if len(p) == 1 and p.isalpha() and p.isupper()]
    usa_letras = any(l not in "YEAOU" for l in letras)

    def es_relleno(pal):
        """
        QUE HACE: decide si una palabra se ignora (no es un nodo ni un valor).
        ENTRADA : palabra.
        PROCESO : es relleno si esta en RELLENO_ARBOL o en PALABRAS_RELACION, salvo una letra
                  mayuscula suelta cuando el problema usa letras como nodos (A, B, C...).
        SALIDA  : True / False.
        """
        letra_nodo = usa_letras and len(pal) == 1 and pal.isalpha() and pal.isupper()
        k = sin_acentos(pal)
        return (k in RELLENO_ARBOL or k in PALABRAS_RELACION) and not letra_nodo

    relaciones = any(sin_acentos(p) in ("hijo", "hijos", "padre") for p in palabras)
    if not relaciones:
        return "abb", [normalizar_valor(p) for p in palabras if not es_relleno(p)]

    pares, sujeto, pendiente, lado = [], None, [], None

    def guardar(suj, hijos):
        """
        QUE HACE: guarda las relaciones padre -> hijo del sujeto actual.
        ENTRADA : sujeto (padre) y lista de (hijo, lado).
        PROCESO : agrega (padre, hijo, lado) por cada hijo, sin lazos a si mismo.
        SALIDA  : ninguna (agrega a la lista 'pares').
        """
        if suj is not None:
            pares.extend((suj, h, l) for h, l in hijos if h != suj)

    for pal in palabras:
        k = sin_acentos(pal)
        if k in ("izquierdo", "izquierda", "izq"):
            lado = "L"
        elif k in ("derecho", "derecha", "der"):
            lado = "R"
        elif k in CONECTORES_ARBOL:
            if pendiente:
                nuevo = pendiente.pop()
                guardar(sujeto, pendiente)
                sujeto, pendiente = nuevo[0], []
        elif not es_relleno(pal):
            pendiente.append((normalizar_valor(pal), lado))
            lado = None
    guardar(sujeto, pendiente)
    return "rel", pares


# ===================================================================
#  ARBOLES: PRESENTACION EN CONSOLA
# ===================================================================
def texto_arbol(arbol):
    """
    QUE HACE: dibuja el arbol con texto, girado 90 grados.
    ENTRADA : arbol.
    PROCESO : recorrido recursivo "derecho, nodo, izquierdo"; la raiz queda a la izquierda,
              arriba van los hijos DERECHOS y abajo los IZQUIERDOS; cada nivel se
              sangra 6 espacios.
    SALIDA  : texto de varias lineas.
    """
    lineas = []

    def rec(n, nivel, rama):
        """
        QUE HACE: agrega a 'lineas' el subarbol de un nodo.
        ENTRADA : nodo, nivel (profundidad) y etiqueta de rama ("(izq) " o "(der) ").
        PROCESO : primero el hijo derecho, luego el nodo con su sangria y al final el izquierdo.
        SALIDA  : ninguna (llena la lista 'lineas').
        """
        if n is None:
            return
        rec(n.der, nivel + 1, "(der) ")
        lineas.append("      " * nivel + rama + str(n.valor))
        rec(n.izq, nivel + 1, "(izq) ")

    rec(arbol.raiz, 0, "")
    return "\n".join(lineas)


def estadisticas_arbol(arbol):
    """
    QUE HACE: calcula los datos matematicos del arbol.
    ENTRADA : arbol.
    PROCESO : cuenta los nodos, cuenta las hojas (nodos sin hijos) y calcula la altura.
    SALIDA  : (nodos, hojas, altura). Se cumple: aristas = nodos - 1.
    """
    nodos = arbol.lista_nodos()
    hojas = sum(1 for n in nodos if n.izq is None and n.der is None)
    return len(nodos), hojas, arbol.altura()


def mostrar_arbol(arbol):
    """
    QUE HACE: muestra como entendio el programa el arbol (para verificarlo).
    ENTRADA : arbol.
    PROCESO : escribe el tipo (binario o de busqueda), la raiz, nodos, hojas, altura y
              el arbol en texto.
    SALIDA  : texto en pantalla.
    """
    n, hojas, alt = estadisticas_arbol(arbol)
    tipo = "ARBOL BINARIO DE BUSQUEDA" if arbol.es_abb else "ARBOL BINARIO"
    print(f"\n{tipo}: raiz = {arbol.raiz.valor}, {n} nodos, {hojas} hojas, altura {alt}.")
    print("(la raiz esta a la izquierda; arriba los hijos derechos, abajo los izquierdos)\n")
    print(texto_arbol(arbol))


# ===================================================================
#  ARBOLES: OPCION 1 - PROBLEMA COMPLETO
# ===================================================================
def modo_problema_completo_arbol():
    """
    QUE HACE: lee el problema de arboles escrito por la persona y lo convierte en un Arbol.
    OPCION 1 - MODO PROBLEMA COMPLETO (arboles).
    ENTRADA : la persona escribe el problema (varias lineas) y termina con
              una linea vacia.
    PROCESO : interpretar_arbol_texto() lo convierte en valores (arbol de
              busqueda) o en relaciones padre -> hijos; se arma el arbol,
              se muestra y se pide confirmacion.
    SALIDA  : objeto Arbol, o None si no se escribio nada.
    """
    print("\n--- MODO PROBLEMA COMPLETO (ARBOLES) ---")
    print("Escriba SOLO los datos del problema, por ejemplo:")
    print("   Insertar 50, 30, 70, 20, 40, 60, 80          (arbol de busqueda)")
    print("   A tiene hijos B y C. B tiene hijos D y E. C tiene hijo derecho F.")
    print("   D es hijo izquierdo de B")
    print("Al terminar presione ENTER en una linea vacia.\n")
    while True:
        lineas = []
        while True:
            linea = input("  > ").strip()
            if linea == "":
                break
            lineas.append(linea)
        if not lineas:
            return None
        tipo, datos = interpretar_arbol_texto("\n".join(lineas))
        try:
            if tipo == "abb":
                if len(datos) < 2:
                    raise ValueError("Necesito al menos 2 valores.")
                arbol, repetidos = armar_abb(datos)
                if repetidos:
                    print("Valores repetidos (se ignoraron):", ", ".join(repetidos))
            else:
                arbol = armar_arbol_relaciones(datos)
        except ValueError as e:
            print(f"No pude armar el arbol: {e}\nIntente de nuevo.\n")
            continue
        mostrar_arbol(arbol)
        if pedir_si_no("Esta bien interpretado el problema?"):
            return arbol
        print("\nEscriba el problema de nuevo (ENTER vacio para cancelar):")


# ===================================================================
#  ARBOLES: OPCION 2 - DATOS CONOCIDOS
# ===================================================================
def modo_datos_conocidos_arbol():
    """
    QUE HACE: arma un Arbol con datos ya conocidos (valores o conexiones padre-hijos).
    OPCION 2 - MODO DATOS CONOCIDOS (arboles).
    ENTRADA : 1) una lista de VALORES (se arma un arbol de busqueda), o
              2) conexiones PADRE HIJO_IZQ HIJO_DER, una por linea
                 (use "-" cuando no hay hijo en ese lado).
    PROCESO : valida los datos y arma el arbol.
    SALIDA  : objeto Arbol, o None si hubo un error.
    """
    print("\n--- MODO DATOS CONOCIDOS (ARBOLES) ---")
    print("1. Tengo una lista de VALORES (se arma un arbol de busqueda)")
    print("2. Tengo las conexiones PADRE -> HIJOS")
    while True:
        op = input("Opcion: ").strip()
        if op in ("1", "2"):
            break
        print("   Escriba 1 o 2.")
    try:
        if op == "1":
            entrada = input("Valores en el orden de insercion (separados por coma o espacio): ")
            valores = [p for p in re.split(r"[,;\s]+", entrada.strip()) if p]
            if len(valores) < 2:
                raise ValueError("Necesito al menos 2 valores.")
            arbol, repetidos = armar_abb(valores)
            if repetidos:
                print("Valores repetidos (se ignoraron):", ", ".join(repetidos))
        else:
            print("\nEscriba cada conexion:  PADRE HIJO_IZQUIERDO HIJO_DERECHO")
            print("Ejemplos:  A B C    |    B D -    |    C - F      ('-' = sin hijo)")
            print("Cuando termine presione ENTER en una linea vacia.")
            pares = []
            while True:
                linea = input("  > ").strip()
                if linea == "":
                    break
                p = [x for x in re.split(r"[,;\s]+", linea) if x]
                if len(p) < 2 or len(p) > 3:
                    print("    Use: PADRE HIJO_IZQUIERDO HIJO_DERECHO")
                    continue
                for lado, h in zip("LR", p[1:]):
                    if h != "-":
                        pares.append((normalizar_valor(p[0]), normalizar_valor(h), lado))
            arbol = armar_arbol_relaciones(pares)
    except ValueError as e:
        print(f"No pude armar el arbol: {e}")
        return None
    mostrar_arbol(arbol)
    return arbol


# ===================================================================
#  ARBOLES: OPCION 3 - EJEMPLOS
# ===================================================================
def ejemplo_precargado_arbol():
    """
    QUE HACE: arma un Arbol a partir de uno de los 3 ejemplos.
    OPCION 3 - EJEMPLOS (arboles).
    ENTRADA : numero del ejemplo (1 a 3).
    PROCESO : arma el arbol del ejemplo elegido.
        1) Arbol binario de busqueda con valores numericos.
        2) Arbol escrito con relaciones padre -> hijos (lenguaje natural).
        3) Arbol de EXPRESION ((8 + 2) * (9 - 4)): sus recorridos dan las
           notaciones PREFIJA (preorden), INFIJA (inorden) y POSFIJA (postorden).
    SALIDA  : objeto Arbol, o None si elige volver.
    """
    print("\n--- EJEMPLOS (ARBOLES) ---")
    print("1. Arbol binario de busqueda (valores 50, 30, 70, 20, 40, 60, 80, 65)")
    print("2. Arbol por relaciones (A tiene hijos B y C, ...)")
    print("3. Arbol de expresion aritmetica ((8 + 2) * (9 - 4))")
    print("0. Volver")
    while True:
        op = input("Ejemplo: ").strip()
        if op == "0":
            return None
        if op == "1":
            arbol, _ = armar_abb("50 30 70 20 40 60 80 65".split())
            print("\nPROBLEMA: insertar 50, 30, 70, 20, 40, 60, 80, 65 en un arbol de busqueda.")
        elif op == "2":
            texto = ("A tiene hijos B y C. B tiene hijos D y E. "
                     "C tiene hijo derecho F. E tiene hijo izquierdo G.")
            print(f"\nPROBLEMA: {texto}")
            arbol = armar_arbol_relaciones(interpretar_arbol_texto(texto)[1])
        elif op == "3":
            print("\nPROBLEMA: arbol de la expresion ((8 + 2) * (9 - 4)).")
            arbol = armar_arbol_relaciones([("*", "+", "L"), ("*", "-", "R"), ("+", "8", "L"),
                                            ("+", "2", "R"), ("-", "9", "L"), ("-", "4", "R")])
        else:
            print("   Opcion no valida.")
            continue
        mostrar_arbol(arbol)
        return arbol


# ===================================================================
#  ARBOLES: DIBUJO (MODO GRAFICO)
# ===================================================================
def dibujar_arbol(arbol, titulo="Arbol"):
    """
    QUE HACE: abre una ventana con el ARBOL dibujado 3 veces, cada vez con
              el ORDEN DE VISITA de un recorrido (numeros rojos).
    ENTRADA : arbol y titulo.
    PROCESO : circulos = nodos, lineas = conexiones padre-hijo; los
              numeros en rojo indican en que lugar se visita cada nodo
              en PREORDEN, INORDEN y POSTORDEN.
    SALIDA  : ventana grafica (se cierra para continuar el programa).
    EXPLICACION: solo usa matplotlib. Las posiciones salen de Arbol.posiciones() y el numero
       rojo de cada nodo es su orden de visita, para ver la diferencia entre los 3 recorridos.
    """
    pos = arbol.posiciones()
    n = len(pos)
    prof = arbol.altura()
    recorridos = [("PREORDEN (raíz - izq - der)", arbol.preorden()),
                  ("INORDEN (izq - raíz - der)", arbol.inorden()),
                  ("POSTORDEN (izq - der - raíz)", arbol.postorden())]
    fig, axs = plt.subplots(1, 3, figsize=(17, 6))
    fig.suptitle(titulo, fontsize=14, fontweight="bold")
    for ax, (nombre, orden) in zip(axs, recorridos):
        rango = {v: i + 1 for i, v in enumerate(orden)}
        for nodo in arbol.lista_nodos():              # lineas padre-hijo
            for h in (nodo.izq, nodo.der):
                if h:
                    (x1, y1), (x2, y2) = pos[nodo.valor], pos[h.valor]
                    ax.plot([x1, x2], [y1, y2], color="#888888", linewidth=1.6, zorder=1)
        for valor, (x, y) in pos.items():             # circulos y numeros
            ax.scatter([x], [y], s=900, c="#cfe8ff", edgecolors="#1f4e79", zorder=2)
            ax.text(x, y, str(valor), ha="center", va="center", fontweight="bold", zorder=3)
            ax.text(x + 0.28, y + 0.28, str(rango[valor]), color="red", fontsize=11,
                    fontweight="bold", zorder=4)
        ax.set_title(nombre)
        ax.set_xlabel(" → ".join(map(str, orden)), fontsize=9, wrap=True)
        ax.set_xlim(-1, n)
        ax.set_ylim(-prof - 0.8, 0.8)
        ax.set_xticks([])
        ax.set_yticks([])
        for lado in ax.spines.values():
            lado.set_visible(False)
    plt.tight_layout()
    plt.show()


# ===================================================================
#  ARBOLES: ANALISIS COMPLETO
# ===================================================================
def resolver_arbol(arbol):
    """
    QUE HACE: con el arbol armado muestra TODOS los resultados.
    ENTRADA : arbol.
    PROCESO : datos del arbol (nodos, hojas, altura), recorridos
              preorden, inorden, postorden y por niveles, y el dibujo.
    SALIDA  : resultados en consola + ventana grafica.
    """
    n, hojas, alt = estadisticas_arbol(arbol)
    print(f"\nNODOS: {n}   HOJAS: {hojas}   NODOS INTERNOS: {n - hojas}   "
          f"ALTURA: {alt}   ARISTAS: {n - 1} (= nodos - 1)")
    print("\nRECORRIDO PREORDEN   (raiz, izquierdo, derecho):", " -> ".join(arbol.preorden()))
    print("RECORRIDO INORDEN    (izquierdo, raiz, derecho):", " -> ".join(arbol.inorden()))
    print("RECORRIDO POSTORDEN  (izquierdo, derecho, raiz):", " -> ".join(arbol.postorden()))
    print("RECORRIDO POR NIVELES (anchura)                :", " -> ".join(arbol.por_niveles()))
    if arbol.es_abb:
        print("\nEn un arbol de busqueda el INORDEN entrega los valores ORDENADOS.")
    print("\nAbriendo ventana grafica... (cierrela para continuar)")
    dibujar_arbol(arbol, "Árbol binario de búsqueda" if arbol.es_abb else "Árbol binario")


# ===================================================================
#  REPORTE EN HTML (se guarda y se abre en el navegador)
# ===================================================================
PLANTILLA_HTML = """<!DOCTYPE html>
<html lang="es"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>%TITULO%</title>
<style>
:root{--bg:#f4f1ea;--fg:#222;--card:#fff;--mut:#666;--bd:#ddd;--nodo:#cfe8ff;--acc:#3b6fb6}
@media (prefers-color-scheme:dark){:root{--bg:#1e1f22;--fg:#eee;--card:#2a2c30;--mut:#aaa;--bd:#444;--nodo:#35557a;--acc:#6aa0e8}}
body{margin:0;padding:18px;background:var(--bg);color:var(--fg);font-family:system-ui,"Segoe UI",sans-serif}
.w{max-width:960px;margin:auto}h1{margin:6px 0 2px}h2{font-size:1.1rem;margin:0 0 8px}
.c{background:var(--card);border:1px solid var(--bd);border-radius:12px;padding:14px;margin:12px 0;overflow-x:auto}
.m{color:var(--mut)}table{border-collapse:collapse}td,th{border:1px solid var(--bd);padding:4px 9px;text-align:center}
th{background:var(--bd)}pre{margin:0;font-size:.95rem}.r{color:#d22;font-weight:700}
svg{max-width:100%;height:auto}.e{stroke:var(--mut);stroke-width:1.8;fill:none}.er{stroke:#d22;stroke-width:4;fill:none}
.nd{fill:var(--nodo);stroke:var(--acc);stroke-width:2}.nr{fill:#ffb3b3;stroke:#d22;stroke-width:2.5}
.tx{fill:var(--fg);font:bold 13px system-ui,sans-serif;text-anchor:middle;dominant-baseline:central}
.pe{fill:var(--mut);font:12px system-ui,sans-serif;text-anchor:middle;dominant-baseline:central}
.bd{fill:#d22}.bt{fill:#fff;font:bold 11px system-ui,sans-serif;text-anchor:middle;dominant-baseline:central}
.f{display:flex;flex-wrap:wrap;gap:12px}.f>div{flex:1;min-width:260px;text-align:center}
</style></head><body><div class="w">
<h1>%TITULO%</h1><p class="m">Reporte generado por el programa de Python (Matemática Discreta).</p>
%CUERPO%
</div></body></html>"""


def guardar_y_abrir_html(nombre, titulo, cuerpo):
    """
    QUE HACE: guarda el reporte como archivo .html y lo abre en el navegador.
    ENTRADA : nombre del archivo, titulo de la pagina y el cuerpo en HTML.
    PROCESO : escribe el archivo junto a este programa (o en la carpeta
              actual si no se puede) y lo abre con el navegador.
    SALIDA  : ruta del archivo guardado (se imprime en consola).
    """
    pagina = PLANTILLA_HTML.replace("%TITULO%", html.escape(titulo)).replace("%CUERPO%", cuerpo)
    for carpeta in (os.path.dirname(os.path.abspath(__file__)), os.getcwd()):
        ruta = os.path.join(carpeta, nombre)
        try:
            with open(ruta, "w", encoding="utf-8") as f:
                f.write(pagina)
            break
        except OSError:
            ruta = None
    if ruta is None:
        print("No pude guardar el archivo HTML.")
        return None
    print(f"\nReporte guardado en: {ruta}")
    webbrowser.open(Path(ruta).as_uri())
    return ruta


def tabla_html(cabecera, filas):
    """
    QUE HACE: arma una tabla HTML con fila y columna de titulos (la matriz del reporte).
    ENTRADA : lista de titulos y lista de filas.
    PROCESO : escapa el texto con html.escape y arma <table>, <tr>, <th> y <td>.
    SALIDA  : texto HTML.
    """
    e = html.escape
    t = "<table><tr><th></th>" + "".join(f"<th>{e(str(c))}</th>" for c in cabecera) + "</tr>"
    for nombre, fila in zip(cabecera, filas):
        t += f"<tr><th>{e(str(nombre))}</th>" + "".join(f"<td>{e(str(x))}</td>" for x in fila) + "</tr>"
    return t + "</table>"


def svg_grafo(grafo, ruta=None):
    """
    QUE HACE: dibuja el grafo como imagen SVG (para el reporte HTML).
    ENTRADA : grafo y, opcionalmente, la ruta (lista de nodos) a resaltar.
    PROCESO : posiciona los nodos en circulo (o en 2 columnas si es bipartito) con seno
              y coseno: angulo = 2*pi*k/n; dibuja lineas o flechas por conexion, los
              pesos si los hay, y la mejor ruta en rojo.
    SALIDA  : texto SVG.
    MATEMATICA: coordenadas polares (x = cx + R*cos(a), y = cy + R*sin(a)).
    """
    e = html.escape
    nodos = grafo.nodos()
    n, W = len(nodos), 580
    r = min(46, 14 + 4 * max(len(x) for x in nodos))
    pos = {}
    if grafo.izquierda:
        izqs = [x for x in nodos if x in grafo.izquierda]
        ders = [x for x in nodos if x not in grafo.izquierda]
        for col, lista in ((0.16, izqs), (0.84, ders)):
            for k, x in enumerate(lista):
                pos[x] = (W * col, W * (k + 1) / (len(lista) + 1))
    else:
        rad = W / 2 - r - 20
        for k, x in enumerate(nodos):
            ang = 2 * math.pi * k / n - math.pi / 2
            pos[x] = (W / 2 + rad * math.cos(ang), W / 2 + rad * math.sin(ang))
    en_ruta = set(zip(ruta, ruta[1:])) if ruta else set()
    if not grafo.dirigido:
        en_ruta |= {(b, a) for a, b in en_ruta}

    def trazo(u, v):
        """
        QUE HACE: calcula el trazo de una arista entre dos nodos.
        ENTRADA : nodos u y v.
        PROCESO : toma el vector unitario de u a v y acorta los extremos el radio del
                  circulo para que la linea no entre al nodo; si es dirigido usa una curva
                  (Bezier cuadratica) para que ida y vuelta no se tapen.
        SALIDA  : (texto del trazo SVG, (x, y) del punto medio para el peso).
        """
        x1, y1 = pos[u]
        x2, y2 = pos[v]
        d = math.hypot(x2 - x1, y2 - y1) or 1
        ux, uy = (x2 - x1) / d, (y2 - y1) / d
        ax, ay = x1 + ux * r, y1 + uy * r
        extra = 3 if grafo.dirigido else 0
        bx, by = x2 - ux * (r + extra), y2 - uy * (r + extra)
        if grafo.dirigido:                                  # curva suave (ida y vuelta no se tapan)
            cx, cy = (ax + bx) / 2 - uy * 16, (ay + by) / 2 + ux * 16
            return f"M{ax:.1f},{ay:.1f} Q{cx:.1f},{cy:.1f} {bx:.1f},{by:.1f}", (
                0.25 * ax + 0.5 * cx + 0.25 * bx, 0.25 * ay + 0.5 * cy + 0.25 * by)
        return f"M{ax:.1f},{ay:.1f} L{bx:.1f},{by:.1f}", ((ax + bx) / 2, (ay + by) / 2)

    s = [f'<svg viewBox="0 0 {W} {W}" width="{W}"><defs>'
         '<marker id="fg" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="8" markerHeight="8" orient="auto">'
         '<path d="M0,0 L10,5 L0,10 z" fill="#888"/></marker>'
         '<marker id="fr" viewBox="0 0 10 10" refX="9" refY="5" markerWidth="6" markerHeight="6" orient="auto">'
         '<path d="M0,0 L10,5 L0,10 z" fill="#d22"/></marker></defs>']
    etiquetas = []
    for u, v, p in grafo.aristas():
        d, medio = trazo(u, v)
        rojo = (u, v) in en_ruta
        marca = (' marker-end="url(#fr)"' if rojo else ' marker-end="url(#fg)"') if grafo.dirigido else ""
        s.append(f'<path d="{d}" class="{"er" if rojo else "e"}"{marca}/>')
        if grafo.es_ponderado():
            etiquetas.append(f'<text x="{medio[0]:.1f}" y="{medio[1] - 5:.1f}" class="pe">{e(str(formatear(p)))}</text>')
    s.extend(etiquetas)
    marcados = set(ruta or [])
    for x in nodos:
        px, py = pos[x]
        s.append(f'<circle cx="{px:.1f}" cy="{py:.1f}" r="{r}" class="{"nr" if x in marcados else "nd"}"/>'
                 f'<text x="{px:.1f}" y="{py:.1f}" class="tx">{e(x)}</text>')
    return "".join(s) + "</svg>"


def reporte_grafo_html(grafo, inicio, origen, destino):
    """
    QUE HACE: crea el reporte HTML de un GRAFO y lo abre en el navegador.
    ENTRADA : grafo y los nodos elegidos (inicio de recorridos, origen y
              destino de la mejor ruta).
    PROCESO : arma dibujo, matriz, lista de adyacencia, grados, conectividad,
              recorridos BFS/DFS, distancias minimas y mejor ruta.
    SALIDA  : archivo reporte_grafo.html abierto en el navegador.
    """
    e = html.escape
    nombres = grafo.nodos()
    ruta, costo = grafo.mejor_ruta(origen, destino)
    dist, _ = grafo.dijkstra(origen)
    unidad = "" if grafo.es_ponderado() else " conexiones"
    tipo = "DIRIGIDO" if grafo.dirigido else "NO DIRIGIDO"
    nom, mat = grafo.matriz_adyacencia()
    mat = [[formatear(x) if x != "-" else x for x in fila] for fila in mat]
    gr = grafo.grados()
    comps = grafo.componentes()
    lista = "\n".join(
        f"{n} -> " + (", ".join(f"{v}({formatear(grafo.ady[n][v])})" if grafo.es_ponderado() else v
                                for v in grafo.vecinos(n)) or "(sin conexiones salientes)") for n in nombres)
    grados = "\n".join(
        f"{n}: " + (f"sale {gr[n][1]}, entra {gr[n][0]}" if grafo.dirigido else f"{gr[n][1]} conexiones")
        for n in nombres)
    if not grafo.dirigido:
        grados += f"\nSuma de grados = {sum(s for _, s in gr.values())} = 2 x {len(grafo.aristas())} aristas (apretón de manos)"
    conexo = ("El grafo es <b>CONEXO</b>." if len(comps) == 1 else
              f"El grafo <b>NO es conexo</b>: {len(comps)} componentes: " + " | ".join(", ".join(c) for c in comps))
    dists = "\n".join(f"{origen} -> {n}: " + (f"{formatear(dist[n])}{unidad}" if dist[n] != INF else "sin ruta")
                      for n in nombres)
    if ruta:
        res = f'<span class="r">{e(" → ".join(ruta))}</span> &nbsp; costo total: <b>{formatear(costo)}{unidad}</b>'
    else:
        res = f"No existe ruta de {e(origen)} a {e(destino)}."
    cuerpo = (
        f'<div class="c"><h2>Grafo {tipo}: {len(nombres)} nodos y {len(grafo.aristas())} conexiones</h2>'
        f'{svg_grafo(grafo, ruta)}<p class="m">La mejor ruta de {e(origen)} a {e(destino)} va en rojo.</p></div>'
        f'<div class="c"><h2>Matriz de adyacencia</h2>{tabla_html(nom, mat)}</div>'
        f'<div class="c"><h2>Lista de adyacencia</h2><pre>{e(lista)}</pre></div>'
        f'<div class="c"><h2>Grado de cada nodo y conectividad</h2><pre>{e(grados)}</pre><p>{conexo}</p></div>'
        f'<div class="c"><h2>Recorridos desde {e(inicio)}</h2>'
        f'<p><b>Anchura (BFS):</b> {e(" → ".join(grafo.bfs(inicio)))}</p>'
        f'<p><b>Profundidad (DFS):</b> {e(" → ".join(grafo.dfs(inicio)))}</p></div>'
        f'<div class="c"><h2>Mejor ruta (Dijkstra)</h2><p>{res}</p>'
        f'<p class="m">Distancias mínimas desde {e(origen)}:</p><pre>{e(dists)}</pre></div>')
    return guardar_y_abrir_html("reporte_grafo.html", "Reporte de GRAFOS", cuerpo)


def svg_arbol(arbol, orden):
    """
    QUE HACE: dibuja el arbol como imagen SVG con el orden de visita.
    ENTRADA : arbol y la lista de valores de un recorrido.
    PROCESO : usa arbol.posiciones() para ubicar los nodos, dibuja las lineas padre-hijo,
              los circulos y, en cada nodo, un numero rojo con su lugar en el recorrido.
    SALIDA  : texto SVG.
    """
    e = html.escape
    pos = arbol.posiciones()
    sx, sy = 52, 66
    W = max(240, len(pos) * sx + 30)
    H = (arbol.altura() + 1) * sy + 30
    rango = {v: i + 1 for i, v in enumerate(orden)}
    xy = {v: (28 + x * sx, 34 + (-y) * sy) for v, (x, y) in pos.items()}
    s = [f'<svg viewBox="0 0 {W} {H}" width="{W}">']
    for nodo in arbol.lista_nodos():
        for h in (nodo.izq, nodo.der):
            if h:
                (x1, y1), (x2, y2) = xy[nodo.valor], xy[h.valor]
                s.append(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" class="e"/>')
    for v, (x, y) in xy.items():
        s.append(f'<circle cx="{x}" cy="{y}" r="19" class="nd"/><text x="{x}" y="{y}" class="tx">{e(v)}</text>'
                 f'<circle cx="{x + 17}" cy="{y - 17}" r="9" class="bd"/>'
                 f'<text x="{x + 17}" y="{y - 17}" class="bt">{rango[v]}</text>')
    return "".join(s) + "</svg>"


def reporte_arbol_html(arbol):
    """
    QUE HACE: crea el reporte HTML de un ARBOL y lo abre en el navegador.
    ENTRADA : arbol.
    PROCESO : arma los datos (nodos, hojas, altura), el arbol dibujado 3 veces con el
              orden de visita de preorden, inorden y postorden y los recorridos escritos.
    SALIDA  : archivo reporte_arbol.html guardado y abierto en el navegador.
    """
    e = html.escape
    n, hojas, alt = estadisticas_arbol(arbol)
    rec = [("PREORDEN (raíz - izq - der)", arbol.preorden()),
           ("INORDEN (izq - raíz - der)", arbol.inorden()),
           ("POSTORDEN (izq - der - raíz)", arbol.postorden())]
    figuras = "".join(f"<div><h2>{t}</h2>{svg_arbol(arbol, o)}</div>" for t, o in rec)
    lineas = "".join(f"<p><b>{t.split(' ')[0]}:</b> {e(' → '.join(o))}</p>" for t, o in rec)
    lineas += f"<p><b>POR NIVELES:</b> {e(' → '.join(arbol.por_niveles()))}</p>"
    if arbol.es_abb:
        lineas += '<p class="m">En un árbol de búsqueda el INORDEN entrega los valores ordenados.</p>'
    cuerpo = (
        f'<div class="c"><h2>Datos del árbol</h2><p>Raíz: <b>{e(arbol.raiz.valor)}</b> &nbsp; Nodos: <b>{n}</b> &nbsp; '
        f'Hojas: <b>{hojas}</b> &nbsp; Nodos internos: <b>{n - hojas}</b> &nbsp; Altura: <b>{alt}</b> &nbsp; '
        f'Aristas: <b>{n - 1}</b></p><pre>{e(texto_arbol(arbol))}</pre></div>'
        f'<div class="c"><h2>Recorridos (el número rojo indica el orden de visita)</h2><div class="f">{figuras}</div></div>'
        f'<div class="c"><h2>Resultados</h2>{lineas}</div>')
    return guardar_y_abrir_html("reporte_arbol.html", "Reporte de ÁRBOLES", cuerpo)


# ===================================================================
#  MENU DE ARBOLES Y MENU PRINCIPAL
# ===================================================================
def menu_arboles():
    """
    QUE HACE: muestra el menu de ARBOLES y resuelve segun la opcion elegida.
    MENU DE ARBOLES (mismo esquema que el menu de grafos).
    ENTRADA : opcion elegida (1, 2, 3 o 0).
    PROCESO : arma el arbol segun el modo elegido, llama a resolver_arbol()
              y ofrece guardar el reporte en HTML.
    SALIDA  : vuelve al menu principal con la opcion 0.
    """
    while True:
        print("\n========== ARBOLES ==========")
        print("1. Escribir el PROBLEMA COMPLETO (el programa lo interpreta)")
        print("2. Ingresar DATOS CONOCIDOS")
        print("3. Usar un EJEMPLO")
        print("0. Volver al menu principal")
        op = input("Opcion: ").strip()
        if op == "1":
            a = modo_problema_completo_arbol()
        elif op == "2":
            a = modo_datos_conocidos_arbol()
        elif op == "3":
            a = ejemplo_precargado_arbol()
        elif op == "0":
            return
        else:
            print("Opcion no valida.")
            continue
        if a is None or a.raiz is None:
            print("No hay suficientes datos para armar el arbol.")
            continue
        resolver_arbol(a)
        if pedir_si_no("Guardar el reporte en HTML y abrirlo en el navegador?"):
            reporte_arbol_html(a)


def menu_principal():
    """
    QUE HACE: muestra el menu principal de estructuras (grafos o arboles).
    MENU PRINCIPAL DE ESTRUCTURAS.
    ENTRADA : opcion elegida (1, 2 o 0).
    PROCESO : abre el menu de GRAFOS o el de ARBOLES.
    SALIDA  : termina el programa con la opcion 0.
    """
    while True:
        print("\n==================================")
        print("   MENU DE ESTRUCTURAS DE DATOS")
        print("==================================")
        print("1. GRAFOS  (matriz de adyacencia, recorridos, mejor ruta)")
        print("2. ARBOLES (recorrido inorden, postorden, preorden)")
        print("0. Salir")
        op = input("Opcion: ").strip()
        if op == "1":
            menu_grafos()
        elif op == "2":
            menu_arboles()
        elif op == "0":
            print("Fin del programa.")
            return
        else:
            print("Opcion no valida.")


# Punto de entrada: se ejecuta solo si corremos este archivo directamente
if __name__ == "__main__":
    menu_principal()