def likelihood():
    likelihood = (50, 38, 27, 99, 5)
    return min(likelihood), max(likelihood)


def run_task1():
    display = likelihood()
    print(f"Maximum likelihood of falling: {display[0]}%")
    print(f"Maximum likelihood of falling: {display[1]}%")


if __name__ == "__main__":
    run_task1()

