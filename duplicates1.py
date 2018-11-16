list = [1,1,1,1,1,1,2,3,3,3,3,4,5,6,6,]
def remove_dublicates(list):
    previous = None
    for a in list:
        if a !=previous:
            previous = a
            yield a
print([x for x in remove_dublicates(list)])

