import math
ang = float(input('Qual o ângulo? '))

seno = math.sin(math.radians(ang))
cos = math.cos(math.radians(ang))
tang = math.tan(math.radians(ang))

print(f'Seno: {seno:.2f} \nCosseno: {cos:.2f} \nTangente: {tang:.2f}')
