def snail(map):
    n = len(map)
    if not map or not map[0]:
        return []
    res = []
    visited = set()
    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    cur_dir = 0
    i, j = 0, 0
    for x in range(n * n):
        visited.add((i, j))
        res.append(map[i][j])
        next_i = i + dirs[cur_dir][0]
        next_j = j + dirs[cur_dir][1]
        if (0 <= next_i < n) and (0 <= next_j < n) and (next_i, next_j) not in visited:
            i, j = next_i, next_j
        else:
            cur_dir = (cur_dir + 1) % 4
            i += dirs[cur_dir][0]
            j += dirs[cur_dir][1]
    return res
