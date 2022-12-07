class treeNode:
    
    def __init__(this):
        this.size = 0
        this.parentNode = None
        this.childNodes = {}
        pass
            
    def get_node(this, nodeName):
        if not nodeName in this.childNodes.keys():
            raise IndexError("Invalid node located")
        return this.childNodes[nodeName]

    def update_size(this, size):
        this.size += size
        if not this.parentNode == None:
            this.parentNode.update_size(size)

    def set_node(this, nodeName, node):
        node.parentNode = this
        this.childNodes[nodeName] = node
        this.update_size(node.size)
        return this
    
    def remove_node(this, nodeName):
        del this.childNodes[nodeName]
        return this

    def has_node(this, nodeName):
        return nodeName in this.childNodes.keys()

class fileNode(treeNode):
    def __init__(this, size, name):
        super().__init__()
        this.size = size
        this.name = name
        this.childNodes = {}
    
    def printNode(this):
        print("|"*this.printLevel, end="")
        print(f"-{this.name}: {this.size}")

class folderNode(treeNode):
    def __init__(this, path):
        super().__init__()
        this.printLevel = 0
        this.path = path

    def printNode(this):
        print("|"*this.printLevel+": " + f"{this.size}", end="")
        print("-"+this.path)
        for node in this.childNodes.keys():
            this.childNodes[node].printLevel = this.printLevel + 1
            this.childNodes[node].printNode()
            
    
    def get_or_create_subfolder(this, path):
        if len(path.split("/")) == 1:
            return this
        if this.has_node(path.split("/")[0]):
            return this.get_node(path.split("/")[0]).get_or_create_subfolder("/".join(path.split("/")[1:]))
        this.set_node(path.split("/")[0], folderNode(path.split("/")[0]))
        return this.get_node(path.split("/")[0]).get_or_create_subfolder("/".join(path.split("/")[1:]))
        


def handleCDCommand(command, baseTree, currentPath:str):
    path = command.split(" ")[1]
    if path == "/":
        return (baseTree, "")
    if path == "..":
        upPath = "/".join(currentPath.split("/")[:-2])
        if not upPath == "":
            upPath += "/"
        return (baseTree, upPath)
    currentPath += path + "/"
    baseTree.get_or_create_subfolder(currentPath)

    return (baseTree, currentPath)

def handleLSCommand(fileList, baseTree, currentPath):
    folder = baseTree.get_or_create_subfolder(currentPath)
    for item in fileList:
        if item.startswith("dir"):
            continue
        size = int(item.split(" ")[0])
        name = item.split(" ")[1]
        folder.set_node(name, fileNode(size, name))

def handleCommandAndOutput(commandAndOutput, baseTree, currentPath):
    command = commandAndOutput[0]
    match command.split(" ")[0]:
        case "cd":
            return handleCDCommand(command, baseTree, currentPath)
        case "ls":
            handleLSCommand(commandAndOutput[1:], baseTree, currentPath)
            return (baseTree, currentPath)
        case _:
            ...

def get_folder_sizes(node, sizes):
    sizes.append((node.path, node.size))
    for child in node.childNodes.keys():
        if isinstance(node.childNodes[child], folderNode):
            sizes = get_folder_sizes(node.childNodes[child], sizes)
    return sizes

def sortBySize(node):
    return node[1]

with open("input.txt","r") as input:
    input = input.read().split("$")[1:]
    fileTree = folderNode("/")
    currentPath = ""
    for command in input:
        commandAndOutput = [line.strip() for line in command.split("\n")][:-1]
        (fileTree, currentPath) = handleCommandAndOutput(commandAndOutput, fileTree, currentPath)

    sizes = get_folder_sizes(fileTree, [])
    sizeOfCombinedSmaller = sum([size[1] for size in sizes if size[1] <=100000])
    print(sizeOfCombinedSmaller)
    updateSize = 30000000
    sizeLeft = 70000000-fileTree.size
    neededSize = updateSize-sizeLeft
    sizes.sort(key=sortBySize)
    for size in sizes:
        if size[1] > neededSize:
            print(size[1])
            break