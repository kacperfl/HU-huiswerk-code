names = ['John', 'Alice', 'Bob', 'Lucy']
scores = [85, 90, 78, 92]

res = zip(names, scores)
for value in res:
    if value[1] > 80:
        print(value)
