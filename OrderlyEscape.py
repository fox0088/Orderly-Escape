from collections import Counter

def calc_gcd(x,y):
  if y==0: return x
  return calc_gcd(y,x%y)

def calc_fac(x):
  if x==1: return 1
  return x*calc_fac(x-1)

def cycle_count(c, n, fac):
  cc=fac[n]
  for i,j in Counter(c).items():
    cc//=(i**j)*fac[j]
  return cc

def partitions(n):
  a = [1]*n
  arr=[a[:]]
  k = n-1
  while k > 0:
    x = a[k-1] + 1
    y = a[k] - 1
    k -= 1
    while x>1 and x<=y:
      a[k] = x
      y -= x
      k += 1
    a[k] = x + y
    arr+= [a[:k+1]]
  return arr

def solution(w, h, s):

  gcd=dict()
  fac=dict()
  for i in range(1,max(w,h)+1):
    fac[i]=calc_fac(i)
    for j in range(i,max(w,h)+1):
      gcd[(i,j)]=calc_gcd(i,j)

  cpw_arr=partitions(w)
  cph_arr=cpw_arr if w==h else partitions(h)

  grid=0
  for cpw in cpw_arr:
    for cph in cph_arr:
      m=cycle_count(cpw, w, fac)*cycle_count(cph, h, fac)
      grid+=m*(s**sum([sum([gcd[(min(i, j),max(i,j))] for i in cpw]) for j in cph]))
  return str(grid//(fac[w]*fac[h]))


print(solution(12,12,4))
