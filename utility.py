import textwrap
import sys
import os.path
import json

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir)))

def print_description(func):
    func_description_headings = ["Title", "Input Data", "Description"]
    class_description_headings = ["Demo Class Name", "Description"]

    def _get_descriptions_from_json(json_path, classname_key, description_key):
        with open(json_path) as data_file:
            data = json.load(data_file)
            return data[classname_key][description_key]

    def print_description_to_console(description_dict, demo_class_description=False):
        _print_separator()
        headings = func_description_headings if not demo_class_description else class_description_headings

        for key in headings:
            line = key + ": " + str(''.join(description_dict[key]))
            print textwrap.fill(line, width=96)
            print ""

    def _print_separator():
        print "" * 64
        print ":" * 64
        print "" * 64

    def _get_descriptions_file_location(file):
        file_path = os.path.abspath(os.path.join(file))
        directory_path = os.path.dirname(file_path)
        descriptions_path = os.path.join(directory_path, "descriptions")
        descriptions_json = os.path.join(descriptions_path, "descriptions.json")
        return descriptions_json

    def _print_class_description(self, json_descriptions_file):
        if not self.class_description_printed:
            class_description_dict = _get_descriptions_from_json(json_path=json_descriptions_file,
                                                                classname_key=self.__class__.__name__,
                                                                description_key="demo_class_description")
            print_description_to_console(class_description_dict, demo_class_description=True)
            self.class_description_printed = True

    def _print_function_descriptions(self, json_descriptions_file):
        function_description_dict = _get_descriptions_from_json(json_path=json_descriptions_file,
                                                               classname_key=self.__class__.__name__,
                                                               description_key=func.__name__)
        print_description_to_console(function_description_dict)

    def _print_class_and_function_descriptions(self):
        json_descriptions_file = _get_descriptions_file_location(self.__file__)
        _print_class_description(self, json_descriptions_file)
        _print_function_descriptions(self, json_descriptions_file)

    def wrapper(self):
        _print_class_and_function_descriptions(self)
        func(self)
    return wrapper

class SetupDemo(object):
    def setup_demo(self, file):
        self.__file__ = file
        self.description_map = self.__class__.__name__
        self.class_description_printed = False