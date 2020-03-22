1. I learned from https://github.com/peterhil/leftrb/blob/master/leftrb, https://www.cs.princeton.edu/~rs/AlgsDS07/09BalancedTrees.pdf and course slides for implementing the binary search tree and red black tree.
2. For question 1, I used the following code to insert and delete nodes to verify the tree:
```python
    keys = ['T', 'H', 'I', 'S', 'I', 'S', 'A', 'N', 'E', 'X', 'A', 'M', 'P', 'L', 'E']
    values = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    st = symbol_table()
    for key, val in zip(keys, values):
        st.insert_in_st(key, val)
    print(st.search_in_st('S'))
    print(st.search_in_st('A'))
    print(st.search_in_st('E'))
    st.delete_in_st('X')
    print(st.search_in_st('X'))
    st.insert_in_st('X', 20)
    print(st.search_in_st('X'))
```
If you want to test it with other data, please change the keys and values.\
2. For question 2, 3 and 4, they all took quite long time to run. So, if you are impatient with the waiting time, please check my report directly.\
3. I used Excel to plot all the curve fitting figures. I only need to write the data into the excel and then plot the figure.\
4. To run my code, you need to install python3.7 or above and libraries including random and numpy.
