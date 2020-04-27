from django.test import TestCase
from bookrental_app.models import Book, Kind, Reader
from bookrental_app.serializers import BookSerializer, KindSerializer, ReaderSerializer
from rest_framework.test import APITestCase, APIClient
from django.urls import reverse
from rest_framework.views import status
from rest_framework.authtoken.models import Token
from . import settings

class BaseViewTest(APITestCase):

	client = APIClient()
	

	
	@staticmethod
	def create_book(name="", kind=""):
		if name != "" and kind != "":
			Book.objects.create(name=name, kind=kind)


	def setUp(self):
		self.create_book("book1", "kind1")
		self.create_book("book2", "kind2")
		self.create_book("book3", "kind3")
		self.create_book("book4", "kind4")

	

class UserTokenJWTGenerator:
	@classmethod
	def generate_token(cls, user):
	    return jwt_encode_handler(jwt_payload_handler(user))


class GetAllBooksTest(BaseViewTest):

	def test_get_all_books(self):

		response = self.client.get(reverse('books-list'))

		expected = Book.objects.all()
		serialized = BookSerializer(expected, many=True)
		self.assertEqual(response.data, serialized.data)
		self.assertEqual(response.status_code, status.HTTP_200_OK)



	





