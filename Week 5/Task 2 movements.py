def movements():
    path=[ "Move Forward", 10, "Move Backward", 5, "Move Left", 3, "Move Right", 1]
    return path

def run_task2():
    print(movements())
    m=movements()
    print(f"Direction: {m[0]}, Steps:{m[1]}")
    print(f"Direction: {m[2]}, Steps:{m[3]}")
    print(f"Direction: {m[4]}, Steps:{m[5]}")

if __name__ == "__main__":
    run_task2()