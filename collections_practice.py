from collections import Counter
import ephem

phones = ['IPhone Xs', 'Samsung Galaxy S10', 'Xiaomi Mi8', 'Iphone Xs', 'Iphone Xs', 'Iphone Xs']
count = Counter(phones)
print(count)
text = 'Ехал Грека через реку видит Грека в речке рак'
text = text.lower().replace(' ','')
print(Counter(text))

mars = ephem.Mars('2020/01/05')
const = ephem.constellation(mars)
print(const)