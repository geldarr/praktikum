#!/usr/bin/env python
# coding: utf-8

# <img src=https://kto-ozvuchival.ru/wp-content/uploads/2017/12/kto-ozvuchivaet-toni-starka-na-russkom-800x500.jpg>
# <hr style="border: 10px solid green;" />
# 
# ## <span style="color:green">Финальный комментарий<span>
# Илья, спасибо за доработки🤝
# 
# Оставил доп комментарий по [тестированию модели](#21-bullet)
#     
# Поздравляю, проект принят👍

# <hr style="border: 2px solid green;" />
# 
# ## Комментарий ревьювера
# 
# Илья, привет! 
# 
# 🤚Меня зовут, Олег Юрьев, я буду проверять твой проект. Если не против, я буду обращаться к тебе на _ТЫ_ . Если это неприемлемо, обязательно напиши мне в комментариях - мы прейдем на _ВЫ_ .
# 
# 🤝Спасибо, что сдал проект вовремя. Тобой проделана большая работа, молодец! 
# 
# ✏️В этой тетрадке ты найдешь мои комментарии.
# 
# Комментарии будут выделены:
# 
# <div style="border:solid green 2px; padding: 20px"> <b>Отличная работа</b><br>
#     Безупречная работа</div>       
# <br>
# <div style="border:solid orange 2px; padding: 20px"> <b>Что можно улучшить</b><br>
#     Ничего дорабатывать не надо, данные пункты работают нормально, но есть способы улучшить. Несколько таких комментариев допустимы, но более - придется некоторые доработать. Большое кол-во мелких замечаний и помарок сказываются на общем впечатлении от работы.</div>   
# <br>
# <div style="border:solid red 2px; padding: 20px"> <b>Что необходимо доработать</b><br>
#     Такие пункты необходимо исправить в первую очередь, чтобы я смог принять проект.</div>
#  
# Не удаляй комментарии, так будем следить за динамикой 📈
#    
# Давай будем в диалоге - основные цели в диалоге:
# - обмен опытом (да я тоже учусь у студентов👨‍🎓)
# - выполнить проект еще лучше
# - помочь тебе стать аналитиком
# 
# Поэтому чтобы мне проще было проверять повторно, а тебе контролировать процесс ревью, оставляй свои комментарии и выделяй их. 
#     
# <div class="alert alert-info" style="border:solid blue 2px; padding: 20px"> <b>Комментарий студента:</b> Например, вот так.</div>
#    
# Поехали! :)
# 
# <hr style="border: 2px solid green;" />

# # Отток клиентов

# Из «Бета-Банка» стали уходить клиенты. Каждый месяц. Немного, но заметно. Банковские маркетологи посчитали: сохранять текущих клиентов дешевле, чем привлекать новых.
# 
# Нужно спрогнозировать, уйдёт клиент из банка в ближайшее время или нет. Вам предоставлены исторические данные о поведении клиентов и расторжении договоров с банком. 
# 
# Постройте модель с предельно большим значением *F1*-меры. Чтобы сдать проект успешно, нужно довести метрику до 0.59. Проверьте *F1*-меру на тестовой выборке самостоятельно.
# 
# Дополнительно измеряйте *AUC-ROC*, сравнивайте её значение с *F1*-мерой.
# 
# Источник данных: [https://www.kaggle.com/barelydedicated/bank-customer-churn-modeling](https://www.kaggle.com/barelydedicated/bank-customer-churn-modeling)
# 
# Признаки
# * RowNumber — индекс строки в данных
# * CustomerId — уникальный идентификатор клиента
# * Surname — фамилия
# * CreditScore — кредитный рейтинг
# * Geography — страна проживания
# * Gender — пол
# * Age — возраст
# * Tenure — количество недвижимости у клиента
# * Balance — баланс на счёте
# * NumOfProducts — количество продуктов банка, используемых клиентом
# * HasCrCard — наличие кредитной карты
# * IsActiveMember — активность клиента
# * EstimatedSalary — предполагаемая зарплата
# 
# Целевой признак
# * Exited — факт ухода клиента

# ### 1 [Подготовка данных](#Подготовка_данных)
# 
#    #### 1.1 [Импорт библиотек](#импорт_библиотек)
#    
#    #### 1.2 [Обработка данных](#обработка_данных)
#    
# ### 2 [Исследование задачи](#исследование_задачи)
#    
#    #### 2.1 [Постановка задачи](#постановка)
#    
#    #### 2.2 [Обработка признаков](#обработка)
#    
#    #### 2.3 [Формирование наборов](#формирование)
#    
#    #### 2.3 [Обучение линейной регрессии](#линейная)
#    
#    #### 2.3 [Случайный лес](#лес)
#    
#    #### 2.3 [Решающее дерево](#дерево)
#    
#    #### 2.3 [Итог](#Итог1)
# 
# ### 3 [Борьба с дисбалансом](#дисбаланс)
#    
#    #### 3.2 [Балансировка классов](#балансировка)
#    
#    #### 3.3 [Решающее дерево](#Дерево_баланс)
#    
#    #### 3.3 [Случайный лес](#Лес_баланс)
#    
#    #### 3.3 [Пороговые значения для случайного леса](#лес_баланс)
#    
#    #### 3.3 [Пороговые значения для дерева](#дерево_баланс)
# 
# ### 4 [Тестирование модели](#тест_модели)
# 

# <div style="border:solid green 2px; padding: 20px"> <b>Отличная работа</b><br>
# Спасибо за полное описание задачи, описание данных и интерактивное оглавление - всегда приятно сразу понимать о чем пойдет речь</div> 

# <a class="anchor" id="Подготовка_данных"></a>
# # 1. Подготовка данных

# Первичная подготовка данных
# Оценка обьема данных
# Оценка пропусков в данных

# <a id="импорт_библиотек"></a>
# ### 1.1 Импорт библиотек

# In[4]:


import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split 
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import f1_score
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import confusion_matrix
from sklearn.metrics import roc_curve
import matplotlib.pyplot as plt
from sklearn.preprocessing import StandardScaler
from tqdm import tqdm
from sklearn.metrics import roc_auc_score
from sklearn.metrics import recall_score
from sklearn.metrics import precision_score
from sklearn.tree import DecisionTreeClassifier
from sklearn.utils import shuffle
import warnings
warnings.filterwarnings(action='once')


# <a id="обработка_данных"></a>
# ### 1.2 Обработка данных

# In[5]:


#загрузим данные
data = pd.read_csv("/datasets/Churn.csv")


# In[6]:


#проверим на пустые значени и типыданных.
data.isna().mean()


# In[7]:


data.info()


# In[8]:


data.head(10)


# 
# Обработка:
# 
#   * Убрать заглавные символы в названиях признаков, удалить не нужные признаки. "Surname".
#    
#   * Тип данных признака Tenure заменить на int
#   
#   * На первом круге будем обучать модель на полных данных, поэтому сформируем датасет без пустых значений. Заполним пустые значения медианой.
#   
#   
#     
#     

# <div style="border:solid orange 2px; padding: 20px"> <b>Что можно улучшить</b><br>
# Затея с заполнение пропусков хорошая (как практика), но кажется, что около 1% не повлияют на результат, а добавление 10 бинарных признаков выглядит сомнительным решением ради увеличения на 1% данных.<br>
# Чем заполнять, можно решить исходя из модели, например, для деревьев и лесов можно заполнять несуществующими значениями, например, 9999.<br>
# При всей некритичности 1% можно заполнить и средним\медианой или средни\медианой по группе целевой</div>  

# <div class="alert alert-info" style="border:solid blue 2px; padding: 20px"> 
# Спасибо за совет, заполнил пустые значения медианой.
# </div>

# <div style="border:solid green 2px; padding: 20px"> <b>Отличная работа 2</b><br>👍</div> 

# In[9]:


# Приведем названия признаков к нижнему регистру
data.columns = data.columns.str.lower()


# In[10]:


data['tenure'].median()


# In[11]:


data['tenure'].mean()


# In[12]:


data['tenure'].fillna(data['tenure'].median(),inplace=True)


# In[13]:


data['exited'].mean()


# In[14]:


# заменим тип данных tenure на int 
data['tenure'] = data['tenure'].astype('int64',errors='ignore') 


# In[15]:


data.info()


# In[16]:


#data = data.fillna('unknown')


# In[ ]:





# In[17]:


data.info()


# Итог
# Проведена первичная обработка полученных данных. 

# <div style="border:solid orange 2px; padding: 20px"> <b>Что можно улучшить</b><br>
# Данные для решения поставленной задачи мы еще не видели, поэтому хорошей практикой будет исследовать их глубже. Построить распределения, посмотреть матрицу корреляций - может удасться выявить аномалии или коррелирующие признаки. Посмотреть графики в разрезах целевой.</div> 

# <div class="alert alert-info" style="border:solid blue 2px; padding: 20px"> Спасибо за подсказку, я учту это в будущем</div>

# <div style="border:solid green 2px; padding: 20px"> <b>Отличная работа 2</b><br>👍</div> 

# <a class="anchor" id="исследование_задачи"></a>
# # 2. Исследование задачи

# ### 2.1 Постановка задачи
# 

# Цель - прогнозирование, уйдёт клиент из банка в ближайшее время или нет. 
# 
# Задача является категориальной. Будем применять модели классификации, 1 - клиент уйдет 0 - клиента отсанется. 
# 
# Лучшим показателем работы модели будут положительные предсказания, так как нам в первую очередь интересны клиенты, которые могут покинуть нас в ближайшее время.
# 
# Основным критерием оценки работы модели будет F-Мера (F1-score), так же дополнительно для предтсавления о работе модели использовать метрики AUC-ROC для построения криво
# 
# Будем использовать 3 модели, линейную регрессию,решающее дерево и случайный лес.
# 

# ### План работ
# - [x] Проверить целевой признак на дисбаланс
# - [x] Отобрать признаки, проверить корреляцию признаков, преобразовать   
# - [x] Сформировать наборы данных тренировочный, валидационный и тестовый
# - [x] Провести преобразование категориальных признаков
# - [x] Выбрать подходящую модель для обучения
# - [x] Обучить модель подобрать гипер параметры проверить результат на валидационном наборе
# - [x] Оценить необходимость маштабирования признаков
# - [ ] Вывод 
# 
# 

# <a id="обработка"></a>
# ### 2.2 Обработка признаков

# In[18]:


#Посмотрим на целевоц признак
data['exited'].plot(kind='hist')


# In[19]:


data['exited'].mean()


# Доля положительных ответов в представленном дадтасете  составляет всего 20%, это может сказаться на результатах модели. Вероятнее всего модель будет реже относить данные к положительному классу.
# 

# <div style="border:solid green 2px; padding: 20px"> <b>Отличная работа</b><br>
# Да, это верное замечание. Думаю нам удасться с этим справиться</div>  

# In[20]:


#Удалим лишние призанки
data = data.drop(['rownumber','customerid','surname'],axis=1)


# In[21]:


#Для обоучения моделей проведем прямое кодирование категориальных признаков
data = pd.get_dummies(data, drop_first=True)


# In[22]:


data


# <a id="обработка"></a>
# ### 2.3 Формирование наборов данных 

# In[23]:


# Из полученного датасета сформируем три набора данных, тренировочный, валидационный и тестовый 70/15/15
#признаки
x = data.drop(['exited'],axis=1)
#целевой признак
y = data['exited']
x_train, x_remainder, y_train, y_remainder = train_test_split(x, y, test_size=0.4, random_state=12345)
#Разделим оставшиеся данные на валидационнцю и тестовую наборы
x_valid, x_test, y_valid, y_test = train_test_split(x_remainder, y_remainder, test_size=0.5, random_state=12345)

#Проверим разбивку
print('Общий размер датасета:',len(x))
print('Размер валидационного набора:',len(x_valid),len(y_valid))
print('Размер тестового набора',len(x_test),len(y_test))
print("Размер тренировочного  набора:",len(x_train),len(y_train))
print("Сумма всех нразбивок:",len(x_valid)+len(x_test)+len(x_train))


# In[26]:


y_test


# <div style="border:solid green 2px; padding: 20px"> <b>Отличная работа</b><br>
# Молодец, что проверяешь себя👌</div>  

# In[1]:


# Для модели линейная регрессия сделаем дополнительный датасет, 
# и сделаем масшабирование признаков creditscore,age,balance,estimatedsalary
numeric = ['creditscore','age','balance','estimatedsalary']
scaler = StandardScaler()

scaler.fit(x_train[numeric])
x_train_scale = x_train.copy()
x_valid_scale = x_valid.copy()       

x_train_scale[numeric] = scaler.transform(x_train_scale[numeric])
x_valid_scale[numeric] = scaler.transform(x_valid_scale[numeric])


# In[ ]:


x_train_scale


# In[ ]:


x_valid_scale


# In[ ]:


x_train


# In[ ]:


x_valid


# In[ ]:


# Создадим дадасет в который будем записывать все показатели моделей.
columns=['model_name','roc_auc_scores','recall_scores','precision_scores','f1_scores','tn','fp','fn','tp']
result_metric = pd.DataFrame(columns=columns)


# In[ ]:


result_metric


# In[ ]:


#перед обучением сделаем функцию сбора метрик 
def metrics_model(model_name,y_valids,predictions,probabilites_one):
    global result_metric
    #roc_auc_scores =0
    roc_auc_scores = roc_auc_score(y_valids, probabilites_one)
    
    #recall_scores=0
    recall_scores = recall_score(y_valids, predictions)
    
    #precision_scores=0
    precision_scores = precision_score(y_valids, predictions)
    
    #f1_scores=0
    f1_scores = f1_score(y_valids, predictions)
    
    tn, fp, fn, tp = confusion_matrix(y_valids, predictions).ravel()

    #result_metric = result_metric.append({'model_name':model_name,'roc_auc_scores':roc_auc_scores,
                       #  'recall_scores':recall_scores,'precision_scores':precision_scores,'f1_scores':f1_scores,
                        #  'tn':tn,'fp':fp,'fn':fn,'tp':tp},ignore_index=True)
    
    #result_metric.drop_duplicates(inplace=True)
    
    result = ({'model_name':model_name,'roc_auc_scores':roc_auc_scores,
                         'recall_scores':recall_scores,'precision_scores':precision_scores,'f1_scores':f1_scores,
                          'tn':tn,'fp':fp,'fn':fn,'tp':tp})
    return result


# <div style="border:solid green 2px; padding: 20px"> <b>Отличная работа</b><br>
# Отличная идея собрать результаты экспериментов в одну таблицу✅</div>       
# <br>
# <div style="border:solid orange 2px; padding: 20px"> <b>Что можно улучшить</b><br>
# На будущее, не советую создавать фукнцию, которая изменяет внешние переменные. <br>
# Корректнее чтобы функция возвращала строку, которую необходимо добавить к таблице.</div>  

# <div class="alert alert-info" style="border:solid blue 2px; padding: 20px"> Намек понят, спасибо.Поправил.

# In[ ]:


def figure():
    f, ax = plt.subplots(figsize=(6,6))
    
    #plt.axhspan(0,1,0,1,color='#d62728')
    ax.plot([0, 1], [0, 1], ls="--",color='#d62728')
    return ax


# In[ ]:


#Функция отрисовки
def roc (y_valid,probabilites_one,name,axis):
   
    fpr, tpr, thresholds = roc_curve(y_valid, probabilites_one)
    roc_auc = pd.DataFrame({'fpr':fpr,'tpr':tpr,'thresholds':thresholds})
    roc_auc['fpr_i'] = roc_auc['fpr']
    
    fig = plt.figure()
    
    #ax = axis
    #fig.add_subplot(title='ROC_AUC'+ name)

    roc_auc.plot(x='fpr',y='tpr',ax=axis,label=name,grid=True)


# Данны подготовлены, сформированны все необходимые наборы. 

# <a id="линейная"></a>
# ### 2.4 Обучение логистической регрессии

# In[29]:


#обучим и проверим логичтическую регрессию на простом датасете
lr = LogisticRegression(solver='liblinear',random_state=12345)
lr.fit(x_train,y_train)


# In[30]:


#обучим и проверим логичтическую регрессию на  датасете с маштабированием
lr_scale = LogisticRegression(solver='liblinear',random_state=12345)
lr_scale.fit(x_train_scale,y_train)


# In[ ]:


#Проверим модель на валидационном наборе  и на наборе с маштабирование
predicted_lr_valid = lr.predict(x_valid)


# In[ ]:


predicted_lr_scale_valid = lr_scale.predict(x_valid_scale)


# In[ ]:


probabilites_lr_one = lr.predict_proba(x_valid)[:,1]


# In[ ]:


probabilites_lr_one_scale = lr_scale.predict_proba(x_valid_scale)[:,1]


# In[ ]:


result_metric=result_metric.append(metrics_model('lr',
              y_valid,predicted_lr_valid,
              probabilites_lr_one),ignore_index=True)


# In[ ]:


result_metric=result_metric.append(metrics_model('lr_scale',
                                   y_valid,predicted_lr_scale_valid,
                                   probabilites_lr_one_scale),ignore_index=True)


# In[ ]:


ax = figure()
roc(y_valid,probabilites_lr_one,' lr',ax)
roc(y_valid,probabilites_lr_one_scale," lr_scale",ax)


# <div style="border:solid orange 2px; padding: 20px"> <b>Что можно улучшить</b><br>
# Сравнение получилось бы нагляднее, будь графики на одной фигуре. Кстати это можно сделть, если из функции возвращать объект <b>ax</b>. Можно дополнительно добавить на график линию под случайной модели (под 45 градусов), чтобы визуально сравнивать насколько мы выше</div>  

# <div class="alert alert-info" style="border:solid blue 2px; padding: 20px"> Совет хороший, спасибо.Улучшил.</div>

# <div style="border:solid green 2px; padding: 20px"> <b>Отличная работа 2</b><br>👍Для большей убедительности графика можно добавить заполнение разницы между кривыми - <a href="https://matplotlib.org/3.1.1/api/_as_gen/matplotlib.pyplot.fill_between.html">fill_between</a></div> 

# #### Промежуточный итог для линейной регрессии:
# 
# Линейная регрессия:
# 
# Полученные результаты ,после обучение и проверки данной модели на двух датасетах с мастабированием и без, оказались недостаточными для решения поставленной задачи. 
# 
# Матрица ошибок показала, что модель слабо распознает положительные ответ из-за этого recall очень мал.
# 
# Показатель ROC AUC всго 0,75 до идеального слишком далеко, врятли получится сильно увеличить его. Целевой показатель тоже очень мал.
# 
# Данную модель для решения задачи далее рассматривать не будем
# 

# <a id="лес"></a>
# ### 2. 5 Модель "Случайный лес"

# Модель случайный лес будем обучать на обчном датасете, без масштабирования.
# 
# 

# In[28]:


warnings.filterwarnings('ignore')
# подберем оптимальные гиперпараметры для модели
best_score = 0
max_est = 0
max_depth = 0
for est in range(1,30,1):
    for depth in range(1,40,1):
        
        clf = RandomForestClassifier(n_estimators=est, max_depth=depth,random_state=12345)
        clf.fit(x_train,y_train)
        predicted = clf.predict(x_valid)
        res_score = f1_score(y_valid,predicted)
    
        if best_score < res_score:
            best_score = res_score
            max_est = est
            max_depth = depth
   
print('гиперпараметры')   
print("n_estimators:",max_est,'max_depth', max_depth, 'f1',best_score) 


# <div style="border:solid orange 2px; padding: 20px"> <b>Что можно улучшить</b><br>
# Данное предупреждение говорит, что в предсказанных значениях есть не все метки классов по отношению к y_true, поэтому f1_score устанавливается в 0. Чтобы не получать предупреждение каждый раз, можно воспользоваться библиотекой <code>warnings</code> - и выводить только однократно - <code>warnings.filterwarnings('once')</code><br><br>
# Ты в цикле прибавляешь по одному дереву, разница между 10 и 11 деревьями очень незначительная, лучше, перебирать деревья через 5\10 и начинать не с 1, а,например, с 10. В помощь отличная статья <a href="https://dyakonov.org/tag/random-forest/">Про параметры RandomForest</a></div>  

# <div class="alert alert-info" style="border:solid blue 2px; padding: 20px"> Спасибо.Поправил.</div>

# In[ ]:





# In[27]:


#Проверим модель
clf = RandomForestClassifier(n_estimators=max_est, max_depth=max_depth,random_state=12345)


# In[ ]:


clf.fit(x_train, y_train)


# In[ ]:


#Полчим прогноз модели 
predicted_clf_valid = clf.predict(x_valid)


# In[ ]:


#Вероятность 
probabilites_clf_one = clf.predict_proba(x_valid)[:,1]


# In[ ]:


result_metric=result_metric.append(metrics_model('clf',y_valid, predicted_clf_valid,
                          probabilites_clf_one),ignore_index=True)


# In[ ]:


ax = figure()
roc(y_valid,probabilites_clf_one,"clf",ax)


# In[ ]:


result_metric


# #### Промежуточный итог для модели Случайный лес
# Модель "решающее дерево"  работает хорошо. результы данной модели на валидационной выборке соответсвуют минимальным требованиям.
# 
# 
# Показатель roc_auc_score говорит что модель существенно чем простой рандом.
# 
# У модели решающего дерева  хорошая точностью, но полноту необходимо увеличить.
# 
# Модель хорошо определяет тех клиентов кто останется. Но еще плохо распознает  тех кто уйдет, вероятно потому как  мало событий положительного класса. 
# С текущим показателей данную модель можно донастроить на сбалансированном датасете.
# 
# 

# <div style="border:solid green 2px; padding: 20px"> <b>Отличная работа</b><br>
# Верные комментарии. Хотя roc_auc у всех моделей выше чем рандом =)</div>      

# <a id="дерево"></a>
# ### 2.5 Решающее дерево

# In[ ]:


warnings.filterwarnings('ignore')
best_score = 0
max_depth = 0
for depht in range(1,60,1):
    tree = DecisionTreeClassifier(max_depth=depht,random_state=12345)
    tree.fit(x_train,y_train)
    predicted_tree = tree.predict(x_valid)
    
    res_score = f1_score(y_valid,predicted_tree)
    
    if best_score < res_score:
        best_score = res_score
        max_depth = depht
       
print('гиперпараметры')            
print("max_depth:",max_depth, 'f1-score',best_score)


# In[ ]:


tree = DecisionTreeClassifier(max_depth=max_depth,random_state=12345)


# In[ ]:


tree.fit(x_train,y_train)


# In[ ]:


predicted_tree_valid = tree.predict(x_valid)


# In[ ]:


probabilites_tree_one = tree.predict_proba(x_valid)[:,1]


# In[ ]:


result_metric=result_metric.append(metrics_model('tree', 
              y_valid, predicted_tree_valid,
              probabilites_tree_one),ignore_index=True)


# In[ ]:


ax = figure()
roc(y_valid,probabilites_tree_one,'tree',ax)


# In[ ]:


result_metric


# <a id="Итог1"></a>
# ## 2. 7 Итог
# 
# Проведено обучение трех моделей на разных датасетах, с маштабированием признаков и без. Выделим  топ модели по целевому для нашей задачи показателю в порядке убывания 
# 
# 1. "Решающее дерево" - модель обучена на датасете без масштабирования 
#     
#   **F1-Мера = 0,59**
# 
# 
# 2. "Случайный лес" - модель обученная на датасете без масштабирования.
# 
#   **F1-Мера = 0,56**
#  
# 
# Все обученные модели дают много ложноотрицательных ответов. Для решения данной проблемы попробуем изменить баланс классов вручную. После оценки при необходимости переобучим модели с параметром **class_weight**.
# 
# 
# 
# 

# # 3. Борьба с дисбалансом

# <a id="балансировка"></a>
# ### 3.1 Подготовка нового набора 
# 

# In[ ]:


y_valid.plot(kind='hist')


# In[ ]:


def upsample(x, y, repeat):
    x_zeros = x[y == 0]
    x_ones = x[y == 1]
    y_zeros = y[y == 0]
    y_ones = y[y == 1]

    x_upsampled = pd.concat([x_zeros] + [x_ones] * repeat)
    y_upsampled = pd.concat([y_zeros] + [y_ones] * repeat)
    
    x_upsampled, y_upsampled = shuffle(
        x_upsampled, y_upsampled, random_state=12345)
    
    return x_upsampled, y_upsampled


# In[ ]:


x_upsampled, y_upsampled = upsample(x_train, y_train, 2)


# In[ ]:


y_upsampled.mean()


# In[ ]:


y_upsampled.plot(kind='hist')


# <a id="Дерево_баланс"></a>
# ###  3.3 "Решающее дерево"

# In[ ]:


#Перед тем как обучить модель, вернемя и подберем новые параметры для обучения


# In[ ]:


warnings.filterwarnings('ignore')
#Подберем новые параметры для модели на новом датасете
best_score = 0
max_depth = 0
for depht in range(1,60,1):
    tree = DecisionTreeClassifier(max_depth=depht,random_state=12345)
    tree.fit(x_upsampled,y_upsampled)
    predicted = tree.predict(x_valid)
    res_score = f1_score(y_valid,predicted)
    if best_score < res_score:
        best_score = res_score
        max_depth = depht
            
print("Глубина дерева:",max_depth, 'F1-мера',best_score)   


# In[ ]:


tree = DecisionTreeClassifier(max_depth=max_depth,random_state=12345)
tree.fit(x_upsampled,y_upsampled)


# In[ ]:


predicted_tree_valid = tree.predict(x_valid)


# In[ ]:


probabilites_tree_one = tree.predict_proba(x_valid)[:,1]


# In[ ]:


result_metric=result_metric.append(metrics_model('tree_balanced',
                                   y_valid, 
                                   predicted_tree_valid, 
                                   probabilites_tree_one),ignore_index=True)


# In[ ]:


result_metric


# <a id="Лес_баланс"></a>
# ###  3.3 "Случайный лес" 

# In[ ]:


warnings.filterwarnings('ignore')
# Теперь подберем кол-во деревьев
best_score = 0
max_est = 0
max_depth = 0
for est in range(1,40,1):
    for depth in range(1,30,1):
        
        clf = RandomForestClassifier(n_estimators=est, max_depth=depth,random_state=12345)
        clf.fit(x_upsampled,y_upsampled)
        predicted = clf.predict(x_valid)
        res_score = f1_score(y_valid,predicted)
    
        if best_score < res_score:
            best_score = res_score
            max_est = est
            max_depth = depth
print('гиперпараметры')   
print("n_estimators:",max_est,'max_depth', max_depth, 'f1',best_score) 


# In[ ]:


clf = RandomForestClassifier(n_estimators=max_est, max_depth=max_depth,random_state=12345)
clf.fit(x_upsampled,y_upsampled)


# In[ ]:


predicted_clf_valid = clf.predict(x_valid)


# In[ ]:


probabilites_clf_one = clf.predict_proba(x_valid)[:,1]


# In[ ]:


result_metric=result_metric.append(metrics_model('clf_balanced',
                                                 y_valid, predicted_clf_valid,
                                                 probabilites_clf_one),ignore_index=True)


# In[ ]:


result_metric


# Модель "Случайны лес" показала очень хорошие результаты, на текущем уровне модель отвечает качеству по нашему целевому признаку
# Для модели "решающее дерево" после балансировки классов тоже удалось увеличить показатели.
# Попробуем еще один способ обучим модель на тренеровочной выборке, но  с параметром class_weight='balanced' и проверим результат.

# In[ ]:


#Перед тем как обучить модель, подберем новые параметры для обучения
#с учетом параметра class_weight


# In[ ]:


best_score = 0
max_depth = 0
for depht in range(1,60,1):
    tree = DecisionTreeClassifier(max_depth=depht,random_state=12345,class_weight='balanced')
    tree.fit(x_train,y_train)
    predicted = tree.predict(x_valid)
    res_score = f1_score(y_valid,predicted)
    if best_score < res_score:
        best_score = res_score
        max_depth = depht
            
print("Глубина дерева:",max_depth, 'Accuracy',best_score) 


# In[ ]:





# In[ ]:


tree = tree = DecisionTreeClassifier(max_depth=max_depth,
                                    random_state=12345,class_weight='balanced')


# In[ ]:


tree.fit(x_train,y_train)


# In[ ]:


predicted_tree_valid = tree.predict(x_valid)


# In[ ]:


probabilites_tree_one = tree.predict_proba(x_valid)[:,1]


# In[ ]:


result_metric=result_metric.append(metrics_model('tree_class_weight', 
                                                 y_valid, 
                                                 predicted_tree_valid, 
                                                 probabilites_tree_one),ignore_index=True)


# In[ ]:


result_metric


# ### Итог
# 
# После ручной и автоматической балансировки классов, f1-мера повысилась. Нам удалось повысить показатель полноты для обеих моделй, но и доля ложноположительных ответов увеличилась. 
# 
# Попробуем изменить пороговые значения и посмотрим на показатели полноты и точности моделей.
# 
# 
# Лучший результат  у модели "Случайный лес".
# 
# Для модели "решающее дерево", будем использовать параметры полученные при обучении на сбалансированном вручную датасете 

# <div style="border:solid green 2px; padding: 20px"> <b>Отличная работа</b><br>
# В шаге все верно. Только кажется, что ты выбрал недостаточный коэффициент для upsample, дисбаласн все еще значительный.</div>      

# <div style="border:solid orange 2px; padding: 20px"> <b>Что можно улучшить</b><br>
# Не увидел тестирования случайного леса с параметром <code>class_weight</code></div>   
# 

# <div class="alert alert-info" style="border:solid blue 2px; padding: 20px">Да я не стал тестировать случайный лес, так как его показатели уже удовлетворительны. Коофицент upsample я подбирал ориентируясь на показатели целевой метрики. Именно на таком балансе у меня получилось добиться нужного результата. </div>

# <div style="border:solid green 2px; padding: 20px"> <b>Отличная работа 2</b><br>👍Ок, такие комментарии важны, их следует добавлять</div> 

# <a id="порог_лес"></a>
# ### Порог для случайного леса

# In[ ]:


probabilites_clf_one


# In[ ]:


f1_best = 0
thresh = 0
prec = 0
rec = 0
for threshold in np.arange(0.3, 0.8, 0.02):
    predictions = (probabilites_clf_one>threshold)*1
    #recall_scores=0
    recall = recall_score(y_valid, predictions)
    f1 = f1_score(y_valid,predictions)
    #precision_scores=0
    precision = precision_score(y_valid, predictions)
    
    if f1 > f1_best:
        f1_best = f1
        thresh = threshold
        prec = precision
        rec = recall
            
print("Порог = {:.2f} | Точность = {:.3f}, Полнота = {:.3f}, f1-мера = {:.3f}".format(
                                                thresh, prec, rec ,f1_best))


# In[ ]:


clf


# In[ ]:


probabilites_clf = clf.predict_proba(x_valid)


# In[ ]:


predicted_clf_valid = (probabilites_clf[:,1] > 0.46)*1


# In[ ]:


f1_score(y_valid,predicted_clf_valid)


# In[ ]:


result_metric=result_metric.append(metrics_model('clf_final',
                                                 y_valid, 
                                                 predicted_clf_valid,
                                                 probabilites_clf[:,1]),ignore_index=True)


# In[ ]:


result_metric


# <a id="порог_дерево"></a>
# ### Порог для решающего дерева

# In[ ]:


tree = DecisionTreeClassifier(max_depth=6,random_state=12345)
tree.fit(x_upsampled,y_upsampled)


# In[ ]:


probabilites_tree_one = tree.predict_proba(x_valid)[:,1]


# In[ ]:


probabilites_tree_one


# In[ ]:


f1_best = 0
thresh = 0
prec = 0
rec = 0
for threshold in np.arange(0.3, 0.8, 0.02):
    predictions = (probabilites_tree_one>threshold)*1
    #recall_scores=0
    recall = recall_score(y_valid, predictions)
    f1 = f1_score(y_valid,predictions)
    #precision_scores=0
    precision = precision_score(y_valid, predictions)
    
    if f1 > f1_best:
        f1_best = f1
        thresh = threshold
        prec = precision
        rec = recall
            
print("Порог = {:.2f} | Точность = {:.3f}, Полнота = {:.3f}, f1-мера = {:.3f}".format(
                                                thresh, prec, rec ,f1_best))


# In[ ]:


tree


# In[ ]:


probabilites_tree = tree.predict_proba(x_valid)


# In[ ]:


predict_tree_valid = (probabilites_tree[:,1] > thresh)*1


# In[ ]:


f1_score(y_valid,predict_tree_valid)


# In[ ]:


result_metric=result_metric.append(metrics_model('tree_final',
                                                 y_valid, predict_tree_valid,
                                                 probabilites_tree[:,1]),ignore_index=True)


# In[ ]:


result_metric


# In[ ]:


ax = figure()
roc(y_valid,probabilites_clf[:,1],'clf_final',ax)
roc(y_valid,probabilites_tree[:,1],'tree_final',ax)


# Изменив порог для двух моделей, мы еще немного смогли поднять целевой показатель. Таким образром после проверки на валидационной выборке, обе модели отвечают целевым показателям и можно оценить их работу на тестовой выборке.
# 
# 

# # 4. Тестирование модели

# In[ ]:


# Обьеденим валидационну выборку и тестову для обучения модели перед тестированием
x_final_train = pd.concat([x_upsampled] + [x_valid])
                        


# In[ ]:


y_final_train = pd.concat([y_upsampled] + [y_valid])


# In[ ]:


x_final_train, y_final_train = shuffle(
        x_final_train, y_final_train, random_state=12345)


# In[ ]:


len(x_final_train)


# In[ ]:


len(y_final_train)


# ### Случайный лес

# In[ ]:


clf = RandomForestClassifier(n_estimators=24, max_depth=10,random_state=12345)
clf.fit(x_final_train,y_final_train)


# In[ ]:


probabilites_clf = clf.predict_proba(x_test)


# In[ ]:


predicted_clf_test = (probabilites_clf[:,1] > 0.46)*1


# In[ ]:


f1_score(y_test,predicted_clf_test)


# In[ ]:


result_metric=result_metric.append(metrics_model('clf_test',
                                                 y_test, 
                                                 predicted_clf_test,
                                                 probabilites_clf[:,1]),ignore_index=True)


# ### Решающее дерево

# In[ ]:


tree = DecisionTreeClassifier(max_depth=6,random_state=12345)
tree.fit(x_final_train,y_final_train)


# In[ ]:


probabilites_tree = tree.predict_proba(x_test)


# In[ ]:


predict_tree_test = (probabilites_tree[:,1] > 0.44)*1


# In[ ]:


f1_score(y_test,predict_tree_test)


# <div style="border:solid orange 2px; padding: 20px"> <b>Что можно улучшить</b><br>
# В строке выше опечатка, смотреть метрику надо на тестовых данных</div>   

# <div class="alert alert-info" style="border:solid blue 2px; padding: 20px"> Спасбо что указал на ошибку, исправил </div>

# <div style="border:solid green 2px; padding: 20px"> <b>Отличная работа 2</b><br>👍</div> 

# In[ ]:


result_metric=result_metric.append(metrics_model('tree_test',
                                                 y_test, predict_tree_test,
                                                 probabilites_tree[:,1]),ignore_index=True)


# In[ ]:


result_metric


# <div style="border:solid red 2px; padding: 20px"> <b>Что необходимо доработать</b><br>
# Тестирование модели выполнено верно, только модель перед тестированием необходимо обучить на объединенной выборке = <code>train + valid</code></div>

# <div class="alert alert-info" style="border:solid blue 2px; padding: 20px"> Ок, поправил. Можешь пояснить зачем такой трюк делается ? И нужно ли подбирать заново гиперпараметры если мы меняем обучающую выборку ? </div>

# <a class="anchor" id="21-bullet">

# <div style="border:solid green 2px; padding: 20px"> <b>Отличная работа 2</b><br>👍 Нет, гиперпараметры подбирать не надо, их уже подобрал. Необходимо это для независимости тестирования качества модели. Об этом лучше посмотреть видео ниже</div> 

# In[ ]:


url = "http://storage.yandexcloud.net/public-bucket-6/split_data.mp4"


# In[ ]:


from IPython.display import Video
Video(url)


# #### Итог 
# Мы получили нужный целевой показатель метрики на моделях  "случаный лес"и "решающее дерево"
# 
# Целевой метрики на тестовой выборке удалось достич применяя следующие методы и практики.
# 
# * Прямое кодирование признаков
# * Балансировка классов, путем анализа результатов можели положительный класс в обучающей выборку был увеличен вдвое.
# * Обучение модели с параметром class, для модели решающее дерево, балансировка классов недала улучшений, пожтому был применен параметр class
# * Анализ и изменение порога. Для обоих моделей был изменен стандартный порог, что позволило увеличить целевую метрику.
# 

# In[ ]:





# <hr style="border: 2px solid green;" />
# 
# ## Общий комментарий
# Спасибо за проделанную работу🤝
# 
# Работа выполнена хорошо. Ты корректно подготовил данные для обучения\тестирования моделей, верно применил методы кодирования признаков\масштабирования, использовал различные техники устранения дисбаланса классов.
# 
# Есть ряд спорных моментов:
# - заполнение пропусков в признаке `tenure` строковым значением с последующим преобразованием в бинарные признаки
# - было бы здорово, проверить не только upsampling но и downsampling
# 
# **Доработать**
# - для тестирования объединить выборки train\valid, обучить модель и проверить её на test
# 
# Исправляй и отправляй на проверку🛠

# <div class="alert alert-info" style="border:solid blue 2px; padding: 20px">  Привет Олег, спасибо за быстры отклик по моей работе. Учел твои замечния. Поправил проект. С балансом я еще поиграюсь.</div>

# # Чек-лист готовности проекта

# Поставьте 'x' в выполненных пунктах. Далее нажмите Shift+Enter.

# - [x]  Jupyter Notebook открыт
# - [x]  Весь код выполняется без ошибок
# - [x]  Ячейки с кодом расположены в порядке исполнения
# - [x]  Выполнен шаг 1: данные подготовлены
# - [x]  Выполнен шаг 2: задача исследована
#     - [x]  Исследован баланс классов
#     - [x]  Изучены модели без учёта дисбаланса
#     - [x]  Написаны выводы по результатам исследования
# - [x]  Выполнен шаг 3: учтён дисбаланс
#     - [x]  Применено несколько способов борьбы с дисбалансом
#     - [x]  Написаны выводы по результатам исследования
# - [x]  Выполнен шаг 4: проведено тестирование
# - [x]  Удалось достичь *F1*-меры не менее 0.59
# - [x]  Исследована метрика *AUC-ROC*

# In[ ]:




