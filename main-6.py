import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


data = pd.read_excel('base.xlsx', engine='openpyxl')
print(data.keys())


fig, ax = plt.subplots(2, 2)
x = np.arange(1, 5)

# cреди опрошенных с женским гендером

grades = list(data[(data.Gender == "Female")]["Little_interest_or_pleasure_in_doing_things "])

y = np.array([grades.count(i) / len(grades) for i in range(1, 5)])


ax[0, 0].bar(x, y)
ax[0, 0].set_title("Распределение ответов на вопрос о чувстве\n подавленности, депрессии и усталости (у девушек)")
ax[0, 0].set_xlabel("Выбор ответа")

#график распределения учащихся по часам занятия учёбой
ax[0, 1].hist(data["How_many_hours_do_you_spend_studying_each_day"])
ax[0, 1].set_title("Распределение учащихся по часам\n занятия учёбой в день")
ax[0, 1].set_xlabel("Количество часов, которое занимает учёба")
ax[0, 1].set_ylabel("Количество учащихся")

studytime = [list(data[(data.How_many_hours_do_you_spend_on_social_media_per_day == i)]["Your_Last_Semester_GPA:"]) for i in ['1 - 2 Hours', '2 - 4 Hours', 'More than 4 Hours']]

ax[1, 0].boxplot(studytime, vert=0, labels=['1-2 часа', '2-4 часа', 'больше 4'])
ax[1, 0].set_title("Соотношение итоговой оценки к количеству времени,\n проведенном в социальных сетях")
ax[1, 0].set_xlabel("Итоговая оценка")
ax[1, 0].set_ylabel("Количество часов в соц. сетях")

#влияние количества гаджетов на успеваемость в зависимости от возраста

ax[1, 1].scatter(data[(data.How_many_of_the_electronic_gadgets_do_you_have == "1 - 3")]["Age"], data[(data.How_many_of_the_electronic_gadgets_do_you_have == "1 - 3")]["Your_Last_Semester_GPA:"], c=[[0, 0, 1, 0.3]])
ax[1, 1].scatter(data[(data.How_many_of_the_electronic_gadgets_do_you_have == "4 - 6")]["Age"], data[(data.How_many_of_the_electronic_gadgets_do_you_have == "4 - 6")]["Your_Last_Semester_GPA:"], c=[[0, 1, 0, 0.3]])
ax[1, 1].scatter(data[(data.How_many_of_the_electronic_gadgets_do_you_have == "More than 6")]["Age"], data[(data.How_many_of_the_electronic_gadgets_do_you_have == "More than 6")]["Your_Last_Semester_GPA:"], c=[[1, 0, 0, 0.3]])
ax[1, 1].set_title('Влияние количества гаджетов на успеваемость\n в зависимости от возраста\n(зеленый: 1-3, синий: 4-6, красный: больше 6)')
ax[1, 1].set_xlabel("Возраст учащихся")
ax[1, 1].set_ylabel("Итоговая оценка")

fig.set_figwidth(10)
fig.set_figheight(10)
fig.subplots_adjust(wspace=0.6, hspace=0.5)
plt.savefig('grafics.png')
plt.show()
input()
