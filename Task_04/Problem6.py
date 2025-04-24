from datetime import datetime

def time_delta(t1, t2):
    T_Format = '%a %d %b %Y %H:%M:%S %z'
    dt1 = datetime.strptime(t1, T_Format)
    dt2 = datetime.strptime(t2, T_Format)
    return str(abs(int((dt1 - dt2).total_seconds())))

if __name__ == '__main__':
    import sys
    input = sys.stdin.read().split('\n')
    t = int(input[0])
    for i in range(1, 2*t+1, 2):
        t1 = input[i].strip()
        t2 = input[i+1].strip()
        print(time_delta(t1, t2))
