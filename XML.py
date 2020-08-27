# XML 1 - Find the score 

def get_attr_number(node):
    attribcount = len(node.attrib)
    for i in node:
        attribcount += get_attr_number(i)
    return attribcount
	
# XML 2 - Find the maximum depth 

maxdepth = -1

def depth(elem, level):
    global maxdepth
    if (level == maxdepth):
        maxdepth += 1

    for child in elem:
        depth(child, level + 1)
