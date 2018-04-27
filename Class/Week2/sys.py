# Author:Alonso Zhang


print(10 / 3)
print(chr(66))
print(u"\u0041")
print(len(u'中文'))
print(len('中文'))

name = 'colby'
print(name.expandtabs())
print(name.center(50, '-'))

print(','.join(['a', 'b', 'c']))

p = str.maketrans('abcdefg', '1234567')  # 将abcdefg映射成1234567
print('colby'.translate(p))

t = ("1", "2", "3")
for i in enumerate(t):
    print(i)
s = set([1, 1, 2, 2, 3, 3])
print(s)