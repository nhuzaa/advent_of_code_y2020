'''
Toboggan Trajectory
Part 2
'''
def main():

    with open("input", "r") as f:
        data = f.read()
        pass_list = [x for x in data.splitlines()]

    print(pass_list)

    width_of_trees = len(pass_list[0])
    no_of_lanes = len(pass_list)
    print('width_of_trees', width_of_trees)
    print('no_of_lanes', no_of_lanes)

    count_trees_pass = 0
    prod_of_tree_pass =  1 # dnt set to zero

    slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]

    
    for slope in slopes:
        i = 0 # x position
        count_trees_pass = 0
        plane_pos = [0,0]
        for y in range (plane_pos[1], no_of_lanes, slope[1]):
            if y > 0:#skip first line
                if pass_list[y][i] == '#':
                    count_trees_pass += 1
                    # print('X')
                else:
                    pass
                    # print('0')

            for x in range (plane_pos[0], plane_pos[0]+slope[0]+1): # +1 as range generate (0,3) 0 1 2
                i = x % width_of_trees
                # print('mod',x, y)
            # print('^')
            plane_pos[0] = x
        
        print("trees encounter", count_trees_pass)
        prod_of_tree_pass *= count_trees_pass

    print("prod_of_tree_pass", prod_of_tree_pass)


if __name__ == '__main__':
    import time 
    b = time.time()
    main()
    e = time.time()
    print("execution time:", e-b)
