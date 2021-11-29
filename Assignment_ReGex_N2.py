
# Q1
#a = input("Enter the number: ")
#b = input("Enter the number: ")

#def gcd(a, b):
#        if a < b:
#               a, b = b, a

#        while (b != 0):
#               return a

#print(gcd(a, b))

#second approach
#a = input("Enter the number: ")
#b = input("Enter the number: ")
#if(a<b):
 #       print("user1 number is greater than user2 number")
#else:
 #       print("user1 number is smaller than user2 number")

#Q2
#with open ("gcd_data.txt", "w+") as fileobj:
#    output=fileobj.read()
#    print(output)


#Q3 password
#import re
#p=input("Input your password:")
#x = True
#while x:
#  if (len(p)<6 or len(p)>15):
#    print("Password should be between 6-15 characters")
#    break
#  elif not re.search("[A-Z]",p):
#    print("Pasword should have at least one capital letter")
#    break
#  if not re.search("[!@#$%^]",p):
#    print("Password should have special characters !, @, #, $, %, ^")
#    break

#  else:
#    print("Valid password")
#    x=False
#    break

#if x:
#  print("Not a valid password")


#Q4: generate 26 txt files as A.txt, B.txt ... Z.txt
#with open("A.txt", 'x') as file:
    #file.write('')
#with open("B.txt", 'x') as file:
   # file.write('')
#with open("C.txt", 'x') as file:
   # file.write('')
#with open("D.txt", 'x') as file:
   # file.write('')
#with open("E.txt", 'x') as file:
    #file.write('')
#with open("F.txt", 'x') as file:
  #  file.write('')
#with open("G.txt", 'x') as file:
   # file.write('')
#with open("H.txt", 'x') as file:
   # file.write('')
#with open("I.txt", 'x') as file:
   # file.write('')
#with open("J.txt", 'x') as file:
  #  file.write('')
#with open("K.txt", 'x') as file:
#    file.write('')
#with open("L.txt", 'x') as file:
 #   file.write('')
#with open("M.txt", 'x') as file:
 #   file.write('')
#with open("N.txt", 'x') as file:
  #  file.write('')
#with open("O.txt", 'x') as file:
    #file.write('')
#with open("P.txt", 'x') as file:
  #  file.write('')
#with open("Q.txt", 'x') as file:
 #   file.write('')
#with open("R.txt", 'x') as file:
#    file.write('')
#with open("S.txt", 'x') as file:
#    file.write('')
#with open("T.txt", 'x') as file:
 #   file.write('')
#with open("U.txt", 'x') as file:
 #   file.write('')
#with open("V.txt", 'x') as file:
 #   file.write('')
#with open("W.txt", 'x') as file:
 #   file.write('')
#with open("X.txt", 'x') as file:
 #   file.write('')
#with open("Y.txt", 'x') as file:
#    file.write('')
#with open("Z.txt", 'x') as file:
 #   file.write('')

#Q5 creating data1.txt
#with open("data1.txt", 'w') as file:
#    file.write('Data Science is Awesome!')

# write an additional line to the data1.txt
#data = open('data1.txt', 'a+')
#data.write('\n' 'Welcome to the python course')

#create a new file
#with open("data2.txt", 'x') as file:
#    file.write('Data Science is Awesome!''\n' 'Welcome to the python course')





