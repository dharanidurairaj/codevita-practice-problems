d,m,y=map(int,input().split("/"))
if(m<13):
    if((m==1 or m==3 or m==5 or m==7 or m==8 or m==10 or m==12) and (d<32)):
        print("Valid")
    elif((m==4 or m==9 or m==11) and (d<31)):
        print("Valid")
    elif(m==2 and d<29):
        print("Valid")
    elif(m==2 and d==29 and y%4==0):
        print("valid")
    else:
        print("Invalid")
else:
    print("Invalid")
