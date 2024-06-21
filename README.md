# Guess Who

Agente inteligente para Guess Who (¿Quién es quién?)

Este código permite adivinar el personaje mediante consultas a una base de datos Prolog.

## Uso

- Ejecutar guesswho.py
- Elegir modo de funcionamiento: Versus (Permite usarse en una partida normal), Auto (se ejecuta hasta encontrar la solucion)

## Optimización VS Busquedas

El quién es quién es un buen ejemplo de problema de optimización puesto que el rendimiento de la partida depende completamente de la calidad de las preguntas realizadas. En el caso de que las cuestiones abarquen demasiados personajes no nos facilitarán demasiada información, y en caso de ser demasiado precisas es más complicado que nos den información relevante. Por este motivo es muy importante encontrar un balance a la hora de realizar las preguntas para maximizar la información obtenida.

## Entorno de tareas

Entorno de tareas | Observable| Agentes | Determinista | Episódico | Estático | Discreto | Conocido
:---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
 GuessWho | Parcial | Multi | Estocástico | Secuencial | Estático | Discreto | Conocido |

## Algoritmo

Este algoritmo busca seleccionar características de los personajes de forma que se creen dos grupos del mismo tamaño. De esta forma, empezando con 24 personajes, la primera pregunta podría ser "¿Tu personaje es calvo, y tiene gafas y las mejillas rojas?", separando los personajes en dos grupos de 12. Y continuaría de esta forma hasta encontrar al personaje correcto.

Por lo que, en promedio, el personaje se acertará en unos 6 intentos.

## Estructura del agente

![](./doc/agent_structure.png)

## Programación lógica

El quién es quién es un juego que tiene una naturaleza lógica, ya que los jugadores hacen preguntas sobre características de los personajes que pueden ser representadas fácilmente mediante reglas lógicas y hechos. Este proceso de razonamiento se puede realizar de forma eficiente con esta estructura.

## Base de Datos Prolog

Cada personaje está representado como un predicado que contiene su nombre como primer argumento y una lista de sus características como segundo. Además, existe un predicado que nos permite consultar si un personaje cuenta con una propiedad específica.

## Requisitos

- Conda
- Python 3.10
- Pysweep

## Instalación

- Instala Conda
- Crea un directorio
- Clona el proyecto
- Inicializa el entorno virtual y actívalo.
```bash
$ conda create -n guesswho python=3.10
$ conda activate guesswho
```
- Instala las dependencias.
```bash
$ pip install -r requirements.txt
```
