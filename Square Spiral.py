add = lambda x,y: [x[0] + y[0], x[1] + y[1]]

def generate_spiral(n = 10):
    index = [0, 0]
    directions = [[-1,0], [0,1], [1, 0], [0, -1]]
    step, current_number = 1, 0
    direction = 0

    while current_number < n:
        for i in range(1, step + 1):
            index = add(index, directions[direction % 4])
            current_number += 1
            print(current_number, index)
        step += 1
        direction += 1

generate_spiral()