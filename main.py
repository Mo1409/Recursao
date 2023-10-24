# EXERCICIO 1
#A
def A(n):
  if n >= 2:
      return A(n-1) + 10 
  elif n ==1:
      return 10
  else:
      return "n inserido menor que 2 e diferente de 1"

print(A(1.3))
#B
def B(n):
  if n >= 2:
      return 1/B(n-1)   
  else:
      return 2
#C
def C(n):
  if n>=2:
      return C(n-1) +(n*n)
  elif n==1:
      return 1
#D
def D(n):
  if n>= 2:
      return (n*n)*D(n-1) + n-1
  elif n == 1:
      return 1
#E
def E(n):
  if n == 1:
      return 3
  elif n == 2:
      return 5
  elif n>= 2:
      return  (n-1)*E(n-1) + (n-2)*E(n-2)
#F
def F(n):
  if n == 1:
      return 2
  elif n == 2:
      return 5
  elif n >=2:
      return F(n-1)*F(n-2)
#G
def G(n):
  if n == 1:
      return 1
  elif n == 2:
      return 2
  elif n == 3:
      return 3
  elif n > 3:
      return G(n-1) + 2* G(n-2)+3*G(n-3)


#EXERCICIO 3
def terceira1(n):
    if n == 2:
        return 1
    elif n<2:
        return 0
    else:
        if terceira1(n-3) == 1 or terceira1(n/2) == 1:
            return 1
        else:
            return 0
print(terceira1(7))

#EXERCICIO 9
def nona(n):
  if n ==1:
      return 1
  else:
      return nona(n-1)+n
