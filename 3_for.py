"""

Домашнее задание №1

Цикл for: Оценки

* Создать список из словарей с оценками учеников разных классов 
  школы вида [{'school_class': '4a', 'scores': [3,4,4,5,2]}, ...]
* Посчитать и вывести средний балл по всей школе.
* Посчитать и вывести средний балл по каждому классу.
"""

def main():
    one_score, score_avg, score_avg_school, all_score_sum, count_all_score = 0, 0, 0, 0, 0
    all_classes = [{'school_class': '1a', 'score' : [3,4,2,4,3,5]},
                   {'school_class': '2a', 'score' : [2,5,3,2,4,4]},
                   {'school_class': '3a', 'score' : [4,3,5,1,1,2]},
                   {'school_class': '4a', 'score' : [1,2,4,5,5,1]},
                   {'school_class': '5a', 'score' : [1,2,5,3,2,4]}]

    for four_clases in range(len(all_classes)):
        all_score = all_classes[four_clases].get('score')
        count_all_score += len(all_score)
        print(count_all_score)
        score_sum = 0
        
        for one_score in all_score:
            score_sum += one_score
            
        all_score_sum += score_sum 
        score_avg = score_sum / len(all_score)

        print(f'Score avarage in classes "{four_clases + 1}a": {score_avg}')

    score_avg_school = all_score_sum / count_all_score
    print(f'Score avarage in school: {score_avg_school}')

            
    
if __name__ == "__main__":
    main()
