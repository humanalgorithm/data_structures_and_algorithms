class TreeLevelVisit(object):
    def tree_level_visit_node(self, current):
        stack = []
        if current == None:
            return

        stack.append(current)
        stack.append(current.left)
        stack.append(current.right)

        for i in range(1, len(stack)):
            stack.append(stack[i].left)
            stack.append(stack[i].right)

        return [node for node in stack]

    def tree_level_visit_element(self, bst_array):
        if bst_array == None:
            return None

        def _get_left(bst_array, index):
            # to go left --> index  * 2 +1
            computed_index = index * 2 + 1
            if computed_index+1 <= len(bst_array):
                return bst_array[computed_index]
            else: return None

        def _get_right(bst_array, index):
            # to go right --> index *2 + 2
            computed_index = index* 2 + 2
            if computed_index+1 <= len(bst_array):
                return bst_array[computed_index]
            else: return None

        stack = []
        if len(bst_array) == 0:
            return

        stack.append(bst_array[0])
        stack.append(_get_left(bst_array, index=0))
        stack.append(_get_right(bst_array, index=0))

        for i in range(1, len(stack)):
            stack.append(stack[i])
            stack.append(_get_left(stack, index=i))
            stack.append(_get_right(stack, index=i))
        return stack
