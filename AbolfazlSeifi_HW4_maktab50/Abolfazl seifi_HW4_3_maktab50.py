scores = {'Art':
              [{'first_name': 'Robert', 'last_name':'Smith', 'score': 4},
               {'first_name': 'Mary', 'last_name':'Hernandez', 'score': 3}],
          'Math':
              [{'first_name': 'Robert', 'last_name':'Smith', 'score': 1},
               {'first_name': 'Maria', 'last_name':'Garcia', 'score': 2},
               {'first_name': 'Mary', 'last_name':'Hernandez', 'score': 3}],
          'Literature':
              [{'first_name': 'Robert', 'last_name':'Smith', 'score': 3},
               {'first_name': 'Maria', 'last_name':'Garcia', 'score': 4},
               {'first_name': 'Mary', 'last_name':'Hernandez', 'score': 1},
               {'first_name': 'James', 'last_name':'Johnson', 'score': 2}],
          'Physics':
              [{'first_name': 'Robert', 'last_name':'Smith', 'score': 4}],
          'Chemistry':
              [{'first_name': 'Robert', 'last_name':'Smith', 'score': 2},
               {'first_name': 'James', 'last_name':'Johnson', 'score': 3}]}

temp = set()
x={}
for i in scores:
    for j in scores.get(i):
        sum = j.get("first_name") + " " + j.get("last_name")
        temp.add(sum)
#print(temp)

for i in temp:
    y = []
    for j in scores:
        for k in scores.get(j):
            if i == (k.get("first_name") + " " + k.get("last_name")):
                y.append(k.get("score"))
    x[i] = y
print(x)