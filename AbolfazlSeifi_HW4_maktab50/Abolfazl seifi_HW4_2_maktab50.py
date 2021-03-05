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

temp= {}
for i in scores:
    #print(i)
    x = []
    for j in scores.get(i):
        x.append(j.get("score"))
    #print(x)
    temp[i]=x
print(temp)