# Сиквел "Герой и Чудовища 2: волшебный тотем" (текстовая игра).

Игрок: рыцарь в фантастической стране. Задача игрока: победить 10 чудовищ, чтобы спасти королевство от нападения и тем самым выиграть игру.


# Описание игры:

В игре есть ри вида чудовищ, каждый со своим типом атаки.

У героя тоже есть класс на выбор: он может быть воином, лучником или магом. Класс нужно выбрать в начале игры.

Попадающиеся предметы тоже могут быть разными:

    меч

    лук

    стрелы

    книга заклинаний

    яблочко

    тотем

Если класс игрока — воин, то максимальный предел случайного показателя атаки от попадающегося меча должен быть увеличен. Воин может случайным образом защищаться от атак ближнего боя.

Если класс игрока — лучник, то максимальный предел случайного показателя атаки от попадающегося лука должен быть увеличен. Лучник может случайным образом защищаться от атак лучников.

Если класс игрока — маг, то максимальный предел случайного показателя атаки от попадающейся книги заклинаний должен быть увеличен. Маг может случайным образом защищаться от магических атак.

При битве герою предоставляется тип атаки на выбор. Нельзя выбрать атаку оружие для которой недоступно.

Независимо от класса, герой начинает свой путь с мечом.

Атака теперь ведётся пошагово. После каждого удара можно выбрать другую атаку если и протагонист и противник ещё живы. Во время боя есть вариант убежать от противника.

Тотем позволяет сохранить текущее состояние игры. Тотем можно подобрать или обойти. Если у героя есть тотем - можно при проигрыше загрузить игру с момента поднятия предыдущего волшебного тотема. Загрузка одноразовая - при использовании тотема место сохранения теряется. Можете воспринимать тотем как одноразовое сохранение.


# Выбранный шаблон проектирования:

Абстрактная фабрика.


# Обоснование выбора шаблона проектирования:

При написании игры будут создаваться объекты (чудовища, герои, оружие). Основные паттерны поведения каждого объекта одни и те же, поведение их будет различаться лишь в зависимости от выбора типа объекта (например, герой-маг, чудовище-лучник). 

Наша абстрактная фабрика будет создавать семейства объектов, и из нее будут создаваться конкретные фабрики для каждого из типов таких объектов. 

Таким образом, можно реализовать принцип открытости-закрытости, упростить добавление новых типов объектов, упростить поддержку кода.


