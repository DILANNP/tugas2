# BEBERAPA FUNGSI DALAM SEBUAH SET
print("SET 1")
himpunan_buah={'mangga','semangka','durian'}#SET1
himpunan_buah.add('jeruk')#ADD
print(himpunan_buah)
himpunan_buah.clear()#CLEAR(menghapus semua)
print(himpunan_buah)
print("SET 2")
himpunan_huruf={'a','b','c'}#SET2
print(himpunan_huruf)
himpunan_huruf.update(['d','e','f'])#UPDATE
print(himpunan_huruf)
himpunan_huruf.pop()#POP
print(himpunan_huruf)
himpunan_huruf.discard('a')#DISCARD(hapus satu anggota)
print(himpunan_huruf)
himpunan_2 = himpunan_huruf.copy()#COPY(salinan satu set menjadi set baru)
print(himpunan_2)
print("-UNION-")#SET3
x = {"apple", "banana", "cherry"}
y = {"satu", "dua", "tiga"}

z = x.union(y)#UNION(operasi gabungan antara dua set atau lebih)
print(z)

print("-difference-")
x = {"manggis", "salak", "markisa"}
y = {"satu", "dua", "tiga"}

z = y.difference(x)#DIFFERENCE
print(z)

print("-difference_update-")
x = {"what", "when", "why"}
y = {"google", "toogle", "moogle"}

x.difference_update(y)
print(x)

print("-symmetric_difference-")
set_A = {1, 2, 3, 4, 5}
set_B = {6, 7, 3, 9, 4}
print(set_A.symmetric_difference(set_B))

print("-symmetric_difference_update-")
SetA = {10, 20, 30, 40, 50, 60}
SetB = {40, 50, 60, 70}

SetA.symmetric_difference_update(SetB)
print(SetA)

print("-interection-")
set1 = {2, 4, 5, 6}
set2 = {4, 6, 7, 8}
set3 = {4, 6, 8}
 
# union of two sets
print("set1 intersection set2 : ",
      set1.intersection(set2))
 
# union of three sets
print("set1 intersection set2 intersection set3 :",
      set1.intersection(set2, set3))

print("-intersection_update-")
# declare set1
set1 = {"java", "python", "c/cpp", "html"}
  
# declare set2
set2 = {"php", "html", "java", "R"}
  
# display sets
print(set1, set2)
  
# perform intersection_update operation 
# on both the sets
set.intersection_update(set1, set2)
  
# display the result set
print(set1)

print("-ISSUPERSET-")
A = {1, 2, 3, 4, 5, 6}
B = {1, 2, 3, 4}
C = {1, 2, 3, 4}

# Returns True
print(A.issuperset(B))

# Returns False
print(B.issuperset(A))

# Returns True
print(C.issuperset(B))

print("-isdisjoint-")
x = {"sawit", "kelapa", "kurma"}
y = {"twitter", "instagram", "facebook"}

z = x.isdisjoint(y)
print(z)

print("-issubset-")
x = {"a", "b", "c"}
y = {"f", "e", "d", "c", "b", "a"}

z = x.issubset(y)
print(z)