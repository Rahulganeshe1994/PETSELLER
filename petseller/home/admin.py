from django.contrib import admin
from home .models import (Animal ,AnimalBreed,AnimalColor,AnimalImages,AnimalLocation, Category)


admin.site.register(Animal)
admin.site.register(Category)
admin.site.register(AnimalBreed)
admin.site.register(AnimalColor)
admin.site.register(AnimalImages)
admin.site.register(AnimalLocation)

