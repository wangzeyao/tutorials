import sys
if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    for i in range(n):
        # 读取每一行
        line = sys.stdin.readline().strip()
        # 把每一行的数字分隔后转化成int列表
        values = list(map(int, line.split()))
        count = []
        for i in range(len(values)):
            count.append(1)
        for i in range(len(values)):
            if i == 0:
                if values[i] > values[i+1] and values[i] > values[len(values)-1]:
                    count[i] += 1
                    continue
            if (values[i] > values[i + 1] and values[i] > values[len(values) - 1]):
                if count[i] <= count[]

