human_years = int(input("Enter the dog;s age in human years: "))
dog_years = 0
for i in range(1,human_years + 1):
    if i <= 2:
        dog_years += 10.5
    else:
        dog_years += 4
print(f"the dog's age in dog's yeats is {round(dog_years)} years.")