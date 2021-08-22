from django.contrib import admin
from .models import Superhero

# Register your models here.
admin.site.site_header = "Superheroes Admin"
admin.site.site_title = "Superheroes Admin Area"
admin.site.index_title = "Welcome to the Superheroes Admin area"

admin.site.register(Superhero)