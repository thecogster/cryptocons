#### terminal commands

## Creates a project 
django-admin startproject myproject

## Create an app
python manage.py startapp appname

## Make preliminary sql code for table creation 
python manage.py makemigrations appname

## Check potential migrations 
python manage.py sqlmigrate appname  migrationscode_0001


## If there is problem with data models recommend clearing pycache and the sqlite db file 

## Stopping a process 
windows key + r resmon.exe navigate to CPU and search for exact file name 

## Lists dictionary Business with how many rows of data we have  
Business.objects.all()
## Store row output as variable
>>> b1 = Business.objects.get(id = '1')

## Adding data 
business_row = Business( business_name = '', business_address = .......)

## Save changes to database
business_row.save()


## You can get user data from foreign key table
 example business_name.author.name

## model_name_set gives us a filtered look at user_cians Businesses 
user_cian.Business_set.all()

## Creates a new Business for user_cian
user_cian.Business_set.create()