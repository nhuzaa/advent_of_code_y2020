'''
--- Day 7: Handy Haversacks ---



Part 1
'''
import math
def read_data(file):
    with open(file, "r") as f:
        data = f.read()
        data_list= [x for x in data.split('\n')]
    return data_list 

def main():
    RULES_POS = 4

    rules = read_data("input_sample")
    print('rules', rules)

    rules_dict ={}
    for r in rules:
        ww = r.split(' ')
        key = ' '.join(ww[:2]) # getting first two words from lines
        rr = ww[4:]
        
        contains = []
        x = 0
        y = 1
        z = 2 
        inc = 4 
        while x < len(rr):
            if rr[x] == 'no':
                break
            value = (int(rr[x]), rr[y] + ' ' + rr[z])
            contains.append(value)
            x += inc
            y += inc 
            z += inc

        rules_dict[key] = contains
    print('######')
    # print(rules_dict)
    def
    find = 'shiny gold'
    count =0
    for k in rules_dict:
        for jj in rules_dict[k]:
            rules_dict[jj[1]] == 
            if jj[1] == find:
                count += jj[0]
                break
        print(k, rules_dict[k])
    print("COUNT", count)

if __name__ == '__main__':
    import time 
    b = time.time()
    main()
    e = time.time()
    print("execution time:", e-b)

