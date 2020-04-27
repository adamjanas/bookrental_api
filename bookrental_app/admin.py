from django.contrib import admin
from bookrental_app.models import Book, Kind, Reader

admin.site.register(Book)
admin.site.register(Kind)
admin.site.register(Reader)

