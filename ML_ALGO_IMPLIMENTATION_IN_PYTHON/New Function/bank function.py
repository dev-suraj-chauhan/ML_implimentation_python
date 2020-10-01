def sbi(d,y):
    if y>=10:
       R=5.5
    elif y>=5:
        R=3.5:
    else:
        R=2.5
    intr=(d*y*R)/100;
    return intr;
def icici(d,y):
    if y>=10:
       R=7.5
    elif y>=5:
        R=4.5:
    else:
        R=2.5
    intr=(d*y*R)/100;
    return intr;
    

D=int (input("Enter the diposite"))
Y=int(input("Enter year"))

print("menu","1.SBI","2.ICICI","3.exit)
c=int (input("Enter your choise"))
      if c==1:
      x=sbi(D,y)
      print("interst",x)
      elif c==2:
      y=icici(D,Y)
      print("interst",y)
      else:
      print("thanks for choising")
