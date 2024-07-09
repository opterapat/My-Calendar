import time
def command(Height,weight):
  Height = Height*0.01
  x = weight/(Height**2)
  print("BMI:"'{:.2f}'.format(x))


def body(bmi):
    bmi = 0
    result = ("")
    if bmi >= 30 :
      result = str("TOO FAT")
    elif bmi >=25 :
      result = str("FAT")
    elif bmi >=23 :
      result = str("NEARLY TO FAT")
    elif bmi >=18.5 :
      result = str("MEDIUM")
    elif bmi <18.5:
      result = str("NOOB")
    else:
      print("????")
    print("body :".upper(),result)

def add_range():
  for i in range (1):
    print(" ",end=" ")

while True:
    name_lastname = str(input("Regist You Name :").upper())
    if name_lastname =="BREAK":
      print("stop working ....")
      break
    else :
      pass
    gender = str(input("Male or Female :").upper())
    Height = eval(input("Height:"))
    weight = eval(input("Weight :"))
    bmi = command(Height,weight)

    print("Loading . . . . .")
    time.sleep(3)
    add_range()
    print("="*20)
    for b in range (2):
      print(" ",end=" ")
    print("RESULT YOUR BMI")
    result = ("")
    add_range()
    print("="*20)
    add_range()
    print(name_lastname)
    add_range()
    print(gender)
    add_range()
    print(Height,"Cm".upper())
    add_range()
    print(weight,"Kilo".upper())
    add_range()
    command(Height,weight)
    add_range()
    body(bmi)
    add_range()
    print("="*20)