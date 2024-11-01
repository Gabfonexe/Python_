"""
Fatorial de um número:
1 -> 1 * 1
2 -> 2 * 1
3 -> 3 * 2 * 1
"""

# 1 - Fatorial de um número
def factorial(num):
  if num == 1:
    return 1
  else:
    return (num * factorial(num - 1))

number = int(input("Digite o número para o fatorial:\n"))
print(f'O fatorial de {number} é {factorial(number)}')



# 2 - Soma total de um número
def total_sum(num):
  if num == 1:
    return 1
  else:
    return (sum + total_sum(num - 1))
  
number = int(input("Digite o número para somar:\n"))
print(f'O fatorial de {number} é {total_sum(number)}')



