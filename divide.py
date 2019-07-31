def calculate_total_score(scores):
    total_score = 0
    for score in scores:
        total_score += score
    return total_score


scores = [1, 2, 3]


total_score = calculate_total_score(scores)


print(total_score)

