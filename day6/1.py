'''
--- Day 6: Custom Customs ---


Part 1
'''
import math
def read_data(file):
    with open(file, "r") as f:
        data = f.read()
        data_list= [x for x in data.split('\n\n')]
    return data_list 

def main():
    groups = read_data("input")
    print('groups',groups)
    sum = 0
    for g in groups:
        uq_d = {c for c in  g if c !='\n'}
        print(uq_d, 'unique')
        sum += len(uq_d)

    print('sum', sum)

if __name__ == '__main__':
    import time 
    b = time.time()
    main()
    e = time.time()
    print("execution time:", e-b)

