import numpy as np
from enum import Enum
RIGHT=0
UP=1
LEFT=2
DOWN=3

class Snake():
    def __init__(self, screen_size, table: np.ndarray):
        self.len=2
        self.dir=RIGHT
        self.pos=np.array([screen_size[0]//2, screen_size[1]//2])
        self.body=[self.pos,self.pos+[0,-1]]
        print(self.body)

        table[self.body[0][0],self.body[0][1]]=1
        table[self.body[1][0],self.body[1][1]]=1
        print(table[screen_size[0]//2, screen_size[1]//2])

        
    
    def write_body(self, new_pos, table:np.ndarray):
        self.body.insert(0, new_pos)
        
        if table[new_pos[0],new_pos[1]]==1:
            return 0
        if table[new_pos[0],new_pos[1]]==2:

            table[new_pos[0],new_pos[1]]=1
            self.pos=new_pos
            self.len+=1
            return 2
        else:
            clear=self.body.pop()
            table[clear[0],clear[1]]=0
            table[new_pos[0],new_pos[1]]=1
            self.pos=new_pos
            return 1
    
    def change_dir(self, new_dir):
        if (new_dir+self.dir)%2!=0:
            self.dir=new_dir

    def step(self, table: np.ndarray):
        
        if self.dir==LEFT:
            out=self.write_body(self.pos+[0,-1],table)
        elif self.dir==UP:
            out=self.write_body(self.pos+[-1,0],table)
        elif self.dir==RIGHT:
            out=self.write_body(self.pos+[0,1],table)
        elif self.dir==DOWN:
            out=self.write_body(self.pos+[1,0],table)

        if not out:
            print("Lost")
        return out