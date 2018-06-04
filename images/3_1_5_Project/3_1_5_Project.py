import matplotlib.pyplot as plt

countries = []
questions = []
subsets = []
answers = []
percentages = []
countries1 = []
percentages1 = []
countries2 = []
percentages2 = []
countries3 = []
percentages3 = []
countries4 = []
percentages4 = []

if len(percentages) == 0:
    datafile = open('feelsafefromcrimealoneatnight.csv', 'r')
    data = datafile.readlines()      
    for line in data[1:]:
        country, question, subset, answer, percentage = line.split(',')
        countries.append(country)
        questions.append(question)
        subsets.append(subset)
        answers.append(answer)
        percentages.append(float(percentage))

if len(percentages1) == 0:
    datafile1 = open('Howlikelyislosejob.csv', 'r')
    data1 = datafile1.readlines()
    for line in data1[1:]:
        country, question, subset, answer, percentage = line.split(',')
        countries1.append(country)
        questions.append(question)
        subsets.append(subset)
        answers.append(answer)
        percentages1.append(float(percentage))

if len(percentages2) == 0:
    datafile2 = open('findjobofsimilarsalary.csv', 'r')
    data2 = datafile2.readlines()    
    for line in data2[1:]:
        country2, question, subset, answer, percentage2 = line.split(',')
        countries2.append(country)
        questions.append(question)
        subsets.append(subset)
        answers.append(answer)
        percentages2.append(float(percentage2))

if len(percentages3) == 0:
    datafile3= open('worriedincomenotsufficient.csv', 'r')
    data3 = datafile3.readlines()
    for line in data3[1:]:
        country3, question, subset, answer, percentage3 = line.split(',')
        countries3.append(country)
        questions.append(question)
        subsets.append(subset)
        answers.append(answer)
        percentages3.append(float(percentage3))
        
if len(percentages4) == 0:
    datafile4 = open('alonedark.csv', 'r')
    data4 = datafile4.readlines()
    for line in data4[1:]:
        country4, question, subset, answer, percentage4 = line.split(',')
        countries4.append(country)
        questions.append(question)
        subsets.append(subset)
        answers.append(answer)
        percentages4.append(float(percentage4))
        
    
fig, ax = plt.subplots()
ax.set_facecolor('xkcd:green')
ax.set_facecolor((1.0, 0.47, 0.42))
ax.set_title('Job Security and Safety Correlation in Europe 2016')
ax.set_xlabel('Country (Using their country codes)')
ax.set_ylabel('Percentage of respondents answering "agree or strongly agree"')
plt.xticks(range(len(countries)), countries, size='small')
plt.setp(ax.get_xticklabels(), visible=True)

line, = ax.plot(percentages, label="I feel safe from crime alone at night?")
line1, = ax.plot(percentages1, label ="How likely is that you might lose your job?", color='red')
line2, = ax.plot(percentages2, label="I feel I can find a job of similar salary?", color='green')
line3, = ax.plot(percentages3, label="Worried about income in old age?", color='yellow')
line4, = ax.plot(percentages4, label="I feel safe when I walk alone after dark?", color='orange')



plt.legend(handles=[line,line1,line2, line3, line4])


fig.show()
print(countries, percentages2)

