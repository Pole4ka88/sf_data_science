
# Проект 4. Анализ резюме из HeadHunter (SQL).


## Оглавление  
[1. Описание проекта](.README.md#Описание-проекта)  
[2. Какой кейс решаем?](.README.md#Какой-кейс-решаем)  
[3. Краткая информация о данных](.README.md#Краткая-информация-о-данных)  
[4. Этапы работы над проектом](.README.md#Этапы-работы-над-проектом)  
[5. Результат](.README.md#Результат)    
[6. Выводы](.README.md#Выводы) 


### Описание проекта  

Дана база резюме Head Hunter. Необходимо:
- Познакомиться с данными
- Провести предварительный анализ данных
- Провести детальный анализ вакансий
- Провести анализ работодателей
- Провести предметный анализ
- Сделать выводы по каждому блоку и общий вывод на проект



### Какой кейс решаем?    

Представим, что это начало проекта по созданию модели машинного обучения, которая будет рекомендовать вакансии клиентам агентства, претендующим на позицию Data Scientist. В данной работе мне необходимо понять, что из себя представляют данные и насколько они соответствуют целям проекта.

**Метрика качества**     
Каждая часть будет состоять из блока практических заданий, которые необходимо выполнить в jupyter-ноутбуке, и контрольных вопросов на платформе. Задания выполняются последовательно.

Помимо проверки заданий на платформе, отправить свой код ментору для code-ревью. Оформить своё решение с помощь шаблона.


**Что практикуем**     
- Учимся писать хороший код на python / SQL
- Учимся анализировать данные
- Учимся делать выводы на основе анализа
- Учимся работать с GitHub


### Краткая информация о данных
  
База данных НН


### Этапы работы над проектом  
1) Загружаем базу данных HH
2) Создаем запросы для анализа данных, анализируем, делаем выводы
4) Загружаем файлы на github


### Результаты:  

 Data Understanding произведён, данные подходят для создания модели машинного обучения, которая будет рекомендовать вакансии клиентам агентства, претендующим на позицию Data Scientist

### Выводы:  

Мы имеем дело с базой данных, в которой 23501 работодатель разместил 49197 вакансий
Покрытие базы - 1362 города
Взято во внимание 294 сферы деятельности
Города, имеющие самое большое количество вакансий - Москва, Санкт-Петербург, Минск, Новосибирск, Алматы. 

У 24073 вакансий заполнено хотя бы одно из двух полей с зарплатой. Эти данные очень важны, тк кандидаты обращают большее внимание на вакансии с уровнем оплаты.
Cредние значения для нижней и верхней границы зарплатной вилки: 71065 и 110537 рублей соответственно.
Самое популярное сочетание: тип рабочего графика - полный день и занятость - полная занятость. На втором месте по популярности - удалённая работа и полная занятость.
Вполне ожидаемо, что работодатели более заинтересованы в постоянном полноценном сотрудничестве. А удалённая работа, это тип рабочего графика, набирающий сейчас особую популярность.
Реже всего работодатели запрашивают опыт более 6 лет, далее порядке возрастания запросов: Нет опыта, от 3 до 6 лет и от 1 года до 3 лет.
На мой взгляд, работодатели редко ищут кандидатов с опытом более 6 лет по многим причинам. Им необходимо более сильная материальная мотивация, бОльшую часть работы можно выполнять
сотрудниками с меньшим опытом. Чаще всего это высокие должности, либо узконаправленные специальности.
По количеству вакансий в пятёрку лидеров вошли работодатели: Яндекс, Ростелеком, Тинькофф, СБЕР и Газпром нефть. Это не удивительно.
Все перечисленные компании - крупнейшие в России, и , безусловно, им необходимо бОльшее число работников.
Регион, в котором наибольшее количество работодателей, но при этом нет вакансий - Россия. Думаю, что это связано с тем, что компании могут регистрировать
личный кабинет на сайте и при этом указывать регион своей компании - Россию, и это будет правильным. Особенно, если филиалы расположены в разных городах. 
Но когда работодатель размещает вакансию, необходимо указывать локацию для будущего сотрудника и в вакаснию вносят город.
Максимальное количество регионов, с опубликованными вакансиями 181 у компании Яндекс

8419 работодателей не указали свою сферу деятельности. Что, однозначно, уменьшает их шансы быть замеченными кандидатами.
На 3м месте в списке компаний, указавших 4 сферы деятельности - 2ГИС. С учётом сортировки по алфавиту.
У 3553 работодателей в качестве сферы деятельности указана «Разработка программного обеспечения».
Компания Яндекс разместила свои вакансии во всех 16 городах миллионниках. Всего это 485 вакансий
В нашем анализе к данным имеют отношение 1771 вакансия
Для начинающего дата-сайентиста найдена 51 вакансия
SQL или postgres в ключевых навыках указали работодатели в 201 вакансии
А Python, как ключевой навык хотели бы видеть в 351 вакансии
Более 6 ключевых навыков в среднем указывают в каждой вакансии DS
Для кандидатов без опыта вакансии предлагаются с зп 74643 руб в среднем, от 1 года жо 3х лет - 139675 руб, от 3х до 6 лет - 243115 руб.
Очевидно и очень показательно, что с увеличением опыта работы, работодатели готовы увеличивать и оплату труда. Задачи становятся труднее, но дороже.
То есть за 3 года ЗП специалиста может вырасти более, чем в 3 раза.
Но при этом, начинающему дата-сайентисту лучше не останавливаться на 1-2 навыках, необходимо расширять границы своего обучения, ведь работодатели хотят видеть специалистов широкого профиля.





Если информация по этому проекту покажется вам интересной или полезной, то я буду очень вам благодарен, если отметите репозиторий и профиль ⭐️⭐️⭐️-дами
>>>>>>> faa1284 (Initial commit)