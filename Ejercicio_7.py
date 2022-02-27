col = str(input('Introduce los colores (R), (V), (Otros), (A): '))
color = col.upper()
r  = 0
v = 0
a = len(color) - 1
colores = []
for j in range(0, a+1):
  colores.append(color[j:j+1])