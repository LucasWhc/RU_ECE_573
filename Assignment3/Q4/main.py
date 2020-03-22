from llrbt import left_red_black_tree
import numpy as np
import random


# I learned from # https://stackoverflow.com/questions/36242046/internal-path-length-of-red-black-tree
def calculate_path_length(node, length_cur=0):
    if node is None:
        return 0
    else:
        return length_cur + calculate_path_length(node.l_child, length_cur + 1) \
               + calculate_path_length(node.r_child, length_cur + 1)


def main():
    trials = 1000
    for length in list(range(500, 10001, 500)):
        paths = []
        for i in range(trials):
            values = [random.randint(1, length) for _ in range(length)]
            tree = left_red_black_tree()
            for val in values:
                tree.insert_in_tree(val)
            paths.append(calculate_path_length(tree.root) / length)
            # print(i)
        average = np.mean(paths)
        std_dev = np.std(paths, ddof=1)
        print('In a shuffled insertion of', length, 'elements, the average path length is', 2*average,
              'and the standard deviation is', 0.5*std_dev)


if __name__ == '__main__':
    main()
