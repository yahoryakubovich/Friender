from django.contrib import admin
from .models import *
from django.utils.html import format_html
from django.utils.safestring import mark_safe

color_code = "ffd700"


@admin.action(description="Change a city")
def change_a_city(modeladmin, request, queryset):
    queryset.update(city="Minsk")


# @admin.display(description="ФИО")
# def upper_case_name(obj):
#     return f"{obj.name} {obj.surname}".upper()

class RatingInLine(admin.TabularInline):
    model = UserRating
    verbose_name = "Рейтинг пользователя"


class HobbiesInLine(admin.StackedInline):
    model = Hobbies.user.through
    verbose_name = "Пользователь данного хобби"
    verbose_name_plural = "Пользователи данного хобби"


@admin.register(Users)
class UsersAdmin(admin.ModelAdmin):
    @admin.display
    def colored_name(self):
        return format_html(
            '<span style="color: #{};">{} {}</span>',
            color_code,
            self.name,
            self.surname,
        )

    def profile_photo(self, objects):
        if objects.photo:
            return mark_safe(f"<img src={objects.photo.url} width=50>")

    fields = [("name", "surname"), "age", "sex", "email", "city", "photo"]
    list_display = [colored_name, "name", "surname", "age", "sex", "city", "profile_photo"]
    list_display_links = ["name", "surname"]
    ordering = ["name"]
    search_fields = ["age", "city", "sex"]
    list_filter = ["age", "city", "sex"]
    list_per_page = 20
    inlines = [
        RatingInLine,
        HobbiesInLine,
    ]
    actions = [change_a_city]


@admin.register(Passport)
class PassportAdmin(admin.ModelAdmin):
    fields = ["passport_id", "date_create", "user"]
    list_display = ["passport_id", "date_create", "user"]
    list_display_links = ["passport_id"]
    ordering = ["passport_id"]
    search_fields = ["passport_id"]
    list_per_page = 20


@admin.register(Hobbies)
class HobbiesAdmin(admin.ModelAdmin):
    fields = ["name_hobby", "category", "user"]
    list_display = ["name_hobby", "category"]
    list_display_links = ["name_hobby"]
    ordering = ["name_hobby"]
    search_fields = ["name_hobby", "category"]
    list_filter = ["name_hobby", "category"]
    list_per_page = 20
    inlines = [
        HobbiesInLine,
    ]


@admin.register(Establishments)
class EstablishmentsAdmin(admin.ModelAdmin):
    def profile_photo(self, objects):
        if objects.photo:
            return mark_safe(f"<img src={objects.photo.url} width=50>")

    fields = ["name", "category", "address", "phone", "photo"]
    list_display = ["name", "category", "address", "phone", "profile_photo"]
    list_display_links = ["name"]
    ordering = ["name"]
    list_per_page = 20


admin.site.register(UserRating)
admin.site.register(EstablishmentsRating)
admin.site.register(Appointments)
admin.site.register(Host)
admin.site.register(Guest)
admin.site.register(Order)
