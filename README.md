# data_structures_and_algorithms
Fun with data structures, algorithms and more

## What is it?
This repository is designed to help in the teaching and undestanding of various data structures, algorithms and coding problems. 

Within each folder you will find a python file with the name of a data structure, algorithm or coding problem. Each one of these files
contains the a class that implements the data structure or algorithm and a demo class that prepares data, prints the description and
runs the class in focus. 

For example the binary_search_tree.py file contains a BinarySearchTree class and a BinarySearchTreeDemo class that sets up data and runs the
BinarySearchTree class. 

## How To Run It
From within the data_structures_and_algorithms folder run the following command:
```
python -m <folder_name>.<file_name>
```

For example in order to run the binary search tree demo:
```
python -m binary_search.binary_search_tree
```

## How  Does It Work?
Each demo follows the below flow: 

demo class instantiates object class --> 

demo class invokes print_description decorator -->

print_description decorator looks at descriptions.json of the class that is calling it -->

there is a descriptions.json within the descriptions folder of each demo folder in this repo. -->

descriptions are printed to the screen along with output of run

## Folder Structure
```
data_structures_and_algorithms/
  <algorithm area>/
    <descriptions folder>/
      descriptions.json
  <algorithm area>/
    <descriptions folder>/
      descriptions.json
   ...
utility/
  print_decorator.py
  print_tree.py
  setup.py
```

## How To Add To It
In order to add a new demo you must do the following 3 steps:
1) Add your demo function in the proper demo class
2) Update the associated descriptions.json
3) Add your function to the list of demos_to_run within the same file.

### How to Add a Demo Example: 
Let's say you want to add a new demo to stack.py (located in queues_and_stacks/stacks.py)
1) Add your class to the demo class
```
    @print_description
    def push_four_then_pop_four(self):
        stack = FILOStack()
        ...
            
    @print_description
    def my_function_to_run(self):
      print "my function"

```
2) Update the descriptions.json in the same folder (located in queues_and_stacks/descriptions/descriptions.json)
```
  "StackDemo": {
    "demo_class_description": {
      "Demo Class Name": "StackDemo",
      "Description": ["..."]
    },
    "push_five_items_then_pop_five_items": {
     ...
    },
    "push_four_then_pop_four": {
     ...
    },
   "my_function_to_run"
    {
     "Title": "My Title", 
     "Input Data": "my input data",
     "Description: ["my description]
    }
  }
```
3) Add your demo function to the list of functions to run at the end of the file:
```
if __name__ == "__main__":
    stack_demo = StackDemo()
    demos_to_run = [stack_demo.push_five_items_then_pop_five_items, stack_demo.push_four_then_pop_four,
    stack_demo.my_function_to_run]
    [func() for func in demos_to_run]
```
That's it, then just run python -m queues_and_stacks.stack

## Structure of description JSON files
There is a descriptions folder for every algorithm area folder in the repo. The descriptions.json contains all of the descriptions
of all the demos in that folder. The folder of these json files is as follows:
```
{
  "<DemoClassName>": {
    "demo_class_description": {
      "Demo Class Name": "<your demo class name>",
      "Description": [
        "<Your description goes here>"
      ]
    },
    "<demo function name>": {
      "Title": "<your demo function title>",
      "Input Data": "<your input data here>",
      "Description": ["<your description here>"]
    },
   "<demo function name 2>": {
      "Title": "<your demo 2 function title>",
      "Input Data": "<your input data here>",
      "Description": ["<your description here>"]
    }
  } 
}
```

## print_description Decorator
The print_description decorator is implemented in data_structures_and_algorithms/utility/print_decorator.py
This decorator inspects the function that called it, gets its location and then reads from the description.json that is in the 
folder of the invoking class. 

For example if you put a @print_decorator on top of a function in /binary_search/binary_search_tree.py the decorator will look for descriptions in binary_search/descriptions/descriptions.json

## Binary Search Tree Print
In utility/print_tree.py there is a utility that is used for printing out binary search trees. it works by calculating the 
amount of spaces and offset increasing in proportion to the level of the tree that it is printing. In order to use it, call it
with a binary search tree that is ordered in depth first traversal order. It is currently compatible printing a binary search 
tree from an array as well as from connected node objects. 

## SetupDemo class
In utility/setup.py there is a class called SetupDemo, all of the demos in this repo extend this class in order to commonize the setting of file paths for use with the print_decorator.

