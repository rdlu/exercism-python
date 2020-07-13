def convert(number):
    queue = []
    if number % 3 == 0: queue.append('Pling')
    if number % 5 == 0: queue.append('Plang')
    if number % 7 == 0: queue.append('Plong')
    if not queue: queue.append(str(number))

    return ''.join(queue)