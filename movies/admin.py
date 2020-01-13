from django.contrib import admin
from .models import Category, Genre, Movie, MovieShots, Actor, Rating, RatingStar, Reviews
from django.utils.safestring import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Категори'''
    list_display = ('id','name', 'url')
    list_display_links = ('name',)

class ReviewInline(admin.TabularInline):
    '''Отзывы'''
    model = Reviews
    extra = 1
    readonly_fields = ('name', 'email',)


class MovieShotsInline(admin.TabularInline):
    model = MovieShots
    extra = 1
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="100" height="100"')

    get_image.short_description = 'Изображения'


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    '''Фильмы'''
    list_display = ('title', 'category', 'url', 'draft')
    list_filter = ('category', 'year',)
    search_fields = ('title', 'category__name',)
    inlines = [MovieShotsInline, ReviewInline]
    save_on_top = True
    save_as = True
    list_editable = ('draft',)
    # fields = (('actors', 'directors', 'genres'),)
    readonly_fields = ('get_image',)
    fieldsets = (
        (None, {
            'fields': (('title', 'tagline'),)
        }),
        (None, {
            'fields': ('description', ('poster', 'get_image'),)
        }),
        (None, {
            'fields': (('year', 'world_premiere', 'country'), )
        }),
        ('Actors', {
            'classes': ('collapse',),
            'fields': (('actors', 'directors', 'genres', 'category'),)
        }),
        (None, {
            'fields': (('budget', 'fees_in_usa', 'fees_in_world'),)
        }),
        ('Options', {
            'fields': (('url', 'draft'),)
        }),
    )

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.poster.url} width="100" height="100"')

    get_image.short_description = 'Постер'

@admin.register(Reviews)
class ReviewAdmin(admin.ModelAdmin):
    '''Отзывы'''
    list_display = ('name', 'email', 'parent', 'movie', 'id')
    readonly_fields = ('name', 'email',)

@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    '''Жанры'''
    list_display = ('name', 'url',)

@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    '''Актёры'''
    list_display = ('name', 'age', 'get_image',)
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = 'Изображения'

@admin.register(Rating)
class RatingAdmin(admin.ModelAdmin):
    '''Рейтинг'''
    list_display = ('movie', 'ip',)

@admin.register(MovieShots)
class MovieShotsAdmin(admin.ModelAdmin):
    '''Кадры из фильма'''
    list_display = ('title', 'movie', 'get_image',)
    readonly_fields = ('get_image',)

    def get_image(self, obj):
        return mark_safe(f'<img src={obj.image.url} width="50" height="60"')

    get_image.short_description = 'Изображения'


# admin.site.register(Category, CategoryAdmin)
# admin.site.register(Genre)
# admin.site.register(Movie)
# admin.site.register(MovieShots)
# admin.site.register(Actor)
# admin.site.register(Rating)
admin.site.register(RatingStar)
# admin.site.register(Reviews)

admin.site.site_title = 'Django Movies'
admin.site.site_header = 'Django Movies'