# Ejercicios_Recursividad

Este es el link del [repositorio]: https://github.com/guerramorantemiguel/Ejercicios_Recursividad.git

Ejercicio 5
Ejercicio 6:

```
frase = str(input('Introduce la frase: '))
sum = 0
max = 0
letras = []
n = int(len(frase))
for i in range(0,n):
  if(frase[i: i + 1]!=' '):
    letras.append(frase[i: i + 1])
    max = max + 1
while(letras[sum]==letras[max - 1 - sum] and sum<max/2):
  print(str(sum) + letras[sum] + letras[max-1-sum])
  sum = sum + 1
  if(sum==int(max/2)):
    print('La frase es palíndromo')
  else:
    print('La frase no es palídormo')
  
```
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
