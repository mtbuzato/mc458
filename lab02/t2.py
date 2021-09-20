# ------------------------------------------------------------
# MC458 - Lab02: Ana Sabi Tudor e suas paradas
# Autor: Miguel Teixeira Buzato (185598)
# mtbuzato.com.br
#
# Implementação do Find Maximum Subarray problem em versão
# iterativa, com base no algoritmo de Joseph B. Kadane.
# ------------------------------------------------------------

if __name__ == "__main__":
  n = int(input())
  p = [int(x) for x in input().split(' ')]

  max_i = max_j = max_total = cur_i = 0
  cur_total = -100000

  for (cur_j, num) in enumerate(p): # Passamos pela lista 1x apenas (O(n))
    if cur_total < 0: # Se o caminho não está valendo a pena, começamos do zero
      cur_i = cur_j
      cur_total = 0

    cur_total += num # Adicionamos o peso no caminho
      
    if cur_total > max_total or ( # Se o caminho for maior OU se for igual mas podemos maximizar j - i, então substituímos
      cur_total == max_total and
      cur_j - cur_i > max_j - max_i
    ):
      max_total = cur_total
      max_i = cur_i
      max_j = cur_j
  
  if max_total <= 0: # Se o melhor caminho for 0 ou menos, retornamos 0,0
    print(0, 0)
  else:
    print(max_i + 1, max_j + 1) # Caso contrário, retornamos o caminho