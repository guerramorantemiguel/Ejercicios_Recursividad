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