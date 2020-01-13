from django.apps import AppConfig


class MoviesConfig(AppConfig):
    name = 'movies'
    '''Отображение названия приложения на русском, а так же смотри в _init_.py'''
    verbose_name = 'Фильмы'
