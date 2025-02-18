# Cake Cottage
Welcome to Cake Cottage corner, your online book of delightful recipes! Whether you're a passionate home baker or a curious foodie, our platform allows you to explore, create, and share your favorite baked goods.

## Table of Contents

### User Stories
"**_As a user, I would like to_** _____________________________"

:white_check_mark: *denotes items that have been successfully implemented*

- :white_check_mark:
- :white_check_mark:
- :white_check_mark:
- :white_check_mark:
- :white_check_mark:

## About the Website
Cake Cottage is more than just a bakery website—it's a community-driven recipe hub where users can:

* Explore Our Menu: Browse through our collection of freshly baked goods, including cakes, pastries, and breads.

* View Recipes: Each product comes with a detailed recipe section, allowing users to recreate their favorite treats at home.

* Leave Comments & Likes: Engage with other baking enthusiasts by sharing your thoughts and feedback on recipes.

* Contact Us: Reach out for custom orders, inquiries, or just to say hello.

## 🚀 Features

* User Recipes – Create and share your own baking masterpieces.

* Interactive Menu – View our collection of baked goods with detailed descriptions.

* Recipe Comments & Likes – Engage with the baking community by leaving feedback and showing appreciation.

* Responsive Design – Accessible on all devices for a seamless experience.



## Typography
[Google Fonts](link_here)
    
## Existing Features
**Register Account**
- Anybody can register for free and create their own unique account. I have built-in authentication and authorization to check certain criteria is met before an account is validated. All passwords are hashed for security purposes!

**Log In to Account**
- For existing users, I have more authentication and authorization incorporated to check that the hashed passwords and username match the database.

**Change Password**
- Users can update their passwords from their profile page, after first validating their existing password.

**Log Out of Account**
- Users can easily log out of their account with the click of a button.

**Delete Account**
- Users can delete their entire account, but a warning is provided to first validate their password, and advise that all of their own recipes will also be deleted, and their favorites removed.

**View All Desserts**
- On the *desserts* page, all recipes are initially displayed in an alphabetical order, with a standard 12-items per page using pagination.

**Search Desserts**
- If a user would like to search for something specific, whether it's a particular recipe, a certain dessert category, or for recipes that exclude certain allergens, then the Search button is perfect! There's also an option to sort the results by a number of different options, order them by either ascending or descending, and even limit the number of results that are displayed per page.

**Add a Recipe**
- [**C**RUD] Create or 'add' a new recipe. Defensive programming in place means users must adhere to minimal requirements when adding a new recipe. If a user doesn't have a photo to accompany their recipe, I have a built-in function that will automatically assign a cute placeholder image based on the type of dessert category they've selected.

**View a Recipe**
- [C**R**UD] Read or 'review' recipes, either from the main page, or the user profile. From here, users also have additional options:
    - Print the recipe.
    - Share the recipe.
    - Check ingredients / directions as 'complete' if making the recipe themselves.
    - View two additional recipe suggestions.
    - View a *conversion chart* either by temperature, volume, or weight.

**Update a Recipe**
- [CR**U**D] Update or 'edit' their own user recipes on this page.

**Delete a Recipe**
- [CRU**D**] Delete or 'remove' a user's own recipes. The *admin* account also has access to delete recipes, should they be inappropriate for example.

**Save a Recipe to Favorites**
- Users can save their own recipes, or recipes submitted by other users, directly into their profile for quicker access next time.


**Admin Superuser**
- My ***'Admin'*** profile has several extra features, which currently include:
    - Edit / Delete any recipe from the database.
    - View join-date / favs / recipes of all registered users. (added February 2020)
    - Delete any registered user from the database. (added February 2020)
    - Receive email for new recipes added or edited from database as backup in case database is lost. (added March 2020)
    - View an interactive map of all visitors to the site. (added April 2020)
    - View statistics of unique visitors by country, and total count. (added April 2020)

## Features Left to Implement


## Technologies Used

- [VS Code](https://code.visualstudio.com/) - Used as my primary IDE for coding.
- [GitHub](https://github.com/) - Used as remote storage of my code online.

### Front-End Technologies

- [HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) - Used as the base for markup text.
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3) - Used as the base for cascading styles.

### Back-End Technologies
  Cake Cottage website is powered by a robust backend built with Django and PostgreSQL, ensuring scalability, security, and ease of development.

Technologies Used
* [Django 5.1.6](https://www.djangoproject.com/): A high-level Python web framework that simplifies development with its powerful ORM, authentication system, and built-in admin panel.

* [PostgreSQL](https://www.postgresql.org/): A powerful, open-source relational database used to store user-generated recipes, comments, and likes.

* [Gunicorn 23.0.0](https://gunicorn.org/): A WSGI HTTP server for running Django applications in production, ensuring efficient request handling.

* [psycopg2](https://pypi.org/project/psycopg2/): A PostgreSQL adapter for Python that allows Django to interact with the database.

* [dj-database-url](https://pypi.org/project/dj-database-url/): Simplifies database configuration by parsing database URLs from environment variables.
    
* [Whitenoise 6.9.0](https://whitenoise.readthedocs.io/en/latest/): Serves static files efficiently, allowing the site to perform well on platforms like Heroku.

* [django-heroku 0.3.1](https://pypi.org/project/django-heroku/): Automatically configures Django settings for deployment on Heroku.

- **Heroku**
    - [Heroku](https://www.heroku.com) - Used for app hosting.

- **Python**    
    - [Python 3.11.9](https://www.python.org/) - Used as the back-end programming language.

## API Endpoints
The backend provides a set of API endpoints to facilitate user interactions such as creating, updating, and retrieving recipes and comments.

### Recipe Endpoints
* GET /api/recipes/ – Retrieve all recipes

* POST /api/recipes/ – Create a new recipe (Authenticated users only)

* GET /api/recipes/<id>/ – Retrieve a single recipe

* PUT /api/recipes/<id>/ – Update a recipe (Owner only)

* DELETE /api/recipes/<id>/ – Delete a recipe (Owner only)

### Comment Endpoints

* GET /api/recipes/<id>/comments/ – Retrieve comments for a recipe

* POST /api/recipes/<id>/comments/ – Add a comment (Authenticated users only)

### Like Endpoints

* POST /api/recipes/<id>/like/ – Like or unlike a recipe (Authenticated users only)

## 🔹 User Authentication
The app supports user authentication and authorization to ensure secure interactions.

* Django Authentication System: Users can register, log in, and manage their accounts.

* Session-Based Authentication: Used for user authentication and maintaining login sessions.

* Permissions & Access Control: Users can create and modify their own recipes, while only the recipe owner can delete or edit them.

## 🔹 Deployment
The website is hosted on Heroku, leveraging PostgreSQL as the production database. With Whitenoise, static files are efficiently handled, ensuring fast load times.

##### Back to [top](##table-of-contents)

## ✅ Feel Free to Explore!
The Little Cake Cottage is a friendly and welcoming space for all baking lovers. Whether you're a beginner or an experienced baker, you are encouraged to:

* Give a like to recipes that inspire you.

* Share your baking journey by writing your own recipes.

* Engage with the community by commenting on and discussing recipes.

* Try new recipes and improve your baking skills!

* Join us in making baking fun, creative, and interactive. Start exploring today! 🍪🥧🎂

## Technologies Used

* Frontend: HTML, CSS, JavaScript (Bootstrap for styling).

* Backend: Python (Django framework).

* Database: PostgreSQL (for production).

* Deployment: Hosted on Heroku with PostgreSQL integration.
  
 # Getting Started
 1. Clone repository:[https://github.com/HBica05/cake-cottage.git]
 2. Set up a virtual environment and install dependencies:
    
    `python -m venv env`

    `source env/bin/activate` --> On Windows use: `env\Scripts\activate`

    `pip install requirements.txt`

 3. Configure the database: `python manage.py migrate`
   
 4. Run the development server: `python manage.py runserver`
 5. Open your browser and visit: [ ]

## Contributing
- We welcome contributions! Feel free to submit pull requests, report issues, or suggest new features.
  
 
 ##### Back to [top](##table-of-contents)