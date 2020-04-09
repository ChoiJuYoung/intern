from datetime import datetime

_labels = [b'a', b'b', b'c', b'd']

#case 1
start = datetime.now()
for _ in range(5000000):
    labels = []
    for lbl in _labels:
        labels.append(lbl.decode('utf-8'))
end = datetime.now()
print("CASE 1: " + str(end - start))

#case 2
start = datetime.now()
for _ in range(5000000):
    labels = list(map(lambda lbl: lbl.decode('utf-8'), _labels))
end = datetime.now()
print("CASE 2: " + str(end - start))

#case 3
start = datetime.now()
for _ in range(5000000):
    labels = [lbl.decode('utf-8') for lbl in _labels]
end = datetime.now()
print("CASE 3: " + str(end - start))



_labels = ['a', 'b', 'c', 'd']
_scores = [1, 2, 3, 4]

#case 1
start = datetime.now()
for _ in range(5_000_000):
    result = {}
    for i in range(len(_labels)):
        result[_labels[i]] = _scores[i]
end = datetime.now()
print("CASE 1: " + str(end - start))

#case 2
start = datetime.now()
for _ in range(5_000_000):
    result = {keys: values for keys, values in zip(_labels, _scores)}
end = datetime.now()
print("CASE 2: " + str(end - start))