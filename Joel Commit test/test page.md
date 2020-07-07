# PracticalTask1_v1a
Instructions for Practical Task 1 of the IT6036 course:

INSTALLATION INSTRUCTIONS

1. Download the zip file to your computer, and then extract the folder.

2. Open a command line and cd.. to the root directory of the app.

3. Create and activate the virtual environment.

4. Install Django (you may need to use proxy settings).

5. Create and run the migrations like this => 
  python manage.py migrate 
  You should see messages starting: 
  Applying contenttypes.0001_initial... OK 
  Applying auth.0001_initial... OK (... etc.)

6. Load the app users and app data like this => 
  python manage.py load_userprofile_data 
  You should see these messages: 
  Loading User data for the user profile... 
  Loading users...

7. Run the server => 
  python manage.py runserver

8. Open a browser and go to http://127.0.0.1:8000/ 
  You should see the home page of the kiwirecruit app.

9. Use the login credentials below to explore the app!

USER LOGIN USERNAMES AND PASSWORDS 
regt	regt1234 
zach	zach1234 
austf	aust1234 
howiec	howi1234 
sandieg	sand1234 
philr	phil1234 
krysv	krys1234

ADMIN LOGIN FOR DJANGO (OPTIONAL!)

If you want access to the Django admin then you first need to create a superuser. Follow the instructions below:

1. Open a command line and cd.. to the root directory of the app.

2. Create a superuser like this => 
python manage.py createsuperuser

3. Follow the prompts to enter a new username and password.

4. To login to the django admin, open a browser and go to http://127.0.0.1:8000/admin/
