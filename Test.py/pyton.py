def dodaj(x,y):
  return x+y
def odejmij (x,y):
   return x-y
print("Wybierz operację:")
print("1. Dodaj")
print("2. Odejmij")
choice=input(" Którą operację chczesz wykonać 1 lub 2?:")
num1= float(input("Pierwsza wartość:"))
num2= float(input("Druda wartość:"))
if choice=='1':
  print(num1,"+",num2,"=", dodaj(num1,num2))
elif choice=='2':
  print(num1,"-",num2,"=", odejmij(num1,num2))
  print("Niepoprawna wartość")