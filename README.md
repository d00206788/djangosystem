# djangosystem

virt env name = djangosystem
project name = djangomainproject
app name = djangoapp

db name = projectdjangodatabase (postgresql)

admin django = user: katie 
               pw: fluffyrice

urls: /home/ >> the main page after logging in
/login/ >> login page
/register/ >> register account page
/logout/ >> logout page
/breeds/ >> view dog breeds and info page
/user/ >> view user profile
/password_change/ >> change account password
/create_dog/ >> add a new dog to db

This application is a dog management system. It allows users to store info regarding their dogs, such as age, name, breed and status.

issues: i created a class called User, not knowing this was a special django command, which led me to some issues in displaying the User class. I renamed the class to Usersinfo, however it still would not perform as expected.
I will know for future to be careful with naming classes and ensuring they do not clash with special django commands.

tests i have run:
testing that all fields in signup and register need to be filled out otherwise form is not valid, same with update user info form.


 
