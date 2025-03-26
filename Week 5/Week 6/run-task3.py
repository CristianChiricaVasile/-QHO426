def steps():
    likelihood = [("step 1", 50), ("step 2", 38), ("step 3", 27), ("step 4", 99), ("step 5", 5)]
    return likelihood

def run_task():
    display_steps = steps()
    good_steps = []
    bad_steps = []

    for step in display_steps:
        if step[1] > 50:
            bad_steps.append(step)
        else:
            good_steps.append(step)

    print(f"Total good steps: {len(good_steps)}, Total bad steps: {len(bad_steps)}")

if __name__ == "__main__":
    run_task()