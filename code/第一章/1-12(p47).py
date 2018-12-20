def JudgeSubjects(mscore, escore, hscore):
	if mscore >= 75:
		if mscore >= 85:
            mlevel = 'Great'
        else:
            mlevel = 'Good'
    else:
        mlevel = 'Bad'
    if escore >= 80:
        if escore >= 90:
            elevel = 'Great'
        else:
            elevel = 'Good'
    else:
        elevel = 'Bad'

    if hscore >= 70:
        if hscore >= 78:
            hlevel = 'Great'
        else:
            hlevel = 'Good'
    else:
        hlevel = 'Bad'
    return {'Maths':mlevel,'English':elevel,'History':hlevel}

def JudgeTotal(total):
    if total >= 270:
        result = 'A+'
    elif total >= 240:
        result = 'A'
       elif total >= 210:
        result = 'B+'
    elif total >= 190:
       result = 'B'
    else:
        result = 'C'
    return result

def CalculateTotal(mscore,escore,hscore):
    return mscore*110/100 + escore*110/100 + hscore*80/100

def InputScore():
    math = int(input("Enter your Maths test score:"))
    while math < 0 or math > 100:
       print("The score is invalid.")
        math = int(input("Enter your Maths test score:"))

    english = int(input("Enter your English test score:"))
            while english < 0 or english > 100:
                print("The score is invalid.")
            english = int(input("Enter your English test score:"))

    history = int(input("Enter your History test score:"))
            while history < 0 or history > 100:
            print("The score is invalid.")
        history = int(input("Enter your History test score:"))
    return math,english,history

def OutputResult(total,TotalLevel,SL):
    print('Total Score:',total)
    print('Total Level:',TotalLevel)
    print('MathsLevel:',SL['Maths'],'EnglishLevel:',SL['English'],'HistoryLevel:',SL['History'])

if __name__ == "__main__":
    math,english,history = InputScore()
    SubjectLevel = JudgeSubjects(math,english,history)
    total = CalculateTotal(math,english,history)
    result = JudgeTotal(total)
    OutputResult(total,result,SubjectLevel)