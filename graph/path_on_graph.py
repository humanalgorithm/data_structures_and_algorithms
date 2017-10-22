"""
Sets up a graph and then provides the ability to see if there is a path between two nodes on the graph. \
In addition this demo logs all of the possible paths from one node to another.


We will set up the following directed graph as illustrated below:
                 > -------------------------------|
     -> 2  -- > 3                9  <             |
   /                                  \           ?
1 ->  ---> 6 ---> 7                    <-> 10 --> 11
  \                 ->  \            /
    <-> 4 <---> 5          <-> 8 <->

"""
import copy
from . import SetupDemo, print_description

class Node(object):
    def __init__(self, value, up_node=None, down_node=None, middle_node=None, previous_node=None):
        self.up_node = up_node
        self.down_node = down_node
        self.middle_node = middle_node
        self.previous_node = previous_node
        self.value = value
        self.processed = False

class PathChecker(object):
    def check_path(self, node_list, current_node, search_element):

        current_node.processed = True

        if current_node.value == search_element:
            return True

        path_previous = False
        path_up = False
        path_down = False
        path_middle = False

        if current_node.previous_node and not current_node.previous_node.processed:
            path_previous = self.check_path(node_list, current_node.previous_node, search_element)

        if current_node.up_node and not current_node.up_node.processed:
            path_up = self.check_path(node_list, current_node.up_node, search_element)

        if current_node.down_node and not current_node.down_node.processed:
            path_down = self.check_path(node_list, current_node.down_node, search_element)

        if current_node.middle_node and not current_node.middle_node.processed:
            path_middle = self.check_path(node_list, current_node.middle_node, search_element)

        current_node.processed = False
        if path_previous or path_up or path_down or path_middle:
            return True
        return False

    def record_path(self, node_list, current_node, search_element, current_path=[], success_paths=[]):

        current_node.processed = True
        this_path = copy.copy(current_path)
        this_path.append(current_node)

        if current_node.value == search_element:
            success_paths.append([node.value for node in this_path])
            current_node.processed = False
            return this_path

        if current_node.previous_node and not current_node.previous_node.processed:
            self.record_path(node_list, current_node.previous_node, search_element, this_path, success_paths)

        if current_node.up_node and not current_node.up_node.processed:
            self.record_path(node_list, current_node.up_node, search_element, this_path, success_paths)

        if current_node.down_node and not current_node.down_node.processed:
            self.record_path(node_list, current_node.down_node, search_element, this_path, success_paths)

        if current_node.middle_node and not current_node.middle_node.processed:
            self.record_path(node_list, current_node.middle_node, search_element, this_path, success_paths)

        current_node.processed = False


class PathOnGraphDemo(SetupDemo):
    """
    We will set up the following directed graph as illustrated below:
                     > -------------------------------|
         -> 2  -- > 3                9  <             |
       /                                  \           ?
    1 ->  ---> 6 ---> 7                    <-> 10 --> 11
      \                 ->  \            /      ^
        <-> 4 <---> 5          <-> 8 <->        |
                    ?                           |
                    - --------------------------
    """

    def __init__(self):
        super(PathOnGraphDemo, self).setup_demo(__file__)

    def set_up_demo1(self):
        self.node_list = {i: Node(value=i) for i in range(1, 12)}

        self.node_list[1].up_node = self.node_list[2]
        self.node_list[1].down_node = self.node_list[4]
        self.node_list[1].middle_node = self.node_list[6]

        self.node_list[2].middle_node = self.node_list[3]

        self.node_list[3].middle_node = self.node_list[11]

        self.node_list[4].previous_node = self.node_list[1]
        self.node_list[4].middle_node = self.node_list[5]

        self.node_list[5].previous_node = self.node_list[4]
        self.node_list[5].middle_node = self.node_list[10]

        self.node_list[6].middle_node = self.node_list[7]

        self.node_list[7].down_node = self.node_list[8]

        self.node_list[8].previous_node = self.node_list[7]
        self.node_list[8].up_node = self.node_list[10]

        self.node_list[10].up_node = self.node_list[9]
        self.node_list[10].previous_node = self.node_list[8]
        self.node_list[10].middle_node = self.node_list[11]

        return self.node_list

    def _log_path_record(self, paths):
        i = 1
        for path in paths:
            print "Path " + str(i) + ": " + str(path)
            i +=1

    def _log_path_check(self, start_node, search_element, result):
        print "Valid path from " + str(start_node.value) + " to " + str(search_element) + " is " + str(result)

    @print_description
    def check_path_from_5_to_11(self):
        self.node_list = self.set_up_demo1()
        start_node = self.node_list[5]
        search_element = 11
        path_checker = PathChecker()
        result = path_checker.check_path(self.node_list, start_node, search_element=search_element)
        self._log_path_check(start_node, search_element, result)

    @print_description
    def check_path_from_8_to_3(self):
        self.node_list = self.set_up_demo1()
        start_node = self.node_list[8]
        search_element = 3
        path_checker = PathChecker()
        result = path_checker.check_path(self.node_list, start_node, search_element=search_element)
        self._log_path_check(start_node, search_element, result)

    @print_description
    def record_path_from_5_to_11(self):
        self.node_list = self.set_up_demo1()
        path_checker = PathChecker()
        result_path = []
        path_checker.record_path(self.node_list, self.node_list[5], search_element=11, success_paths=result_path)
        self._log_path_record(result_path)

    @print_description
    def record_path_from_1_to_11(self):
        self.node_list = self.set_up_demo1()
        path_checker = PathChecker()
        result_path = []
        path_checker.record_path(self.node_list, self.node_list[1], search_element=11, success_paths=result_path)
        self._log_path_record(result_path)

if __name__ == "__main__":
    graph_demo = PathOnGraphDemo()
    demos_to_run = [graph_demo.check_path_from_5_to_11,
                    graph_demo.check_path_from_8_to_3,
                    graph_demo.record_path_from_5_to_11,
                    graph_demo.record_path_from_1_to_11]
    [func() for func in demos_to_run]
