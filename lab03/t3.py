# ------------------------------------------------------------
# MC458 - Lab03: Ordenação numa galáxia muito muito distante
# Autor: Miguel Teixeira Buzato (185598)
# mtbuzato.com.br
#
# Inicialmente tentei utilizar um BubbleSort para realizar essa
# contagem. Apesar de ter funcionado e possuir uma solução em uma
# linha, ela era ineficiente e chegava a levar mais de 30s. Então
# o melhor jeito é utilizar o MergeSort como base e contar a quantidade
# de flips que deveriam ser necessários, já que esse tenta realizar
# movimentos que levam mais de 1 número por vez de um lugar para
# o outro.
# ------------------------------------------------------------

def count_min_flips(arr):
  if len(arr) <= 1: # Parar recursões
    return 0

  mid = len(arr) // 2
  left, right = arr[:mid], arr[mid:] # Quebramos a array em 2 metades

  flips = count_min_flips(left) + count_min_flips(right) # Contamos os flips de cada metade recursivamente

  i, j = 0, 0

  # Fazemos um 'merge' das array de volta na array inicial
  # contando os 'flips' necessários para construí-la
  for idx in range(len(arr)):
    # Caminhamos na array da direita enquanto ainda existirem elementos
    # nela que forem menores que os da esquerda, ou quando a da esquerda
    # acabar. Caso contrário, caminhamos na array da esquerda e contamos os
    # 'flips' que seriam necessários pra realizar esse merge. 
    if i >= len(left) or (j < len(right) and left[i] > right[j]):
      arr[idx] = right[j]
      j += 1
    else:
      arr[idx] = left[i]
      i += 1
      flips += j

  return flips

if __name__ == "__main__":
  size = int(input())
  containers = [int(i) for i in input().split(' ')]
  print(count_min_flips(containers))