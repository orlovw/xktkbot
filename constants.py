facts = ['Этот доклад был написан за день!\n(бот за 4 часа)',
         'Интересно а можно было б написать телеграмм бота не имея телеграмма?\nМой телеграмм - @orlow\nЕсли все же захотите написать - могу помочь',
         'Опыт создания ботов - 6 месяцев, в особо везучие моменты мне даже за это платили деньги)',
         '(из словаря)\nбот - Небольшое парусное, гребное или моторное судно.',
         'Этот бот хостится на Heroku\nhttps://dashboard.heroku.com',
         'Существуют конструкторы для ботов, которые умеют работать с 1С!!!\nКак по мне "ЦЕ ПЕРЕМОГА!',
         'Хотя есть много конструкторов ботов, которые предлагают написать своего бота "не написав ни одной строчки кода"\n'
         'Чаще всего они очень ограничены, я уже не говорю о привязке к базе данных',
         'На OpenWeather с бесплатной подпиской можно отправлять только 10 запросов в минуту.\n'
         'Так что сейчас погода константная, да 🤔\n'
         '(но в исходниках есть закомментированый работающий код запросов к OpenWeather, все норм!)',
         'Комментарии отправляются докладчику в лс, он обязательно потом все прочтет!',
         'Вот бы написать бота, который пишет ботов. который пишет ботов, который пишет ботов',
         'В докладе и боте(33) слово бот(34) повторяется 34 раза',
         'Надеюсь вы заходили на гитхаб, но все же скажу что написано все на Python(3)']

slides = {
1:"""Если говорить в двух словах то бот это просто программа с удобным для человека интерфейсом. Вот к примеру удобный интерфейс Windows 10, нажимаешь кнопку и бум – что-то произошло!
Забегая вперед скажу что почти все действия в ботах ведутся в виде некого диалога. А если эта программа направлена на широкий круг пользователей, то интерфейс вообще стараются делать в виде общения с настоящим человеком.""",
2:""" А теперь на счет мессенджеров, в них они прижились потому что в большинстве месседжеров в самой программной части есть только чаты (нет групп, сообществ и т.д. , к чему пользователи привыкли в социальных сетях)
Cовместив удобный интерфейс программы  с интерфейсом чата мы получаем нашего бота.
На слайде видно клавиатуру, которая предоставляет имитированный GUI, ну и в принципе все понятно. И что самое главное пользователю не надо писать команды, как это было раньше, что зачастую отпугивало очень много потенциальных клиентов.""",
3:"""Такие боты были и раньше (ICQ, старый Вконтакте) , но с течением времени и ненадобности они просто вымерли, а сейчас заново начинают возрождаться из-за упомянутых выше причин,  в этом суть моего доклада так-то, дать побольше информации разработчикам о новом старом тренде. Многие компании сейчас начинают писать своих ботов привязывать к сайту и т.д. 
В Приват-боте например можно даже расплатиться или переслать деньги!""",
4:"""А теперь отвечу на главный «А как это работает?». Есть запрос от пользователя,  который попадает на сервера там пересылается нам, мы (наш сервер) составляем ответ и отправляем его на сервер мессенджера, откуда уже обработанный ответ идет пользователю.
Также следует сказать про получение обновлений – обычно это делается с помощью вебхуков (полноценного сервера), который принимает сообщения, но можно использовать и лонг поллинг (ежесекундный запрос нескольких последних сообщений.)""",
5:"""Запрос от телеграмм-сервера или чтобы было понятнее, обновление. Это json-объект, с информацией об действии пользователя (к примеру он отправил нашему боту сообщение) 
Тут есть много информации, но 70% ее зачастую просто не используется. Давайте попробуем отбросить то, что нам не нужно. Теперь нужно придумать, что можно ответить и сформировать ответ.""",
6:"""Ответ на сообщение представляет стандартный http-запрос, в котором мы должны указать метод и обязательные параметры, чтобы он сработал, а также тут присутствует токен нашего бота. Токен – уникальный идентификатор длинной около 14 символов, если вы уже работали с API некоторых сайтов, как OpenWeather, OpenWiki, Google API  к примеру, то вы понимаете о чем я говорю. С помощью него телеграмм-сервера понимают с каким именно ботом им нужно работать. 
Вообще такая система токенов очень часто используется в веб-приложениях. Его лучше никому не говорить, так как человек может запросто потом отправлять сообщения с помощью вашого бота пользователям.""",
7:"""Плюсы
1. Легкий и быстрый с точки зрения разработки
2. Как не странно также быстр и в отправлении ответов
3. Интеграция сторонних сервисов 
4. Интерфейс однообразен и понятен всем пользователям
5. Затрачивает мало ресурсов
6. Невозможно заDDoSить 
7. Всю «грязную работу» берет на себя сервер мессенджера 
""",
8:"""Минусы
1. Что-то сложное и полезное написать с таким интерфейсом вряд ли удастся
2. Падает сервер мессенджера – падает бот
3. Разные мессенджеры уже должны использовать разные программные интерфейсы (API)
4. Цензура мессенджера """
}

photos = ['AgADAgADE6kxG7Y6MUkYWZrYzFFVtz3hDw4ABBuZdo7OrOVLZpYDAAEC',
          'AgADAgADFKkxG7Y6MUkqqk2J7vX4eb0QMw4ABKINZVyd2tKQ9DcBAAEC',
          'AgADAgADFakxG7Y6MUlr7npEe-HzqFTkDw4ABOC2tsTodunNhJkDAAEC',
          'AgADAgADFqkxG7Y6MUm25rtBE6pKurv7Mg4ABB1yYqWDO4kuDjwBAAEC',
          'AgADAgADF6kxG7Y6MUlXhJshjqQIhRLEDw4ABO2-vO-UKMZOh48DAAEC',
          'AgADAgADGKkxG7Y6MUlA2J3RMCnDmzrXDw4ABKofeV9QxS5EbJgDAAEC',
          'AgADAgADGakxG7Y6MUk4zzCkRXUMJaoRMw4ABKNnHN1hx6L15zkBAAEC',
          'AgADAgADGqkxG7Y6MUnZsMa0Qjtgo38TMw4ABEISIZzK1SjXLzwBAAEC',
          'AgADAgADJ6kxG7Y6MUkwtJuMOdR7NksDMw4ABOaYVdPnRg5q6joBAAEC',
          'AgADAgADKKkxG7Y6MUkWPwGtSfJ6-ZXLDw4ABIpHIm2IWPu-5ZkDAAEC',
          'AgADAgADKakxG7Y6MUnh7V_OZui19Qj-Mg4ABJEH99aigNlcBjwBAAEC',
          'AgADAgADKqkxG7Y6MUk4UIRoNTP1lMgWMw4ABNRVfahvNtB34jwBAAEC',
          'AgADAgADK6kxG7Y6MUmJUaSb07P9kxoAATMOAATBTdzmh5nnYlM9AQABAg']