# scores = [73, 45, 32]


# DYANMICALLY

scores = []
for i in range(3):
    score = int(input("Enter Score: "))
    scores.append(score)


average = sum(scores) / len(scores)

print(f"Average: {average}")
