x="The quick brown fox jumps over the lazy dog"
'''
t=x.split()
temp=""
for i in t:
    temp += i[1]
print(temp)'''

print(''.join(i[1] for i in x.split()))
