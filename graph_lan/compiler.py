from matplotlib import pyplot as plt
available_graphs = [
    "LINE",
    "BAR",
    "PIE",
    "SCATTER",
    "AREA",
    "HISTOGRAM",
]


class run():
    def __init__(self, filename):
        self.f = open(filename, 'r')
        self.text = self.f.read()
        self.lines = self.f.readlines()
        self.f.close()

    def run(self):
        tokens = self.text.split(";")
        for i in tokens:
            i = i.split(":")
            print()
            if i[0] == "GRAPH":
                self.draw(tokens, i[1])

    def draw(self, tokens, graph):
        token = tokens
        for i in range(len(token)):
            token[i] = tokens[i].replace("\n", "")
        for i in tokens:
            ii = i.split(":")
            if ii[0] == "DATA":
                j = ii[1].split(",")
                keys = []
                values = []
                j.pop(len(j) - 1)
                for kk in range(len(j)):

                    keys.append(j[kk].split("-")[0])
                    values.append(int(j[kk].split("-")[1]))
                if len(keys) != len(values):
                    print("Error: Data not in correct format")
                    return ValueError
                data = [keys, values]

            if i.split(":")[0] == "TITLE":
                title = i.split(":")[1]
            if i.split(":")[0] == "XL":
                x_axis = i.split(":")[1]
            if i.split(":")[0] == "YL":
                y_axis = i.split(":")[1]

        compiled_to_python_code = f"""try:
    from matplotlib import pyplot as plt
except:
    if __name__ == "__main__":
        pip.main(['install', "matplotlib"])

plt.{graph.lower()}({data[0]}, {data[1]})
plt.title('{title}')
plt.xlabel('{x_axis}')
plt.ylabel('{y_axis}')
plt.show()
"""
        with open("compiled.py", "w") as f:
            f.write(compiled_to_python_code)
