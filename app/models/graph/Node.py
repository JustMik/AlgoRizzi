
class Node():
    def __init__(self, id, label=None, title=None, shape='dot'):
        self.id = id
        self.label = label
        self.title = title
        self.shape = shape

    def __repr__(self):
        id = ('"id": ' + str(self.id))
        label = (' , "label": "' + str(self.label) + '"') if self.label else ''
        shape = (' , "shape": "' + str(self.shape) + '"')
        title = (' , "title": "' + str(self.title) + '"') if self.title else ''
        return '{ ' + id + label + shape + title + '}'
