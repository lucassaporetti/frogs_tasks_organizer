class Entity:
    def __init__(self, id: str = None):
        self.id = id

    def __str__(self):
        return "{}".format(self.id)

    def to_dict(self) -> dict:
        ret_dict = {}
        for key, value in self.__dict__.items():
            if isinstance(value, int):
                ret_dict[key] = int(value)
            elif isinstance(value, float):
                ret_dict[key] = float(value)
            elif isinstance(value, bool):
                ret_dict[key] = bool(value)
            else:
                ret_dict[key] = str(value)
        return ret_dict
