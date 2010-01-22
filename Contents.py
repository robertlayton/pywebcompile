
class Contents(object):
    """ Contains the contents for one page
    """
    def __init__(self, filename, **args):
        self.filename = filename
        self.properties = args

    def __in__(self, item):
        return item in self.properties
    
    def __getitem__(self, item):
        if item == 'filename':
            return filename
        else:
            return self.properties[item]

    def __setitem__(self, key, value):
        self.properties[key] = value

