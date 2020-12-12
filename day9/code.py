
'''
--- Day 9: Encoding Error ---


'''
import re
from itertools import permutations , combinations

# FILE ="input_sample"
FILE ="input"
PRE_POS = 25 

def readFile() -> list:
    with open(f"{FILE}", "r") as f:
        return [int(line.strip()) for line in f.read().strip().split("\n")]

def check_num(pos, num_list):
    pp = pos - PRE_POS
    pre_list = num_list[pp:pos]
    sum_list = [n[0] +n[1] for n in list(combinations(pre_list, 2))]
    sum_list.sort()
    sum_list = set(sum_list)

    print(sum_list)

    if num_list[pos] not in sum_list:
        return True 
    return False 


def part1(num_list: list) ->int:
    pos = PRE_POS
    while pos < len(num_list):
        if check_num(pos,num_list):
            return num_list[pos]
        pos+= 1

    return 0

def part2(num_list:list ) -> int:
    which_num = part1(num_list) 
    p_sum = prefix_sum(num_list)
    if which_num in p_sum:
         xx =jp_sum.index(which_num)

    up = 0 
    down = 2
    # print(f'which_num, {which_num}')
    while down <= len(p_sum):
        ss = sum(num_list[up:down])
        # print(ss, 'sum')
        if ss > which_num :
            if down - up > 2:
                up+=1
            else :
                up, down = 1+up,  1 +down
                
        elif ss < which_num:
            down+=1
        elif ss == which_num:
            return min(num_list[up:down]) + max(num_list[up:down])

    return 0 
    

if __name__ == "__main__":
    num_list = readFile()
    print(f"Part 1: {part1(num_list)}")
    print(f"Part 2: {part2(num_list)}")
