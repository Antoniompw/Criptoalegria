KEY_LENGTH = 7

def matrice_creator(filename):
    mats = []
    with open(filename) as f:
        line = 1
        while(line != ''):
            mat = []
            for _ in range(KEY_LENGTH):
                line = f.read(KEY_LENGTH)
                mat.append(line)
            mats.append(mat)
    return mats

def matrice_norm(matrices):
    for mat in matrices:
        for line, index in zip(mat, range(len(mat))):
            line = list(line)
            while len(line) != KEY_LENGTH:
                line.append(' ')
            mat[index] = line
    return matrices

def transposition(mat, key):
    new_mat = [[None] * KEY_LENGTH for _ in range(KEY_LENGTH)]
    for i in key:
        for j in range(len(key)):
            new_mat[i][j] = mat[j][i]
    return new_mat

def de_transposition(mat, key):
    new_mat = [[None] * KEY_LENGTH for _ in range(KEY_LENGTH)]
    for i in key:
        for j in range(len(key)):
            new_mat[j][i] = mat[i][j]
    return new_mat

filename = "test.txt"        
key = [5,2,1,4,6,3,0]
stages = range(3)
matrices = matrice_creator(filename)
matrices = matrice_norm(matrices)

for i, index in zip(matrices,range(len(matrices))):
    for _ in stages:
        i = transposition(i, key)
        matrices[index] = i

with open("encripted.txt", "w+") as f:
    for i in matrices:
        for j in i:
            for k in j:
                f.write(k)

for i, index in zip(matrices,range(len(matrices))):
    for _ in stages:
        i = de_transposition(i, key)
        matrices[index] = i

with open("deencripted.txt", "w+") as f:
    for i in matrices:
        for j in i:
            for k in j:
                f.write(k)