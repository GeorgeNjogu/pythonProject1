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

number = 6
if number  % 2 == 0 :
    print("even")
else:
    print("odd")
#casting
first_name = "George"
last_name = "Njogu"
full_name=first_name+" "+last_name
print(full_name)

#int and string

first_name = "George"
last_name = 9
full_name=first_name+str(last_name)

#string to integer
pens_total=40
books_total="50"
grand_total=str(pens_total)+books_total
print("overall is:" ,grand_total)

#float to string
bucket=20.0
book="50.0"
total=bucket+float(book)
print("total is:",total,"shillings")
#or
bucket=80
book="50.0"
total=bucket+float(book)
result="total is:"+str(total)+"Shillings"
print(result)

#LOOPING
#while loop
i=1
while i<=10:
    print(i)
    i += 2
    #



