from queue import Queue


def maxAreaOfIsland(grid: list):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    rows = len(grid)
    cols = len(grid[0])
    maxArea = 0
    visited = [[0 for i in range(cols)] for j in range(rows)]
    q = Queue()
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1 and visited[row][col] == 0:  # 如果ij是1并且没访问过
                visited[row][col] = 1
                area = 1  # 当前最大面积是area 1
                q.put((row, col))
                while q.empty() != True:
                    loca = q.get()
                    X = [1, -1, 0, 0]
                    Y = [0, 0, 1, -1]
                    for i in range(4):
                        nowRow = loca[0] + X[i]
                        nowCol = loca[1] + Y[i]
                        if nowRow >= 0 and nowRow < rows and nowCol >= 0 and nowCol < cols and visited[nowRow][nowCol] == 0\
                                and grid[nowRow][nowCol]==1:
                           area += 1
                           visited[nowRow][nowCol] = 1
                           q.put((nowRow,nowCol))
                if maxArea < area:
                    maxArea = area
    return maxArea

l = [[1,1,0,0,0],[1,1,0,0,0],[0,0,0,1,1],[0,0,0,1,1]]
print(maxAreaOfIsland(l))