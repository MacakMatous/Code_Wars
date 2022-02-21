def snail(snail_map):
    dimension = len(snail_map)
    path = []
    
    if not snail_map[0]:
        return path
    elif dimension == 1:
        path.extend(snail_map[0])
        return path
    else:
    
        for j in range(1, dimension):
            row = j - 1
            for i in range(j - 1, dimension - j + 1):
                path.append(snail_map[row][i])

            col = dimension - j
            for i in range(j, dimension - j + 1):
                path.append(snail_map[i][col])

            row = dimension - j
            for i in range(j - 1, dimension - j).__reversed__():
                path.append(snail_map[row][i])

            col = j - 1
            for i in range(j, dimension - j).__reversed__():
                path.append(snail_map[i][col])
        return(path)
