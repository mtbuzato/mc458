# ------------------------------------------------------------
# MC458 - Lab05: Problema do troco
# Autor: Miguel Teixeira Buzato (185598)
# mtbuzato.com.br
#
# Implementação de um algoritmo para encontrar o menor número
# de moedas necessárias pra pagar o menor valor possível desde
# que esse seja ao menos o valor alvo. Pode ser maior.
# ------------------------------------------------------------

max_int = 1e10 # Valor máximo arbitrário

def minCoins(coins, types_of_coins, target):
  # Criamos nossa tabela de valores pra cada alvo
  table = [(0 if i == 0 else max_int) for i in range(target + 1)]
  i = 1

  # Podemos andar até o valor máximo definido como max_int
  while i < max_int:
    # Iteramos pra cada tipo de moeda
    # construindo o resultado dado base de valores anteriores
    for j in range(types_of_coins):
      if (coins[j] <= i):
        sub_res = table[i - coins[j]]
        if (sub_res != max_int and sub_res + 1 < table[i]):
          table[i] = sub_res + 1

    # A partir do momento que chegamos em valores que
    # possivelmente são o resultado
    if i >= target:
      # Se for impossível atingir o alvo
      if table[target] == max_int:
        # Aumentamos o alvo
        target += 1
        table.append(max_int)
      else:
        # Caso contrário, chegamos no resultado
        break
      
    i += 1

  return (target, table[target])

if __name__ == "__main__":
  target_amount = int(input())
  types_of_coins = int(input())
  coins = [int(x) for x in input().split()]

  results = minCoins(coins, types_of_coins, target_amount)
  print(f'{results[0]} {results[1]}')
