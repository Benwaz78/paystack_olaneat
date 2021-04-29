from django.db import models


# Create your models here.


class Book(models.Model):
	book_title = models.CharField(max_length=40)
	image = models.FileField(upload_to='uploads/')
	price = models.DecimalField(max_digits=12, decimal_places=2)
	description = models.TextField()


	def book_image(self):
		if self.image:
			return self.image.url

	def __str__(self):
		return self.book_title


class Payment(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email_name = models.CharField(max_length=50)
	phone = models.CharField(max_length=15)
	book = models.ForeignKey(Book, on_delete=models.CASCADE)

	def __str__(self):
		return self.first_name
	
	