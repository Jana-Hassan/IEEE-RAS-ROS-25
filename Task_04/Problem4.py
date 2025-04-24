if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    
    Scores = [[score, None] for score in arr]
    
    Scores.sort(reverse=True)
    
    max_score = Scores[0][0]
    
    score_list = [s for s in Scores if s[0] < max_score]
    
    if score_list:
        runnerUp_score = score_list[0][0]
        print(runnerUp_score)
   
