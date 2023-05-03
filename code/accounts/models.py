from django.db import models
from django.db.models  import IntegerField

from django.contrib.auth.models import User
from django.core.validators import MaxValueValidator, MinValueValidator
from django.forms import DateInput
import crum

# Create your models here.
# from django.contrib.auth.models import AbstractUser

# class CustomUser(AbstractUser):
#     # add additional fields in here
# 	full_name = models.CharField(max_length=100, null = True)
# 	telephone_number = models.BigIntegerField( null = False)
# 	email = models.EmailField(null = False)
# 	def __str__(self):
# 		return self.username



class Business(models.Model):
	id = models.BigAutoField(primary_key=True)

	def save(self, *args, **kwargs):
		user = crum.get_current_user()
		if user and not user.id:
			user = None
		if not self.id:
			self.created_by = user
		self.author = user
		super(Business, self).save(*args, **kwargs)
	
	author = models.ForeignKey('auth.User', blank=True, default=crum.get_current_user(), on_delete = models.CASCADE, null = True)
	class business_sector(models.TextChoices):
		Retail = '1', "Retail"
		Professional = '2', "Professional"
		Services = '3', 'Services'
		Food_and_Drink = '4', 'Food_and_Drink'
		Entertainment = '5', 'Entertainment'

	business_name = models.CharField(max_length=100, null = True)
	business_address = models.CharField(max_length=100, null = True)
	company_number = models.IntegerField(null = True)
	business_sector_name = models.CharField(max_length=2, choices=business_sector.choices, default=business_sector.Entertainment)

	# def save(self, *args, **kwargs):
	# 	user = get_current_user()
	# 	if user and not user.id:
	# 		user = None
	# 	if not self.id:
	# 		self.created_by = user
	# 	self.author = user
	# 	super(Business, self).save(*args, **kwargs)
		
	def __str__(self):
		return self.business_name




class BusinessLoan(models.Model):
	id = models.BigAutoField(primary_key=True)
	CURRENCIES =[                                                                                                                                                                                                                        
		('USD', 'US Dollars'),                                                                                                                                                                                                                    
        ('EUR', 'Euro'),                                                                                                                                                                                                                          
        ('GBP', 'British Pound'),                                                                                                                                                                                                                 
        ('AUD', 'Australian Dollar')]
	currency = models.CharField(max_length=4, choices=CURRENCIES)
	loan_value = models.IntegerField( default=1, validators=[MaxValueValidator(100000), MinValueValidator(10000)])
	loan_length_in_days = models.IntegerField(default=180)
	business_id = models.ForeignKey(Business, on_delete = models.CASCADE, null = True)

	def __int__(self):
		return self.id

# class CustomUser(AbstractUser):
#     # add additional fields in here
# 	full_name = models.CharField(max_length=100, null = True)
# 	telephone_number = models.BigIntegerField( null = False)

# 	def __str__(self):
# 		return self.username


	
