# ------------------------------------------------------------
# MC458 - Lab01: Problema de Acesso à Lista
# Autor: Miguel Teixeira Buzato (185598)
# mtbuzato.com.br
#
# Implementação de um sistema de cálculo de custos de
# algoritmos do problema de acesso à lista.
# O código foi desenvolvido pensando em atingir o resultado
# do custo, e não de implementar o algoritmo em si.
# ------------------------------------------------------------

from types import FunctionType
from typing import Dict, List

# Classe pra associar valores
class Association():
  def __init__(self, value, associated_value):
    self.value = value
    self.associated_value = associated_value

def mtf(array: List[int], req: int, idx: int):
  # Movemos pro início
  array.pop(idx)
  array.insert(0, req)

def trans(array: List[int], req: int, idx: int):
  # Movemos pra 1 antes
  array.pop(idx)
  array.insert(max(idx - 1, 0), req)

def fc(array: List[Association], req: int, idx: int):
  value = array[idx]

  # Aumentamos a frequência
  value.associated_value += 1

  # Removemos o item
  array.pop(idx)

  # Reposicionamos o item
  for array_value in array:
    if array_value.associated_value <= value.associated_value:
      array.insert(array.index(array_value), value)
      break

def bit(array: List[Association], req: int, idx: int):
  value = array[idx]

  # Se for 1
  if value.associated_value:
    array.pop(idx)
    array.insert(0, value) # Colocamos no início

  # Flip no bit
  value.associated_value = not value.associated_value

algorithms: Dict[str, FunctionType] = {
  'mtf': mtf,
  'trans': trans,
  'fc': fc,
  'bit': bit
}

if __name__ == "__main__":
  n = int(input()) # Número total de itens
  array = [int(num) for num in input().split(' ')] # Lista com números
  bit_array = [bool(int(bit)) for bit in input().split(' ')] # Inicializador do BIT
  k = int(input()) # Número total de requisições
  requests = [int(req) for req in input().split(' ')] # Requisições

  for algo, func in algorithms.items():
    array_copy = array.copy() # Criamos uma cópia por algoritmo
    total_cost = 0

    if algo == 'bit' or algo == 'fc':
      if algo == 'fc':
        # Se for FC, criamos a associação entre valor e frequência (início = 0)
        array_copy = [Association(array_copy[i], 0) for i in range(n)]
      else:
        # Se for BIT, criamos a associação entre valor e bit
        array_copy = [Association(array_copy[i], bit_array[i]) for i in range(n)]
      
      for req in requests:
        # Buscamos o item com custo
        idx = 0
        for association in array_copy:
          if association.value == req:
            break

          idx += 1

        # Se o item foi encontrado, executamos o algoritmo,
        # caso contrário, custo de n + 1
        if idx < n:
          total_cost += idx + 1
          func(array_copy, req, idx)
        else:
          total_cost += n + 1
    else:
      # Processamos as requests
      for req in requests:
        try:
          # Pegamos a posição do item
          idx = array_copy.index(req)
          total_cost += idx + 1

          func(array_copy, req, idx) # Executamos a organização do algoritmo
        except ValueError:
          # Se o item não está na lista, retornamos
          # o custo de n + 1
          total_cost += n + 1

    print(total_cost) # Imprimimos o resultado