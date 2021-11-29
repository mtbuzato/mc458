# ------------------------------------------------------------
# MC458 - Lab06: Travessia
# Autor: Miguel Teixeira Buzato (185598)
# mtbuzato.com.br
#
# Busca encontrar a maneira mais rápida de fazer a travessia
# de n pessoas com velocidade i_n por uma ponte onde no máximo 2
# pessoas podem transitar. É necessário sempre uma pessoa estar com
# uma tocha e existe apenas uma tocha. 
# ------------------------------------------------------------

def traverse(n, speeds):
  total = (n - 2) * speeds[0] + sum(speeds[1:]) # Primeiro calculamos o "pior-melhor" caminho que podemos fazer
  limit = 2 * speeds[1] - speeds[0] # Definimos a ida e volta mais rápida
  while speeds[n - 2] > limit: # E buscamos otimizar onde possível
    total -= speeds[n - 2] - limit
    n -= 2

  return total

if __name__ == "__main__":
  n = int(input())
  speeds = [int(x) for x in input().split()]
  print(traverse(n, speeds))