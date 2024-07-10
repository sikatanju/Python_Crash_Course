# * Making a custom containers (e.g. list, dictionaries, etc.)
# *** Under the hood, we may be using more than one data structure

# ** The goal is to make it to our liking. 

class TagCloud:
    def __init__(self):
        self.__tags = {}

    def add(self, tag):
        self.__tags[tag.lower()] = self.__tags.get(tag.lower(), 0) + 1

    def __getitem__(self, tag):
        return self.__tags.get(tag.lower(), 0)
    
    def __setitem__(self, key, value):
        self.__tags[key.lower()] = value

    def __len__(self):
        return len(self.__tags)
    
    def __iter__(self):
        return iter(self.__tags)


cloud = TagCloud() 
cloud.add('py')
cloud.add('py')
cloud.add('Py')

# print(cloud.tags)
# print(cloud['py'])
# cloud['js'] = 3

# print(len(cloud))

# *** To see all the attributes of a class (including private ones):
# print(cloud.__dict__)
# print(cloud._TagCloud__tags)
