def movements():
    path=[ "Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path

def run_task2():
    print("Moving...")
    path1=movements()
    for i in range(0,len(path1),2):
        print(i,path1[i])


if __name__ == "__main__":
    run_task2()