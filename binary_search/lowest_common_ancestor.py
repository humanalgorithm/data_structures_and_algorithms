
#                     0  1  2 3   4  6   7
#Tree sample #######

# to go left --> index  * 2 +1
# to go right --> index *2 + 2
'''
           15
     10           20
 7     12      17       22
6 9  11 13   16  18   21 23
'''
#[15, 10, 20, 7, 12, 17, 22, 6, 9, 11, 13, 16, 18, 21, 23]

from __init__ import print_description, SetupDemo, print_tree_from_breadth_first_stack

class LowestCommonAncestor(object):

    def __init__(self, binary_search_tree):
        self.binary_search_tree = binary_search_tree

    def _find_path(self, current_root_index, elem, path):
        path.append(self.binary_search_tree[current_root_index])
        if self.binary_search_tree[current_root_index] == elem:
             return

        if elem < self.binary_search_tree[current_root_index]:
            self._find_path(current_root_index*2 + 1, elem, path)

        if elem > self.binary_search_tree[current_root_index]:
            self._find_path(current_root_index*2+2, elem, path)
        return path

    def _find_common_path(self, path1, path2):
        x = 0
        common_path = []
        while (x < len(path1) and x < len(path2)):
            if path1[x] == path2[x]:
                common_path.append(path1[x])
            x = x + 1
        return common_path

    def calculate_lowest_common_ancestor(self, elem1, elem2):
        path1 = self._find_path(0, elem1, [])
        path2 = self._find_path(0, elem2, [])
        print "path 1 for " + str(elem1) + " is ", path1
        print "path 2 for " + str(elem2) + " is ", path2
        common_path = self._find_common_path(path1, path2)
        return common_path[len(common_path)-1] if len(common_path) > 0 else "No common ancestor"


class LowestCommonAncestorDemo(SetupDemo):
    def __init__(self):
        super(LowestCommonAncestorDemo, self).setup_demo(__file__)
        self.binary_search_tree1 = [15, 10, 20, 7, 12, 17, 22, 6, 9, 11, 13, 16, 18, 21, 23]
        self.binary_search_tree2 = [6, 4, 9, 3, 5, 7, 10]

    @print_description
    def lowest_common_ancestor_for_13_and_6(self):
        search_element1 = 13
        search_element2 = 6
        print "Tree for path calculation is: "
        print_tree_from_breadth_first_stack(self.binary_search_tree1)
        print ""
        lowest_common_ancestor = LowestCommonAncestor(self.binary_search_tree1)
        result = lowest_common_ancestor.calculate_lowest_common_ancestor(elem1=search_element1, elem2=search_element2)
        print "Lowest ancestor between " + str(search_element1) + " and " + str(search_element2) + " is " + str(result)

    @print_description
    def lowest_common_ancestor_for_16_and_18(self):
        search_element1 = 16
        search_element2 = 18
        print "Tree for path calculation is: "
        print_tree_from_breadth_first_stack(self.binary_search_tree1)
        print ""
        lowest_common_ancestor = LowestCommonAncestor(self.binary_search_tree1)
        result = lowest_common_ancestor.calculate_lowest_common_ancestor(elem1=search_element1, elem2=search_element2)
        print "Lowest ancestor between " + str(search_element1) + " and " + str(search_element2) + " is " + str(result)

    @print_description
    def lowest_common_ancestor_for_6_and_23(self):
        search_element1 = 6
        search_element2 = 23
        print "Tree for path calculation is: "
        print_tree_from_breadth_first_stack(self.binary_search_tree1)
        print ""
        lowest_common_ancestor = LowestCommonAncestor(self.binary_search_tree1)
        result = lowest_common_ancestor.calculate_lowest_common_ancestor(elem1=search_element1, elem2=search_element2)
        print "Lowest ancestor between " + str(search_element1) + " and " + str(search_element2) + " is " + str(result)


lowest_common_ancestor_demo = LowestCommonAncestorDemo()
demos_to_run = [lowest_common_ancestor_demo.lowest_common_ancestor_for_13_and_6,
                lowest_common_ancestor_demo.lowest_common_ancestor_for_16_and_18,
                lowest_common_ancestor_demo.lowest_common_ancestor_for_6_and_23]
[func() for func in demos_to_run]