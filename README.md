# Ejercicios_Recursividad

Este es el link del [repositorio]: https://github.com/guerramorantemiguel/Ejercicios_Recursividad.git

Ejercicio 5:
```
tabla = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]
a = int(inpu('Introduzca el valor que quiera enontrar '))
b = 0
c = len(tabla)
d = (b + c)/2
class tablas:
  def __init__(self,tabla,a,b,c):
    self.c = c
    self.a = a
    self.b = b
  def encontrar_valor (self):
    if self.c < self.b:
      print('No existe coincidencia en la posición dada')
    else:
      self.d = d
      if tabla[self.d] == a:
        return self.d
      elif tabla[self.d] > a:
        print (encontrar_valor(self))
        return encontrar_valor (self, self.d - 1)
      else:
        return encontrar_valor(self, self.d + 1)
  resultado = tablas(tabla,a,c,b)
  print(resultado.encontrar_valor())     
```
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
