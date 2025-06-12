# To Check if the Number is a Prime no or not


def is_prime(number):
    if number < 2:
        print("This number cannot be a Prime Number.")

    if number == 2:
        print("This is a Prime Number.")

    is_prime_flag = True

    for i in range(2, number):
        if number % i == 0:
            is_prime_flag = False
            break

    if is_prime_flag:
        print("This is a Prime Number. ")
    else:
        print("This is NOT a Prime Number.")


number_input = int(input("Enter the Number you need to check if it is a Prime Number: "))
is_prime(number_input)

"""
For input 25

Iteration	i	25 % i	Is it 0?	Action Taken
1	2	25 % 2 = 1	❌ No	Continue
2	3	25 % 3 = 1	❌ No	Continue
3	4	25 % 4 = 1	❌ No	Continue
4	5	25 % 5 = 0	✅ Yes	Set is_prime_flag = False
Break the loop
"""
