import numpy as  np
import random 


class Maze:
    """ A class to define mazes

    """

    # CONSTURCTOR

    def __init__(self, h=20, w=20):
        """ Constructor method

        Args:
            h (int, optional): Height (in nodes) of the maze. Defaults to 20.
            w (int, optional): Width (in nodes) of the maze. Defaults to 20.
        """
        self.h = h
        self.w = w
        self.right_con = np.ones(self.h * self.w, dtype=bool) 
        self.down_con = np.ones((self.h * self.w) - self.w, dtype=bool) 
        self.right_con[self.w-1::self.w] = False
        self.player = 0
        self.start = 0
        self.end = self.w - 1
    
    # MAZE MOVES

    def can_move_left(self):
        """ Checks if the player can move left

        Returns:
            bool: True if they can
        """
        if self.player % self.w == 0:
            return False
        else:
            return self.right_con[self.player-1] 

    def can_move_right(self):
        """ Checks if the player can move right

        Returns:
            bool: True if they can
        """
        return self.right_con[self.player]
    
    def can_move_up(self):
        """ Checks if the player can move up

        Returns:
            bool: True if they can
        """
        if self.player < self.w:
            return False
        else:
            return self.down_con[self.player-self.w]

    def can_move_down(self):
        """ Checks if the player can move down

        Returns:
            bool: True if they can
        """
        if self.player >= self.w*(self.h-1):
            return False
        else:
            return self.down_con[self.player]

    def move_left(self):
        """ Moves the player to the left
        """
        if self.can_move_left():
            self.player -= 1
        # else:
        #     print("Can't do that") # DEBUG

    def move_right(self):
        """ Moves the player to the right
        """
        if self.can_move_right():
            self.player += 1
        # else:
        #     print("Can't do that") # DEBUG

    def move_up(self):
        """ Moves the player up
        """
        if self.can_move_up():
            self.player -= self.w
        # else:
        #     print("Can't do that") # DEBUG
    
    def move_down(self):
        """ Moves the player down
        """
        if self.can_move_down():
            self.player += self.w
        # else:
        #     print("Can't do that") # DEBUG

    # MAZE GENERATION STARTERS

    def recdiv_generation_start(self): 
        """ Starts the generation of a maze using recursive division
        """
        self.start=0
        self.end=self.w*self.h-1
        self.recdiv_generation(0,self.w-1,0,self.h-1)
        self.player=self.start

    # MAZE GENERATION AUXILIAR FUNCTIONS

    def recdiv_generation(self,lbound,rbound,ubound,dbound,horiz=True):
        """ Recursive function for the recursive division maze generation

        Args:
            lbound (int): Left bound of the space to generate the cut
            rbound (int): Right bound of the space to generate the cut
            ubound (int): Upper bound of the space to generate the cut
            dbound (int): Lower bound of the space to generate the cut
            horiz (bool, optional): Does a horizontal cut if True. Defaults to True.
        """
        if horiz:   # Horizontal
            if rbound - lbound >= 1:
                rcut = random.randint(ubound, dbound-1)
                rhole = random.randint(lbound, rbound)
                # print("Horizontal cut on depth "+str(rcut)+" with a hole at " + str(rcut*self.w + rhole))   # DEBUG
                self.down_con[rcut*self.w+lbound:rcut*self.w+rbound+1] = False
                self.down_con[rcut*self.w+rhole] = True
                # print(self.data())  # DEBUG
                # print(str(self))    # DEBUG
                self.recdiv_generation(lbound,rbound,ubound,rcut,False)
                self.recdiv_generation(lbound,rbound,rcut+1,dbound,False)
            # else:
            #     print("Ending for left and right bounds "+str(lbound)+", "+str(rbound)) # DEBUG
        else:       # Vertical cut
            if dbound - ubound >= 1:
                rcut = random.randint(lbound, rbound-1)
                rhole = random.randint(ubound, dbound)
                # print("Vertical cut on width "+str(rcut)+" with a hole at " + str(rcut + self.h*rhole))     # DEBUG
                self.right_con[ubound*self.w+rcut:dbound*self.w+rcut+1:self.w] = False
                self.right_con[rhole*self.w+rcut] = True
                # print(self.data())  # DEBUG
                # print(str(self))    # DEBUG
                self.recdiv_generation(lbound,rcut,ubound,dbound,True)
                self.recdiv_generation(rcut+1,rbound,ubound,dbound,True)
            # else:
            #     print("Ending for up and down bounds "+str(ubound)+", "+str(dbound)) # DEBUG

    # MAZE DATA

    def __str__(self):
        """ Gives a string representation of the maze state

        Returns:
            str: Maze representation
        """
        ret = "+"
        for w in range(0, self.w):
            ret += "---+"
        for h in range(0, self.h):
            ret += "\n|"
            for w in range(0, self.w):
                if self.right_con[h*self.w+w]:
                    if h*self.w+w == self.player:
                        ret += " P  "
                    elif h*self.w+w == self.end:
                        ret += " E  "
                    elif h*self.w+w == self.start:
                        ret += " S  "
                    else:
                        ret += "    "
                else:
                    if h*self.w+w == self.player:
                        ret += " P |"
                    elif h*self.w+w == self.end:
                        ret += " E |"
                    elif h*self.w+w == self.end:
                        ret += " S |"
                    else:
                        ret += "   |"
            ret += "\n+"
            if h != self.h-1:
                for w in range(0, self.w):
                    if self.down_con[h*self.w+w]:
                        ret += "   +"
                    else:
                        ret += "---+"
            else:
                for w in range(0, self.w):
                    ret += "---+"
        return ret
    
    def data(self):
        """ Useful data about the maze 

        Returns:
            str: Data about the maze
        """
        ret ="width: "+str(self.w)+" height: "+str(self.h)
        ret+="\nRight connections: "+str(self.right_con)
        ret+="\nDown connections: "+str(self.down_con)
        return ret

    def has_ended(self):
        """ Checks if the player has finished the maze

        Returns:
            bool: True if the player has ended the maze
        """
        return self.player == self.end