x=5
x+=3
x=x+3
x*=4
print("my answer is:", x)

y=3%4
print("my answer is:",y)

y=10
y==30
print (y)

y=20
y=34
print (y==35)

p=6
m=7
print (p!=m)

x=5
print(not(x>3 and x<10))

#conditional statements
age=25
if age>=18:
    print("you are an adult")

#nothing happens when the code is false
age=15
if age>=18:
    print("you are an adult")

#the elif statement
if age > 18:
    print("adult")
elif age < 18:
    print("child")

a = 33
b = 10
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

president_age=20
nationality="Ugandan"

if president_age >=18 and nationality=="Kenyan":
    print("you are a successful candidate")
else:
    print("you cannot be a candidate")

country="Tanzania"
if country=="Kenyan":
    print("selected")
elif country=="Ugandan":
    print("selected too")
else:
    print("not selected")



