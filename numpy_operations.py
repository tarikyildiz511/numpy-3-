import numpy as np
#rastgele sayı
numbers1 = np.random.randint(10,100,6)
numbers2 = np.random.randint(10,100,6)
#ekrana yazdır
print(numbers1)
print(numbers2)
# n+n = result
result = numbers1 + numbers2
#n+10 = result
result = numbers1 + 10
#n-n = result
result = numbers1 - numbers2
#n*n = result
result = numbers1* numbers2
#n * 10 = result
result = numbers1* 10
# n/n = result
result = numbers1/numbers2
result = numbers1/10
# Matematikte sinüs, trigonometrik bir fonksiyon
result = np.sin(numbers1)
#Trigonometrik bir fonksiyon. Cos kısaltmasıyla ifade edilir.
result = np.cos(numbers1)
#Matematikte negatif olmayan bir gerçel {\displaystyle x\!} sayısının temel karekök bulma işlemi 
result = np.sqrt(numbers1)
#Logaritma, üstel işlevlerin tersi olan bir matematiksel işlevdir.
result = np.log(numbers1)
#
mnumbers1 = numbers1.reshape(2,3)
mnumbers2 = numbers2.reshape(2,3)
# print(mnumbers1)
# print(mnumbers2)
# result = np.vstack((mnumbers1,mnumbers2))
#döngü açmaya gerek kalmadan hepsini kontrol ediyor
result = numbers1 >=50




print(result)

