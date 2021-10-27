# FOR LOOP
# fruits = ["apple", "banana", "cherry"]
# print(fruits[0])
# for x in fruits:
#     print(x)
#     print('---')

# y = range(6)
# for n in y:
#     print(n)

# print('---')

# z = range(3,6)
# for m in z:
#     print(m)

# print('---')

# w = range(3,20,2)
# for o in w:
#     print(o)

# count = int(input("Berapa Data:"))

# nama_pelanggan = []
# umur_pelanggan = []

# for i in range(count):
#     print('Data ke {}'. format(i+1))
#     nama = input('Nama: ')
#     umur = int(input('Umur: '))

#     nama_pelanggan.append(nama)
#     umur_pelanggan.append(umur)

# for i in range(len(nama_pelanggan)):
#     print("Pelanggan {} berusia {}". format(nama_pelanggan[i], umur_pelanggan[i]))

# WHILE LOOP
# i = 1
# while i<6:
#     print(i)
#     i+=1

# CONTINUE
# for i in range(5):
#     if i == 2:
#         continue
#     print(i)

# for i in range(10):
#     if i%2 == 0:
#         continue
#     print(i)

# BREAK
# for i in range(5):
#     if i == 3:
#         break
#     print(i)

# NESTED LOOP
# for i in range(3):
#     print('i: {}'. format(i))
#     for j in range(3):
#         print('j: {}'. format(j))

# for baris in range(5):
#     for kolom in range(5):
#         print('{}.{}'. format(baris+1, kolom+1), end=' ')
#     print()

x = [1,2,3,4,5]
y = [2,4,3,5,6]
z =0

for i in x:
    for j in y:
        if i == j:
            z=z+1
print(z)