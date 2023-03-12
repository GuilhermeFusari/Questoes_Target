# Um número é Fibonacci se e somente se um ou ambos (5 * n 2 + 4) ou (5 * n 2 - 4)
import math
def RaizPerfeita(x):
    n = int(math.sqrt(x))
    return n*n == x
# Retorna true se n pertence à sequencia de fibonacci
def eFibonacci(n):
    return RaizPerfeita(5*n*n + 4) or RaizPerfeita(5*n*n - 4)
    
def main(x):
	    if (eFibonacci(x) == True):
	         print ((x),"é um numero da sequencia de Fibonacci")
	    else:
	         print ((x),"não é um numero da sequencia de Fibonacci")
x = int(input("Digite o numero que voce pensa ser da sequencia de Fibonacci: "))
main(x)