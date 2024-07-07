
month = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

# x = int(input())
# month = month[x-1]

def calendar(month,day):
  for d in range(day):
    print("  ",end=" ")

  for i in range(1,month+1):
    print(f" {i:>2}",end="")
    if(d+i+1)%7 == 0:
      print()

def calendar1(month):
  for d in range(0):
    print("  ",end=" ")

  for i in range(1,month+1):
    print(f" {i:>2}",end="")
    if(i)%7 == 0:
      print()

x = int(input())
try:
  month = month[x-1]
except:
  pass
if month == False:
  print(("it's just 12 month").upper)
match x :

  case 1 :
    print("\t JAN")
    print("="*22)
    print(" M "," T ","W ","T ","F ","S ","S ")
    print("="*22)
    calendar1(month)
    print()
    print("="*22)
  case 2 :
    print("\t FEB")
    print("="*22)
    print(" M "," T ","W ","T ","F ","S ","S ")
    print("="*22)
    day = 3
    calendar(month,day)
    print()
    print("="*22)
  case 3 :
    print("\t MAR")
    print("="*22)
    print(" M "," T ","W ","T ","F ","S ","S ")
    print("="*22)
    day = 4
    calendar(month,day)
    print()
    print("="*22)
  case 4 :
    print("\t APR")
    print("="*22)
    print(" M "," T ","W ","T ","F ","S ","S ")
    print("="*22)
    calendar1(month)
    print()
    print("="*22)
  case 5 :
    print("\t MAY")
    print("="*22)
    print(" M "," T ","W ","T ","F ","S ","S ")
    print("="*22)
    day = 2
    calendar(month,day)
    print()
    print("="*22)
  case 6 :
    print("\t JUNE")
    print("="*22)
    print(" M "," T ","W ","T ","F ","S ","S ")
    print("="*22)
    day = 5
    calendar(month,day)
    print()
    print("="*22)
  case 7 :
    print("\t JULY")
    print("="*22)
    print(" M "," T ","W ","T ","F ","S ","S ")
    print("="*22)
    calendar1(month)
    print()
    print("="*22)
  case 8 :
    print("\t AUG")
    print("="*22)
    print(" M "," T ","W ","T ","F ","S ","S ")
    print("="*22)
    day = 4
    calendar(month,day)
    print()
    print("="*22)
  case 9 :
    print("\t SEP")
    print("="*22)
    print(" M "," T ","W ","T ","F ","S ","S ")
    print("="*22)
    day = 6
    calendar(month,day)
    print()
    print("="*22)
  case 10 :
    print("\t OCT")
    print("="*22)
    print(" M "," T ","W ","T ","F ","S ","S ")
    print("="*22)
    day = 1
    calendar(month,day)
    print()
    print("="*22)
  case 11 :
    print("\t NOV")
    print("="*22)
    print(" M "," T ","W ","T ","F ","S ","S ")
    print("="*22)
    day = 4
    calendar(month,day)
    print()
    print("="*22)
  case 12 :
    print("\t DEC")
    print("="*22)
    print(" M "," T ","W ","T ","F ","S ","S ")
    print("="*22)
    day = 6
    calendar(month,day)
    print()
    print("="*22)
  case defult:
    print("month it just have 12 month")
  
  