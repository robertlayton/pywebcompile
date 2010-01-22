
class Contents(object):
    """ Contains the contents for one page
    """
    def __init__(self, filename, **args):
        self.filename = filename
        self.properties = args

    def __setattr__(self, key, value):
        if key == 'filename':
            self.filename = value
        else:
            # use __setitem__
            self[key] = value

    def __getattr__(self, key):
        if key == "filename":
            return self.filename
        else:
            return self[key]
        
    def __getitem__(self, item):
        return self.properties[item]

    def __setitem__(self, key, value):
        self.properties[key] = value
