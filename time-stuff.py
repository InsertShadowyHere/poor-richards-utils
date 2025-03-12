"""
Basic method to time a function

"""
import time

def do_something(a, b):
    c = a * b
    d = c * b + a
    e = b ** c + b - a * c
    return e


def time_me(func, *args, reps=1000000):
    start = time.time()
    func(*args)
    end0 = time.time() - start
    start = time.time()
    for _ in range(reps):
        func(*args)
    end = time.time()
    end1 = (end-start)/reps
    print(f"Timed {func.__name__} with params {args}.")
    print(f"On average, it took {(end - start)/reps} ms per call over {reps} calls.")
    print(f"However, when run the first time, it took {end0} ms.")
    print(f"That means it took {round(end0/end1, 5)} times longer the first time.")

x = "nop"
if __name__ == "__main__":
    time_me(print, f"{x}+1=2")
    #time_me(print, "{}+1=2".format(x))
"""
Timed print with params ('nop+1=2',).
On average, it took 1.4878578186035157e-06 ms per call over 1000000 calls.
However, when run the first time, it took 1.1920928955078125e-05 ms.
That means it took 8.01214 times longer the first time."""
"""
Timed print with params ('nop+1=2',).
On average, it took 1.6445560455322266e-06 ms per call over 1000000 calls.
However, when run the first time, it took 1.0013580322265625e-05 ms.
That means it took 6.08893 times longer the first time."""