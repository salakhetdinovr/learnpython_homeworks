score = [
    {'school_class': '4a', 'scores': [3, 3, 4, 5, 2, 4, 2, 5, 5, 4]}, 
    {'school_class': '5b', 'scores': [3, 4, 5, 4, 3, 3, 3]}, 
    {'school_class': '6c', 'scores': [2, 4, 4, 4, 2, 5, 3, 3, 3]}
]

score_sum = 0
mid_score_sum = 0
mid_score_school = 0

for element_score in range(len(score)):
    for element in score[element_score]['scores']:
        score_sum += element
        class_length =  score_sum / len(score[element_score]['scores'])
    print("Средняя оценка класса -", score[element_score]['school_class'], ":", class_length)
    mid_score_sum += score_sum
    score_sum = 0
    length = len(score[element_score]['scores'])
    mid_score_school += length

print("Средняя оценка по школе:", mid_score_sum / mid_score_school)


