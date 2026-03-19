📘 GUÍA – Lenguajes y Autómatas II
🧠 1. ¿Qué es un problema?
Un problema es una situación no trivial que requiere solución.

Para resolverlo:

Se simplifica (modelo mental)

Se eliminan datos irrelevantes

Se aplica lógica o matemáticas

⚙️ 2. Elementos de un problema
Todo problema tiene 3 partes clave:

✔️ Modelo
Representación simplificada del problema real

Ej: convertir una historia en operaciones matemáticas

🎯 Objetivo
Qué se quiere lograr

Ej: menor distancia, menor costo, menos pasos

📊 Función de evaluación
Mide qué tan buena es una solución

Permite comparar soluciones

🧩 3. Tipos de problemas importantes
✈️ Problemas de rutas
Ejemplo:

Minimizar transbordos

Minimizar distancia

⚠️ Importante: el objetivo cambia la solución

🚗 Problema del Viajante (TSP)
Pasar por todas las ciudades una sola vez y regresar al inicio

Minimizar distancia total

🔹 Representación:

Grafo (nodos = ciudades)

Matriz de distancias

🔹 Complejidad:

Crece con factorial:
n! → muy grande rápidamente

👉 Conclusión:

Problema NP (intratable)

No se puede resolver exacto fácilmente

Se buscan aproximaciones

🔢 Problema SAT (Satisfactibilidad booleana)
Variables: verdadero o falso

Objetivo:

Encontrar valores que hagan la función verdadera

🔹 Operadores:

AND (∧)

OR (∨)

NOT (¬)

🔹 Forma:

FNC (Forma Normal Conjuntiva)

👉 Complejidad:

Espacio de soluciones = 
2
𝑛
2 
n
 

También es NP

📈 Programación Lineal Entera (PLE)
Maximizar o minimizar una función

Con restricciones

Ejemplo:

Maximizar ganancias

Variables: productos a fabricar

🔹 Elementos:

Función objetivo

Restricciones

Variables enteras

👉 A diferencia de otros:

Puede ser tratable si es pequeño

🤖 4. Inteligencia Artificial y problemas
La IA busca resolver problemas complejos como:

Rutas (VRP)

Reconocimiento de voz

Visión artificial

Predicciones

👉 Idea clave:

No siempre encuentra la mejor solución, pero sí una muy buena en poco tiempo

🔍 5. Búsqueda no informada
No usa información extra

También llamada:
👉 búsqueda a ciegas

Ejemplo:

Buscar llaves sin pistas

🧱 6. Representación de problemas
Estados
Cada posible configuración

Operadores
Acciones que cambian estados

Espacio de estados
Todas las combinaciones posibles

🌳 7. Árboles y grafos
Conceptos:
Nodo → estado

Padre → nodo anterior

Hijo → resultado de una acción

Raíz → inicio

Hoja → sin hijos

Problema:
Pueden existir ciclos → se deben evitar

👉 Solución:

Guardar nodos visitados

🔁 8. Proceso general de búsqueda
Iniciar con nodo raíz

Revisar si es solución

Expandir (generar hijos)

Repetir hasta encontrar solución

🌐 9. Búsqueda en amplitud (BFS)
Características:
Recorre por niveles

Usa cola FIFO

Pasos:
Meter nodo inicial

Sacar nodo

Verificar solución

Generar hijos

Repetir

✅ Propiedades
✔️ Completa
→ Siempre encuentra solución si existe

✔️ Óptima (solo en algunos casos)
→ Cuando el costo depende del nivel

❌ No siempre óptima
→ Ejemplo: rutas con distinta distancia

⏱️ Complejidad
Tiempo:
👉 O(b^d)

Memoria:
👉 Muy alta (guarda muchos nodos)

🧩 10. Ejemplo: Puzzle lineal
Estados: permutaciones

Operadores:

Izquierda (I)

Centro (C)

Derecha (D)

👉 Objetivo:

Ordenar piezas

👉 Solución:

BFS encuentra la solución con menos movimientos

💡 11. Ideas clave para examen
Todo problema necesita:
👉 modelo + objetivo + función de evaluación

Problemas NP:
👉 no se resuelven fácilmente (TSP, SAT)

BFS:
👉 usa cola FIFO
👉 es completa
👉 no siempre es óptima

Espacio de estados:
👉 crece muy rápido (factorial o exponencial)
