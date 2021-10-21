# ------------------------------------------------------------
# MC458 - Lab04: Ordenacao de contas bancarias
# Autor: Miguel Teixeira Buzato (185598)
# mtbuzato.com.br
#
# Ao receber uma lista de contas em hex, ordená-las em 'ordem
# alfabética' (equivalente ao crescente numérico) utilizando o
# Radix Sort. Para isso, foi utilizada uma versão do Counting
# Sort capaz de processar esses números de conta.
# ------------------------------------------------------------

acc_format = 'XX XXXXXXXX XXXX XXXX XXXX XXXX' # Utilizado para pular espaços

# Implementação do Counting Sort que
# suporta essas strings. Recebe a lista e
# qual index da string estamos observando
# (equivalente a olhar para um algarismo)
def counting_sort(arr, x):
  n = len(arr)

  output = [0] * (n) # Criamos a array de saíða
  count = [0] * 16 # e a de contagem (16 pois estamos em hex)

  # Fazemos a contagem, transformando o hex em int para relacionar na array de contagem
  for i in range(0, n):
    count[int(arr[i][x], 16)] += 1

  # E então somamos as cada número da array de contagem
  # com o anterior, em ordem crescente
  for i in range(1, 16):
    count[i] += count[i - 1]

  # E então, de trás pra frente construímos nossa
  # array de saída
  for n in reversed(arr):
    index = int(n[x], 16)
    output[count[index] - 1] = n
    count[index] -= 1

  return output

# O RadixSort vai basicamente executar o
# Counting Sort para cada 'algarismo'
# do número da conta
def radix_sort(arr):
  x = 30

  while x >= 0:
    if acc_format[x] != ' ':
      arr = counting_sort(arr, x)
    x -= 1

  return arr

if __name__ == "__main__":
  transactions = {}

  n = int(input())

  # Leitura e contagem dos inputs
  for i in range(n):
    account = input()

    if account not in transactions:
      transactions[account] = 0

    transactions[account] += 1

  # Aplicação do algoritmo
  sorted_accounts = radix_sort(list(transactions.keys()))

  # Imprimindo saída
  print(len(sorted_accounts))
  for sorted_account in sorted_accounts:
    print(f'{sorted_account} {transactions[sorted_account]}')
