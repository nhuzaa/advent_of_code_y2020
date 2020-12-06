'''
--- Day 5: Binary Boarding ---

Part 1
'''
import math
def read_data(file):
    with open(file, "r") as f:
        data = f.read()
        data_list= [x for x in data.splitlines()]
    return data_list 

def binary_operation(L,M,N,H, code,str_f, str_b):
    for k,r in enumerate(code):
        M = int((L +H) /2)
        N = round((L +H) /2)
        print("%%", L,M,N,H)
        if r == str_f:
           H = M 
        else:
           L = N 
        # print(">>", L,M,N,H)
        print('r',r, L,H)
    return L if N == M == H else H

def main():
    data = read_data("input")
    print('data',data)

    highest_id = 0
    for bp in data:

        final_row = binary_operation(0,64,65,127, bp[0:7],'F','B')
        final_col = binary_operation(0, 3, 4,7, bp[7:],'L', 'R')
        print('final row',final_row)
        print('final col',final_col)

        id = final_row * 8 + final_col
        print('id',id)
        highest_id = id if id > highest_id else highest_id
        print('#####')

    print('Highest ID', highest_id)

if __name__ == '__main__':
    import time 
    b = time.time()
    main()
    e = time.time()
    print("execution time:", e-b)

