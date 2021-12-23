import numpy as np

class Pattern:
    def __init__(self):
        self.known = {'glider' : [(20, 20), (21, 20), (22, 20), (22, 19), (21, 18)],
                      'acorn' : [(90, 70), (91, 70), (91, 68), (93, 69), (94, 70), (95, 70), (96, 70)],
                      'diehard' : [(90, 69), (91, 70), (91, 69), (95, 70), (96, 70), (96, 68), (97, 70)],
                      'cros' : [(72, 72), (73, 73), (74, 74), (75, 75), (76, 76), (77, 77), (78, 78),
                                (72, 78), (73, 77), (74, 76),           (76, 74), (77, 73), (78, 72)],
                      'v' : [(72, 72), (73, 73), (74, 74), (75, 75), (76, 74), (77, 73), (78, 72)]}

        self.rand = {'small_random': [range(50), 70, 80], 
                     'full_random': [range(7500), 0, 150]}

        self.rock = [(0, 1),   (0, 2),   (0, 10),  (0, 11),
                     (4, 3),   (4, 4),   (4, 5),   (4, 7),   (4, 8),  (4, 9),
                     (1, 0),   (2, 0),   (3, 0),   (4, 0),   (5, 0),  (6, 0),  (7, 0),  (8, 0),  (9, 0), (10, 0), (11, 0), (12, 0),
                     (1, 3),   (2, 3),   (3, 3),   (4, 3),   (5, 3),  (6, 3),  (7, 3),  (8, 3),
                     (5, 6),   (6, 6),   (7, 6),   (8, 6),
                     (1 ,9),   (2 ,9),   (3 ,9),   (4 ,9),   (5 ,9),  (6 ,9),  (7 ,9),  (8 ,9),
                     (1 ,12),  (2 ,12),  (3 ,12),  (4 ,12),  (5 ,12), (6 ,12), (7 ,12), (8 ,12),
                     (8, 6),   (8, 7),   (8, 8),   (8, 9),   (8, 10), (8, 11), (8, 12),
                     (9, 4),   (9, 5),
                     (10, 5),
                     (11, 6),  (11, 7),  (11, 8),
                     (9, 13),  (10, 13), (11, 13), (12, 13),
                     (13, 1),  (14, 1),
                     (13, 12), (14, 12),
                     (15, 2),
                     (15, 11),
                     (16, 3),  (16, 4),  (16, 5),  (16, 6),  (16, 7), (16, 8), (16, 9), (16, 10),
                     (18, 3),  (18, 4),  (18, 5),  (18, 6),  (18, 7), (18, 8), (18, 9), (18, 10),]
                      
    def build(self, pattern):
        self.board = np.full((150,150), 0)

        if pattern in self.known.keys():
            for i in self.known[pattern]:
                self.board[i] = 1

        elif pattern in self.rand.keys():
            rand_patt = self.rand[pattern]
            for i in rand_patt[0]:
                row = np.random.randint(rand_patt[1], rand_patt[2])
                col = np.random.randint(rand_patt[1], rand_patt[2])
                self.board[row, col] = 1

        elif pattern == 'rock':
            self.rock_board = np.full((20, 20), 0)
            for i in self.rock:
                self.rock_board[i] = 1
            
            for x in range(self.rock_board.shape[0]):
                for y in range(self.rock_board.shape[1]): 
                    if self.rock_board.T[x, y] == 1:
                        self.board[x + 67, y + 67] = 1

        return self.board