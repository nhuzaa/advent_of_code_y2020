'''
--- Day 4: Passport Processing ---

Part 2
'''
import re
def read_data(file):
    with open(file, "r") as f:
        data = f.read()
        pass_list = [x for x in data.split('\n\n')]
    return pass_list 

class validation(object):

    def __init__(self):
        pass

    def byr(self,v):
        v = int(v)
        if v >= 1920 and v <= 2002:
            return True
        return False

    def iyr(self,v):
        v = int(v)
        if v >= 2010 and v <= 2020:
            return True
        return False

    def eyr(self,v):
        v = int(v)
        if v >= 2020 and v <= 2030:
            return True
        return False

    def hgt(self,v):
        unit = v[-2:]
        value = int(v[:-2])
        if unit == 'cm':
            if value >=150 and value <=193:
                return True
        elif unit == 'in':
            if value >=59 and value <=76:
                return True 
        return False

    def hcl(self,v):
        if v[0] == '#' and len(v[1:])==6:
            return True
        return False

    def ecl(self,v):
        color = ( 'amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth')
        if v in color:
            return True
        return False

    def pid(self,v):
        if len(v) == 9 :
            return True
        return False 

def validator(passport):
    required_fields = ( 'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid')
    
    vv = validation()
    for f in required_fields:
        if f in passport:
            if getattr(vv,f)(passport[f]):
                continue
            else:
                print(f ,'invalid for',passport)
                return False 
        else:
            return False

    return True


def main():
    data = read_data("input")
    valid_passports = 0
    passports =[]
    for p in data :
        datum = re.split('\n| ', p)
        single_passport = {}
        for dd in datum:
            foo= dd.split(':')
            if len(foo)>1:
                single_passport[foo[0]] = foo[1]
        valid_passports = valid_passports + 1 if validator(single_passport) else valid_passports
        passports.append(single_passport)
    # print(passports)
    print(valid_passports)
            

if __name__ == '__main__':
    import time 
    b = time.time()
    main()
    e = time.time()
    print("execution time:", e-b)

