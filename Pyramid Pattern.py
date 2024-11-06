#Pyramid Pattern problem with f-string

#1. Pyramid
print("\n1. Normal Pyramid")
for i in range(5):
    x='🤌 '
    x = x*i
    print(f'{x: ^10}')

#2. Invert Pyramid
print("\n2. Invert Pyramid")
for i in range(5):
    x ='🤌 '
    x = x*(5-i)
    print(f'{x: ^10}')

#3. Left Sided Pyramid
print("\n3. Left Sided Pyramid")
for i in range(5):
    x = '🤌 '
    x = x*i
    print(f'{x: <10}')

#4. Right Sided Pyramid
print("\n4. Right Sided Pyramid")
for i in range(5):
    x ='🤌 '
    x = x*i
    print(f'{x: >10}')