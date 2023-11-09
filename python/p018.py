

with open('../data/data18.txt','r') as f:
    ans = []
    all_lines = f.readlines()
    for i in range(len(all_lines)):
        line = all_lines[i]
        line = line.split()
        as_int = [int(n) for n in line]
        ans.append(as_int)
    triangle = ans

def compute():
    for i in reversed(range(len(triangle)-1)):
        for j in range(len(triangle[i])):
            triangle[i][j] += max(triangle[i+1][j],triangle[i+1][j+1])
    return str(triangle[0][0])

if __name__ == "__main__":
    print (compute())