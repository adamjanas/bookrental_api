from rest_framework import serializers
from bookrental_app.models import Book, Kind, Reader


class BookSerializer(serializers.ModelSerializer):
	class Meta:
		model = Book
		fields = ('id', 'name', 'kind')
	
class KindSerializer(serializers.ModelSerializer):
	class Meta:
		model = Kind
		fields = ('id', 'name')

class ReaderSerializer(serializers.ModelSerializer):
	class Meta:
		model = Reader
		fields = ('id', 'name', 'books')
		