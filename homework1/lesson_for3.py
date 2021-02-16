score = [
    {'school_class': '4a', 'scores': [3, 3, 4, 5, 2, 4, 2, 5, 5, 4]}, #37
    {'school_class': '5b', 'scores': [3, 4, 5, 4, 3, 3, 3]}, #25
    {'school_class': '6c', 'scores': [2, 4, 4, 4, 2, 5, 3, 3, 3, 4]}
]

score_sum = 0
mid_score_school = 0
mid_score_class_1 = 0
mid_score_class_2 = 0
mid_score_class_3 = 0

for element in range(3):
    for elem in score[element]['scores']:
        score_sum += elem
    length = len(score[element]['scores']) 
    mid_score_school += length

for el in score[0]['scores']:
    mid_score_class_1 += el

for el in score[1]['scores']:
    mid_score_class_2 += el
    
for el in score[2]['scores']:
    mid_score_class_3 += el

length_2 = len(score[0]['scores']) 
length_3 = len(score[1]['scores'])
length_4 = len(score[2]['scores'])

print("Средняя оценка по школе:", score_sum/mid_score_school)
print("Средняя оценка класса -", score[0]['school_class'], ":", mid_score_class_1 / length_2)
print("Средняя оценка класса -", score[1]['school_class'], ":", mid_score_class_2 / length_3)
print("Средняя оценка класса -", score[2]['school_class'], ":", mid_score_class_3 / length_4)