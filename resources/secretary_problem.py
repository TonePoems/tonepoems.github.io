import random
import matplotlib.pyplot as plt

MONTE_CARLO_REPS = 100

def find_best(num_interviews, total_candidates=100):
    candidates = list(range(total_candidates))
    random.shuffle(candidates)
    return max(candidates[:num_interviews])

list_interviews = list(range(1,101))
list_avg_best = []
list_ratio = []

for interview_count in list_interviews:
    total = 0
    for i in range(1000):
        total += find_best(interview_count)
    avg_best = total/MONTE_CARLO_REPS
    ratio = avg_best/interview_count
    #print(f'Interviews: {interview_count}\tavg best score: {avg_best}\tRatio: {ratio}')
    list_avg_best.append(avg_best)
    list_ratio.append(ratio)


plt.plot(list_interviews, list_avg_best)
plt.xlabel('# of interviews')
plt.ylabel('avg_best')
plt.title('Secretary Problem Scores')
plt.show()
