from llrbt import left_red_black_tree, is_red, is_black
import numpy as np
import random


def number_of_red(node):
    cnt = 0
    if node is None:
        return 0
    if is_red(node):
        cnt += 1
    return cnt + number_of_red(node.l_child) + number_of_red(node.r_child)


def main():
    trials = 100
    tree = left_red_black_tree()
    # for length in [10000, 100000, 1000000]:
    # This way of implementation will run very slow, so I suggest run 10000, 100000 and 1000000 respectively
    for length in [1000000]:
        percentages = []
        for i in range(trials):
            values = [random.randint(1, length) for _ in range(length)]
            for val in values:
                tree.insert_in_tree(val)
            percentage = number_of_red(tree.root) / length
            percentages.append(percentage)
            print(i)
        print('In a shuffled insertion of', length, 'elements, the average percentage of the red nodes is',
              np.mean(percentages))


if __name__ == '__main__':
    main()
