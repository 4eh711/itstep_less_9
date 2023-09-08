class GenIt:
    def __init__(self,data):
        self.data =data

    def __iter__(self):
        return self.generator()

    def generator(self):
        for item in self.data:
            yield item

list = [1,2,3,4,5,6,7]
iterable = GenIt(list)

for _ in iterable:
    print(_)
