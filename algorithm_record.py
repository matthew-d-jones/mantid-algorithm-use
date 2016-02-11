class AlgRecord:

    def __init__(self, name, count, is_child, version):
        self.name = name
        self.count = count
        self.is_child = is_child
        self.version = version

    def get_data_list(self):
        return [self.name, self.count, self.is_child, self.version]
