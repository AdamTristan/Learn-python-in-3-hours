
secret_word = "giraffe"
guess = ""
n = 0

while guess != secret_word and n<=3:
    guess = input("enter guess: ")
    n = n + 1

if n < 4:
    print("u winnn!")
else:
    print("u LOST!!")


