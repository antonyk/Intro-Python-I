class Store:
    def __init__(self, name, categories):
        self.name = name
        self.categories = categories

    def __str__(self):
        result = f"{self.name}:"
        for i, v in enumerate(self.categories):
            result += f"\n  {i+1}: {v}"

        result += f"\n--------------"
        result += f"\n  {len(self.categories)+1}: Exit"

        return result

    def __repr__(self):
        pass


mystore = Store('Daves Emporium', ['shoes', 'bags', 'pants'])
print(mystore)


l = [1, 2, 3, 4, 5]
a, *b, c = l

print(a, b, c)

# a, *b = l
