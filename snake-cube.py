turns = [0, 0, 1, 1, 1, 0, 1, 1, 0, 1, 1, 1,\
         0, 1, 0, 1, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0]

(X, Y, Z) = (0, 1, 2)
(U, D) = (1, -1)

def other_dims(dim):
    if dim == X:
        return [(Y, U), (Y,D), (Z,U), (Z,D)]
    elif dim == Y:
        return [(X, U), (X, D), (Z,U), (Z,D)]
    else: #dim == Z
        return [(X, U), (X, D), (Y,U), (Y,D)]

def print_sol(sol):
    nxt_pos = list(origin)
    for nxt in sol:
        print nxt_pos,
        nxt_pos[nxt[0]] += nxt[1]
    print nxt_pos

def place_next(i, prv_pos, prv, sol, visited):

    cur_pos = list(prv_pos)
    cur_pos[prv[0]] += prv[1]
    cur_pos = tuple(cur_pos)

    if cur_pos[prv[0]] < 0 or cur_pos[prv[0]] > 2:
        # print "Out of bound"
        return
    if cur_pos in visited:
        # print "Occupied"
        return

    i += 1
    visited[cur_pos] = 1
    sol.append(prv)

    if len(visited) == 3*3*3:
        print "Found solution:"
        print_sol(sol)
        exit(0)

    if turns[i] == 1:
        for n in other_dims(prv[0]):
            # print "Turning", n
            place_next(i, cur_pos, n, sol, visited)
    else:
        # print "No turning"
        place_next(i, cur_pos, prv, sol, visited)

    del visited[cur_pos]
    del sol[-1]
    
for x in range(3):
    for y in range(3):
        z = 2
        origin = (x, y, z)
        nxt = (Z, D)
        place_next(0, origin, nxt, [], {origin:1})
