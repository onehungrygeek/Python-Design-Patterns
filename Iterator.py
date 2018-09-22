def count_to(num):
    numbers = ['one', 'two', 'three', 'four', 'five']
    iterator = zip(range(num), numbers)
    for position, number in iterator:
        yield number

for num in count_to(4):
    print(num)
