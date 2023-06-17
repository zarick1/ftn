class Node:
    def __init__(self, p = None , l = None , r = None, d = None, v = None):
        self.parent = p
        self.left = l
        self.right = r
        self.data = d
        self.value = v

    def __str__(self):
        return str(self.data)

class Tree:
    def __init__(self, r = None):
        self.root = r

    def insert(self, z):
        y = None
        x = self.root
        while x is not None:
            y = x
            if z.value < x.value:
                x = x.left
            else:
                x = x.right
        z.parent = y
        if y is None:
            self.root = z
        elif z.value < y.value:
            y.left = z
        else:
            y.right = z


    def inorder_tree_walk(self, x):
        if x is not None:
            self.inorder_tree_walk(x.left)
            print(x)
            self.inorder_tree_walk(x.right)

    def search_tree(self, x, letter, val):
        string = ""
        while x is not None and letter != x.data:
            if val < x.value:
                x = x.left
                string += "."
            else:
                x = x.right
                string += "-"
        return string

    def find_character(self, x, string):
        for char in string:
            if char == "-":
                x = x.right
            elif char == ".":
                x = x.left
        return x.data


if __name__ == "__main__":

    dict = {"start":100,
         "E":50, "T":150, "I":25, "A":75, "N":125, "M":175, "S": 12, "U":37, "R":62, "W":87, "D":112, "K":137, "G":162, "O":187,
         "H":6, "V":18, "F":31, "p1":40, "L":55, "p2":70, "P":80, "J":90, "B":105, "X":120, "C":130, "Y":140, "Z":155, "Q":170, "p3":180, "p4":190,
         "5":5,  "4":7,  "p5":17, "3":19,  "p6":30, "p7":32, "p8":39, "2":41, "p9":54, "p10":56, "+":69, "p11":71, "p12":79, "p13":81, "p14":89, "1":91,
        "6":104, "=":106, "/":119,  "p15":121, "p16":129, "p17":131, "p18":139, "p19":141, "7":154, "p20":156, "p21":165, "p22":171, "8":179, " ":181, "9":189, "0":191}

    tree = Tree()
    for key in dict:
        temp = Node(d=key, v=dict[key])
        tree.insert(temp)

    tree.inorder_tree_walk(tree.root)

    input0 = input("unesi ono sto zelis da enkodujes: ")
    #input = "PERA PERIC"
    output = ""
    for char in input0:
        temp = dict[char]
        output += tree.search_tree(tree.root, char, temp)
        output += " "
    print(output.replace("---.-", "/"))


    #input1 = ".--. . .-. .- / .--. . .-. .. -.-. "
    #input11 = input1.replace("/", "---.-")
   #print(input11)
    input1 = input("Unesi ono sto zelis da dekodujes: ")
    input11 = input1.replace("/", "---.-")
    output1 = ""
    temp = ""
    for char in input11:
        if char == " ":
            output1 += tree.find_character(tree.root,temp)
            temp = ""
        else:
            temp += char
    print(output1)
