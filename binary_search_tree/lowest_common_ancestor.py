binary_search_tree = [6, 4, 9, 3, 5, 7, 10]

binary_search_tree = [15, 10, 19, 7, 12, 16, 20, 6, 9, 11, 13, 14, 17, 18, 21]
#                     0  1  2 3   4  6   7
#Tree sample #######

# to go left --> index  * 2 +1
# to go right --> index *2 + 2
'''
           15
     10         19
 7     12     16    20
6 9  11 13   14 17  18 21
'''


def least_common_ancestor(binary_search_tree, elem1, elem2):
    def find_path(binary_search_tree, current_root_index, elem, path):
        path.append(binary_search_tree[current_root_index])
        if binary_search_tree[current_root_index] == elem:
            return

        if elem < binary_search_tree[current_root_index]:
            find_path(binary_search_tree, current_root_index*2 + 1, elem, path)

        if elem > binary_search_tree[current_root_index]:
            find_path(binary_search_tree, current_root_index*2+2, elem, path)
        return path

    def find_common_path(path1, path2):
        x = 0
        common_path = []
        while (x < len(path1) and x < len(path2)):
            if path1[x] == path2[x]:
                common_path.append(path1[x])
            x = x +1
        return common_path

    path1 = find_path(binary_search_tree, 0, elem1, [])
    path2 = find_path(binary_search_tree, 0, elem2, [])

    print "path 1 for " + str(elem1) + " is ", path1
    print "path 2 for " + str(elem2) + " is ", path2
    common_path = find_common_path(path1, path2)
    return common_path[len(common_path)-1] if len(common_path) > 0 else "No common ancestor"

result = least_common_ancestor(binary_search_tree, 10, 13)
print "least common ancestor is ", result
