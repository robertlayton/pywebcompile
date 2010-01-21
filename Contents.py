
class Contents(object):
    """ Contains the contents for one page
    """
    def __init__(self, filename, **args):
        self.filename = filename
        self.parameters = args

    def __getitem__(self, item):
        return self.parameters[item]

    def __setitem__(self, key, value):
        self.parameters[key] = value
