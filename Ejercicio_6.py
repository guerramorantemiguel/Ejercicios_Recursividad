frase = str(input('Introduce la frase: '))
sum = 0
max = 0
letras = []
n = int(len(frase))
for i in range(0,n):
  if(frase[i: i + 1]!=' '):
    letras.append(frase[i: i + 1])
    max = max + 1