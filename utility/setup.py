class SetupDemo(object):
    def setup_demo(self, file):
        self.__file__ = file
        self.description_map = self.__class__.__name__
        self.class_description_printed = False