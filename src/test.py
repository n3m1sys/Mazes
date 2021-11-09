import maze
import os

def play():
    """ Simple function to play the generated maze.
    """
    m = maze.Maze(20,20)
    m.recdiv_generation_start()
    os.system("clear")
    while(not m.has_ended()):
        print(m)
        key = False
        while(not key):
            key = True
            uinput= input("\nEntrada:\nw := arriba\na := izquierda\ns := abajo\nd := derecha\n")
            if uinput[-1] == "w" or uinput[-1] == "W":
                m.move_up()
            elif uinput[-1] == "a" or uinput[-1] == "A":
                m.move_left()
            elif uinput[-1] == "s" or uinput[-1] == "S":
                m.move_down()
            elif uinput[-1] == "d" or uinput[-1] == "D":
                m.move_right()
            else:
                print("INVALID INPUT")
                key = False
        # sys.stdout.flush()
        os.system("clear")
    print(m)
    print("\n YOU WIN!!! ")

def dfs_test():
    """ Executes the Deep First Search algorithm over a random maze.
    """
    import ai.dfs as ai
    bfs = ai.DFS()
    bfs.start()

def bfs_test():
    """ Executes the Best First Search algorithm over a random maze.
    """
    import ai.bfs as ai
    bfs = ai.BFS()
    bfs.start()

def main():
    """ Main function, call here the functions to run the different algorithms
    or play a random maze.
    """
    # play()
    # dfs_test()
    bfs_test()


if __name__ == "__main__":
    main()