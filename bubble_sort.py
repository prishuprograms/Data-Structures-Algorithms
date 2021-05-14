
def bubble_sort(elements, key = None):
    size = len(elements)
    for i in range(size - 1):
        swapped = False
        for j in range(size - 1 - i):
            if elements[j][key] > elements[j + 1][key]:
                tmp = elements[j]
                elements[j] = elements[j + 1]
                elements[j + 1] = tmp
                swapped = True
        if not swapped :
            break
if __name__ == '__main__':
    # elements = [5,9,2,1,67,34,88,34]
    elements = [
        {'name': 'kathy', 'transaction_amount': 200, 'device': 'vivo'},
        {'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
        {'name': 'aamir', 'transaction_amount': 800, 'device': 'iphone-8'},
        {'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
    ]
    bubble_sort(elements, key = 'transaction_amount')
    print(elements)