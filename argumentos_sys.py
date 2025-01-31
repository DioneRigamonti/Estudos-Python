import sys

argumento_01 = int(sys.argv[1])
argumento_02 = int(sys.argv[2])
argumento_03 = int(sys.argv[3])

print(f'ESSE É O ARGUMENTO NUMERO 1: {argumento_01}')
print(f'ESSE É O ARGUMENTO NUMERO 2: {argumento_02}')
print(f'ESSE É O ARGUMENTO NUMERO 3: {argumento_03}')

def soma(*args):
    return sum(args)

argumentos = soma(argumento_01, argumento_02, argumento_03)

print(f'A soma de todos os argumentos é de : {argumentos}')