from django.shortcuts import render
from rest_framework import viewsets, permissions
from bookrental_app.models import Book, Kind, Reader
from bookrental_app.serializers import BookSerializer, KindSerializer, ReaderSerializer


class BookView(viewsets.ModelViewSet):
	queryset = Book.objects.all()
	serializer_class = BookSerializer

class KindView(viewsets.ModelViewSet):
	queryset = Kind.objects.all()
	serializer_class = KindSerializer

class ReaderView(viewsets.ModelViewSet):
	queryset = Reader.objects.all()
	serializer_class = ReaderSerializer
	