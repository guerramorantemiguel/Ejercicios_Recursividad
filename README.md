# Ejercicios_Recursividad

Este es el link del [repositorio]: https://github.com/guerramorantemiguel/Ejercicios_Recursividad.git

Ejercicio 5
Ejercicio 6

Ejercicio 7:

```
col = str(input('Introduce los colores (R), (V), (Otros), (A): '))
color = col.upper()
r  = 0
v = 0
a = len(color) - 1
colores = []
for j in range(0, a+1):
  colores.append(color[j:j+1])
while(v<=a):
  if(colores[v] == 'R'):
    v = v + 1
  else:
    if(colores[v] == 'R'):
      aux = colores[v]
      colores[v] = colores[r]
      colores[r] = aux
      v = v + 1
      r = r + 1
    else:
      colores[v] = 'A'
      aux = colores[v]
      colores[v] = colores[a]
      colores[a] = aux
      a = a + 1
print(colores)
```
