with open('filename.txt') as f:
    strings = [s.rstrip() for s in f.readlines()]
estimation = [s.split(';')[1:] for s in strings]
for x in estimation:
    print(sum(map(int, x))/len(x))
average_math = sum([int(x[0]) for x in estimation])/len(estimation)
average_phys = sum([int(x[1]) for x in estimation])/len(estimation)
average_rus = sum([int(x[2]) for x in estimation])/len(estimation)
print(average_math, average_phys, average_rus)