
class Edge():
    def __init__(self, _from, _to):
        self._from = _from
        self._to = _to

    def __repr__(self):
        # {"from": 0, "to": 1}
        _from = '"from": ' + str(self._from)
        _to = ', "to": ' + str(self._to)
        return '{ ' + _from + _to + ' }'
