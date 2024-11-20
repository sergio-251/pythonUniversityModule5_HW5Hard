from time import sleep


class UrTube:
    def __init__(self):
        self.users = User.get_users()
        self.videos = []
        self.current_user = None

    def log_in(self, nickname, password):
        if nickname in User.get_nicknames():
            if User.get_user(nickname)[0].password == hash(password):
                self.current_user = User.get_user(nickname)[0]
            else:
                print('Пароль совсем не пароль!')
        else:
            print('Мы таких не знаем!')

    def register(self, nickname: str, password: str, age: int):
        if nickname not in User.get_nicknames():
            self.current_user = User(nickname, password, age)
        else:
            print(f'Пользователь {nickname} уже существует')

    def add(self, *args):
        self.videos.extend([v for v in args if
                            all([v.title.lower() != self.videos[_].title.lower() for _ in range(len(self.videos))])])

    def get_videos(self, search_str):
        return [v.title for v in self.videos if search_str.lower() in v.title.lower()]

    def watch_video(self, title):
        if self.current_user:
            if len(self.get_videos(title)) != 0 and title == self.get_videos(title)[0]:
                current_video = [self.videos[i] for i in range(len(self.videos)) if self.videos[i].title == title]
                if self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                else:
                    for i in range(current_video[0].duration):
                        print(i + 1, end=' ')
                        sleep(1)
                    print('Конец видео')
        else:
            print('Войдите в аккаунт, чтобы смотреть видео')


class Video:
    __videos = []

    @classmethod
    def get_videos(cls):
        return cls.__videos

    def __init__(self, title: str, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode
        Video.__videos.append(self)


class User:
    __users = []  # Инкапсуляция, чтобы нельзя было изменить список вручную из любой точки программы

    @classmethod
    def get_users(cls):
        return cls.__users

    @classmethod
    def get_nicknames(cls):
        return [cls.__users[i].nickname for i in range(len(cls.__users))]

    @classmethod
    def get_user(cls, nickname):
        return [cls.__users[i] for i in range(len(cls.__users)) if cls.__users[i].nickname == nickname]

    def __str__(self):
        return self.nickname

    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age
        User.__users.append(self)


ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
ur.log_in('urban_pythonist', 'iScX4vIJClb9YQavjAgF')
print(ur.current_user)
ur.log_in('urban_pythonist', '1111111')
ur.log_in('Sergey', 'qY3Id88H!xc')
ur.register('Sergey', 'qY3Id88H!xc', 42)
print(ur.current_user)
