import sys
import textwrap
import sys
import os.path
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

def print_description(func):
    headings = ["Title", "Input Data", "Description"]

    def get_descriptions_from_json(json_path, classname_key, function_key):
        with open(json_path) as data_file:
            data = json.load(data_file)
            return data[classname_key][function_key]

    def print_to_console(description_dict):
        print_separator()
        for key in headings:
            line = key + ": " + str(''.join(description_dict[key]))
            print textwrap.fill(line, width=96)
            print ""

    def print_separator():
        print "" * 64
        print ":" * 64
        print "" * 64

    def get_descriptions_file_location(file):
        file_path = os.path.abspath(os.path.join(file))
        directory_path = os.path.dirname(file_path)
        descriptions_path = os.path.join(directory_path, "descriptions")
        descriptions_json = os.path.join(descriptions_path, "descriptions.json")
        return descriptions_json

    def wrapper(self):
        json_descriptions_file = get_descriptions_file_location(self.__file__)
        function_description_dict = get_descriptions_from_json(json_path=json_descriptions_file,
                                                               classname_key=self.__class__.__name__,
                                                               function_key=func.__name__)
        print_to_console(function_description_dict)
        func(self)

    return wrapper


class SetupDemo(object):
    def setup_demo(self, file):
        self.__file__ = file
        self.description_map = self.__class__.__name__


