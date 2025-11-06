"""
A generator function is a special kind of function in Python that produces values one at a time,
instead of returning them all at once.
"""


def generate_even_numbers(limit):
    n = 0
    while n <= limit:
        yield n
        n += 2


for num in generate_even_numbers(10):
    print(num)


"""
What is happening 

🧩 Step-by-step
Step 1:

The function generate_even_numbers(10) is called,
but it doesn’t run immediately — it returns a generator object.
At this point:
No numbers exist yet.
Nothing has been stored.
The function is just ready to start.

Step 2:

The for loop internally calls next() on that generator object.
This causes the function to start running until it reaches the first yield.
n = 0
yield n → gives 0 back to the loop
The function pauses right there.
So now, the for loop prints 0.

Step 3:

Then, the for loop automatically calls next() again.
The generator resumes exactly where it left off:
It continues from after the yield n line,
Executes n += 2, so n = 2,
Hits yield n again → returns 2, and pauses again.
So now the loop prints 2.

Step 4:

This keeps happening:
The generator runs only until the next yield.
Each time, it produces one value, not a full list.
Nothing is “stored” — the previous value is gone once yielded.

Step 5:

When n becomes 12 (bigger than limit),
the loop while n <= limit: stops → the generator ends → StopIteration is raised internally → for loop stops.
"""