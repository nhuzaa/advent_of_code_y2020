
'''
--- Day 8: Handheld Halting ---

'''
import re

FILE ="input"

def readFile() -> list:
    with open(f"{FILE}", "r") as f:
        return [line.strip() for line in f.read().strip().split("\n")]

def parseIns(ins) -> dict:
    cache = [] 
    for i in ins:
        s_ins = re.split(r'(\W+)',i)
        s_ins[1] =  s_ins[1][1] # can be better
        cache.append(s_ins)
    return cache 

def follow_ins(ins_list: dict, acum: int, pos: int):
    ins = ins_list[pos]
    cmd , op, dd = ins[0], ins[1], int(ins[2])

    if cmd == 'acc':
        acum = (acum + dd) if op == "+" else (acum - dd )
        pos += 1
    elif cmd == 'jmp':
        pos = (pos + dd) if op == "+" else (pos - dd )
    elif cmd == 'nop':
        pos += 1
    else:
         # error
        pass
    return acum , pos

def part1(ins_list: dict) -> int:
    visited, acum, pos = [] , 0 , 0
    while True:
        if pos in visited:
            break
        visited.append(pos)

        acum, pos = follow_ins(ins_list, acum , pos)
            
    return acum

def replace(ins_list: dict, pos: int) -> dict:

    cmd , op, dd = ins_list[pos][0], ins_list[pos][1], ins_list[pos][2]
    new_ins = 'jmp' if cmd =='nop' else 'nop'

    new_list = [[new_ins, op, dd] if pos == k else x for k,x in enumerate(ins_list) ]
    return new_list 

def part2(ins_list: dict) -> int:
    
    for k, ins in  enumerate(ins_list):
        if ins[0] == 'jmp' or ins[0] == 'nop':
            new_list = replace(ins_list, k)
            visited = []
            acum = 0
            pos = 0
            
            while True:
                if pos in visited:
                    break
                elif pos >= len(new_list):
                    return acum
                visited.append(pos)
                acum, pos = follow_ins(new_list, acum , pos)

    return 0
            

if __name__ == "__main__":
    ins_list = parseIns(readFile())
    print(f"Part 1: {part1(ins_list)}")
    print(f"Part 2: {part2(ins_list)}")
