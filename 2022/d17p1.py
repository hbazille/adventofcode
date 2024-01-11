import numpy as np 

SIZE = 4000

rock1 = np.array([[1,1,1,1]], dtype = bool)
rock2 = np.array([[0,1,0],[1,1,1],[0,1,0]], dtype = bool)
rock3 = np.array([[1,1,1],[0,0,1],[0,0,1]], dtype = bool)
rock4 = np.array([[1],[1],[1],[1]], dtype = bool)
rock5 = np.array([[1,1],[1,1]], dtype = bool)
rocks = [rock1, rock2, rock3, rock4, rock5]

allrocks = np.zeros((SIZE, 7), dtype = bool)

def place(rock, allrocks, x, y, highest):
    h, w = rock.shape
    allrocks[y:y+h, x:x+w] = allrocks[y:y+h, x:x+w] | rock
    if highest < y+h:
        return y+h
    return highest
    
def lateral(rock, x):
    h, w = rock.shape
    return not( x < 0 or x+w > 7)
    
def collide(rock, allrocks, x, y):
    h, w = rock.shape
    return y < 0 or (allrocks[y:y+h, x:x+w] & rock).any()


if __name__ == '__main__':  
    file1 = open('data/day17', 'r')
    line = file1.readlines()[0][:-1]
    n = len(line)
    highest = 0
    t = 0
    for i in range(2022):
        rock = rocks[i % 5]
        x, y = 2, highest + 3
        while True:
            wind = 1 if line[t] == ">" else -1
            t = (t + 1) % n
            if lateral(rock, x + wind) and not collide(rock, allrocks, x + wind, y):
                x = x + wind
            if collide(rock, allrocks, x, y - 1):
                break
            y -= 1
        highest = place(rock, allrocks, x, y, highest)
    print(highest)
