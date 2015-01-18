import csv

def list_words(text):
"""
Returns a list of words of length>=3 (to avoid common words such as 'of','the' etc) present in a given subjec line.
input => An e-mail subject line.
output=>List of words present in subject line.
"""
    words = []
    words_tmp = text.lower().split()
    for p in words_tmp:
        if p not in words and len(p) > 2:
            words.append(p)

    return words

def training(texts):
"""
A function to extract features i.e. frequency of occurence of a word in a particular category of e-mail(spam/non spam).
Input=> A list of tuple pairs of format =>(subject,category).
Output=>Returns 1.c_words : A dict which gives frequency of a word in each category.
                2.c_categories :A dict giving count of subjects of each category.
                3.c_texts : Total number of subjects used for training.
                4.c_tot_words :Total number of unique words found in subjects of both categoryi.e. spam/non-spam.
"""
    c_words ={}
    c_categories ={}
    c_texts = 0
    c_tot_words =0
    

    for t in texts:
        c_texts = c_texts + 1
        if t[1] not in c_categories:
            c_categories[t[1]] = 1
        else:
            c_categories[t[1]]= c_categories[t[1]] + 1

    for t in texts:
        words = list_words(t[0])
        for p in words:
        if p not in c_words:
            c_tot_words = c_tot_words +1
            c_words[p] = {}
            for c in c_categories:
                c_words[p][c] = 0
        c_words[p][t[1]] = c_words[p][t[1]] + 1

    

    return (c_words, c_categories, c_texts, c_tot_words)


def classifier(subject_line, c_words, c_categories, c_texts, c_tot_words):
"""
Classifies the given subject line as spam/non spam using features passed from training().
Input=> 1.subject_line :subject to test for categorisarion.
        2.Rest are as defined in training().
Output=> Returns category of subject with probability.
"""
    category =""
    category_prob = 0

    for c in c_categories:
      
        prob_c = float(c_categories[c])/float(c_texts)
        words = list_words(subject_line)
        prob_total_c = prob_c
        for p in words:
          if p in c_words:
                prob_p= float(c_words[p][c])/float(c_tot_words)
                prob_cond = prob_p/prob_c
                prob =(prob_cond * prob_p)/ prob_c
                prob_total_c = prob_total_c * prob
          if category_prob < prob_total_c:
                category = c
                category_prob = prob_total_c
            
        
         
            

    return (category, category_prob)


if __name__ == "__main__":

    with open('training.csv') as f:
        subjects = dict(csv.reader(f, delimiter=','))
        p,c,t,tp = training(subjects.items())
    
	#First Test
        clase = classifier("Available on Term Life - Free",p,c,t,tp)
        print("Result: {0} ".format(clase))


    #Second Test
    with open("test.csv") as f:
        correct = 0
        tests = csv.reader(f)
        for subject in tests:
            clase = classifier(subject[0],p,c,t,tp)
            if clase[0] == subject[1]:
                correct += 1
        print("Efficiency {0} of 10".format(correct))
