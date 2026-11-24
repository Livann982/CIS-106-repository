def find_high_low(names, scores):
    high_var = 0
    high_index = 0
    low_var = 999
    low_index = 0
    
    for i in range(len(scores)):
        if scores[i] > high_var:
            high_var = scores[i]
            high_index = i
            
        if scores[i] < low_var:
            low_var = scores[i]
            low_index = i
            
    print(f"Highest Score: {names[high_index]} with {high_var}")
    print(f"Lowest Score:  {names[low_index]} with {low_var}")

def main():
    last_names = []
    exam_scores = []
    
    with open("scores.txt", "r") as file:
        line = file.readline().strip()
        while line != "":
            last_names.append(line)
            score = int(file.readline().strip())
            exam_scores.append(score)
            line = file.readline().strip()
            
    find_high_low(last_names, exam_scores)

main()
