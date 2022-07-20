import random

uppercase1=chr(random.randint(65, 90))
uppercase2=chr(random.randint(65, 90))

lowercase1=chr(random.randint(97, 122))
lowercase2=chr(random.randint(97, 122))

number1=random.randint(0,9)
number2=random.randint(0,9)

password=uppercase1+uppercase2+lowercase1+lowercase2+str(number1)+str(number2)
#random.shuffle(password)
print(password)
