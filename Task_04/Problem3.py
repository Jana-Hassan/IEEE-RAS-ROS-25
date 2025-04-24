if __name__ == '__main__':
    N = int(input())
    List = []
    Command = {
        'insert': lambda x: List.insert(int(x[0]), int(x[1])),
        'print': lambda x: print(List),
        'remove': lambda x: List.remove(int(x[0])),
        'append': lambda x: List.append(int(x[0])),
        'sort': lambda x: List.sort(),
        'pop': lambda x: List.pop(),
        'reverse': lambda x: List.reverse()
    }
    for i in range(N):
        Com, *pos = input().split()
        Command[Com](pos)
