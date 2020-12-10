'''
--- Day 6: Custom Customs ---


Part 2
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
        # print('>>>>')
        pp = g.split('\n')
        # print('pp',pp)
        in_pp = pp[0]
        for p in pp:
            if p is not '' :  # to skipp the last split
                in_pp = set(in_pp).intersection(p) 
                # print('in_pp', in_pp)
        # print('len', len(in_pp))
        sum += len(in_pp)

    print('sum', sum)

if __name__ == '__main__':
    import time 
    b = time.time()
    main()
    e = time.time()
    print("execution time:", e-b)

