# 🍰 Cake Cottage
Welcome to Cake Cottage corner, your online book of delightful recipes! Whether you're a passionate home baker or a curious foodie, our platform allows you to explore, create, and share your favorite baked goods.

## 📌 Table of Contents

User Stories

About the Website

🚀 Features

🛠 Technologies Used

🔹 API Endpoints

🔒 User Authentication

🌍 Deployment

✅ Feel Free to Explore!

📌 Getting Started

🤝 Contributing


### User Stories
"**_As a user, I would like to_** _____________________________"

:white_check_mark: *denotes items that have been successfully implemented*

- :white_check_mark: 'register and log in, so that I can create and manage my recipes.'
- :white_check_mark: 'create, update, and delete recipes, so that I can share and manage my recipes.'
- :white_check_mark: 'comment on a recipe, so that I can give feedback or ask questions.'
- :white_check_mark: 'submit, view, and comment on recipes'
- :white_check_mark: ''

"**_As the developer, I want to_"

- :white_check_mark: 'manage the recipes and user comments, so that I can ensure the website maintains quality content.'
- :white_check_mark: 'optimize my website for faster loading so that users can have a better experience.'
- :white_check_mark: 'be able to test the app and find no errors so that users can use it smoothly'

## 🔠 Typography
We have carefully selected typography that complements the aesthetic of Cake Cottage:

[Google Fonts](https://fonts.google.com/) - Custom fonts are used to create a welcoming and warm feel for users.
    
## 🔹 Existing Features
### 👤 User Authentication & Profile Management
✔️ **Register Account** – Users can create an account with secure authentication.

✔️ **Log In** – Existing users can access their accounts securely.

✔️ **Change Password** – Users can update their passwords from their profile.

✔️ **Log Out** – A simple one-click logout button.

✔️ **Delete Account** – Users can remove their entire account along with their recipes.

### 🍰 Recipe Management

✔️ View All Desserts – A collection of desserts displayed with pagination.

✔️ Search Desserts – Users can search by category, name, or specific ingredients.

✔️ Add a Recipe – Users can submit their own recipes with images and descriptions.

✔️ View a Recipe – Detailed view of each recipe with ingredients and instructions.

✔️ Update a Recipe – Users can edit their own recipes.

✔️ Delete a Recipe – Users can remove their own recipes from the database.

✔️ Save to Favorites – Users can save recipes for quick access later.

### 🎉 Community Engagement

✔️ Like & Comment on Recipes – Users can interact with others by liking and commenting on recipes.

✔️ Share Recipes – Users can share their favorite recipes via social media.

🛠️ Admin Features

✔️ Manage User Accounts – Admin can edit or delete users.

✔️ Approve & Moderate Recipes – Admin can manage submitted content.

✔️ Track Site Activity – Admin can view analytics on user interactions.

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

# 📖 About the Website

Cake Cottage is more than just a bakery website—it's a community-driven recipe hub where users can:

🍰 Explore Our Menu – Browse through a collection of freshly baked goods, including cakes, pastries, and breads.

📜 View Recipes – Each product comes with a detailed recipe section to help you recreate your favorite treats at home.

💬 Leave Comments & Likes – Engage with other baking enthusiasts by sharing thoughts and feedback on recipes.

📩 Contact Us – Reach out for custom orders, inquiries, or just to say hello!

## 🚀 Features

✨ User Recipes – Create and share your own baking masterpieces.

📌 Interactive Menu – View our collection of baked goods with detailed descriptions.

👍 Recipe Comments & Likes – Engage with the baking community.

📱 Responsive Design – Accessible on all devices.

## Features Left to Implement

## 🛠 Technologies Used

- [VS Code](https://code.visualstudio.com/) - Used as my primary IDE for coding.
- [GitHub](https://github.com/) - Used as remote storage of my code online.

### 🖥️ Front-End Technologies

- [HTML](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5)  - Used as the base for markup text.
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS/CSS3) - Used as the base for cascading styles.
- [JavaScript](https://developer.mozilla.org/en-US/docs/Web/JavaScript) – Enhancing interactivity.
- [Bootstrap](https://getbootstrap.com/) – Providing a responsive design.


### 🖥️ Back-End Technologies
  Cake Cottage website is powered by a robust backend built with Django and PostgreSQL, ensuring scalability, security, and ease of development.

Technologies Used
* [Django 5.1.6](https://www.djangoproject.com/): A high-level Python web framework that simplifies development with its powerful ORM, authentication system, and built-in admin panel.

* [PostgreSQL](https://www.postgresql.org/): A powerful, open-source relational database used to store user-generated recipes, comments, and likes.

* [Gunicorn 23.0.0](https://gunicorn.org/): A WSGI HTTP server for running Django applications in production, ensuring efficient request handling.

* [psycopg2](https://pypi.org/project/psycopg2/): A PostgreSQL adapter for Python that allows Django to interact with the database.

* [dj-database-url](https://pypi.org/project/dj-database-url/): Simplifies database configuration by parsing database URLs from environment variables.
    
* [Whitenoise 6.9.0](https://whitenoise.readthedocs.io/en/latest/): Serves static files efficiently, allowing the site to perform well on platforms like Heroku.

* [django-heroku 0.3.1](https://pypi.org/project/django-heroku/): Automatically configures Django settings for deployment on Heroku.

### 🚀 Deployment
- **Heroku**
    - [Heroku](https://www.heroku.com) - Hosting platform.

## 🔹 API Endpoints
The backend provides a set of API endpoints to facilitate user interactions such as creating, updating, and retrieving recipes and comments.

### 📌 Recipe Endpoints
* GET /api/recipes/ – Retrieve all recipes

* POST /api/recipes/ – Create a new recipe (Authenticated users only)

* GET /api/recipes/<id>/ – Retrieve a single recipe

* PUT /api/recipes/<id>/ – Update a recipe (Owner only)

* DELETE /api/recipes/<id>/ – Delete a recipe (Owner only)

### 💬 Comment Endpoints

* GET /api/recipes/<id>/comments/ – Retrieve comments for a recipe

* POST /api/recipes/<id>/comments/ – Add a comment (Authenticated users only)

### ❤️ Like Endpoints

* POST /api/recipes/<id>/like/ – Like or unlike a recipe (Authenticated users only)

  
## 🔒 User Authentication
The app supports user authentication and authorization to ensure secure interactions.

* 🔑 Django Authentication System: Users can register, log in, and manage their accounts.

* 🔐 Session-Based Authentication:  Maintains user login sessions securely.

* 👤 Permissions & Access Control: Users can create and modify their own recipes; only owners can edit or delete them.

## 🌍 Deployment

The website is hosted on Heroku, leveraging PostgreSQL as the production database. Whitenoise efficiently manages static files for improved performance.

## ✅ Feel Free to Explore!
The Little Cake Cottage is a friendly and welcoming space for all baking lovers. Whether you're a beginner or an experienced baker, you are encouraged to:

* ✅ Give a like to recipes that inspire you.

* ✅ Share your baking journey by writing your own recipes.

* ✅ Engage with the community by commenting on and discussing recipes.

* ✅ Try new recipes and improve your baking skills!

* 🎉 Join us in making baking fun, creative, and interactive. Start exploring today! 🍪🥧🎂

 # 📌 Getting Started
 ## 🏗️ Installation Guide
 
1️⃣ Clone repository: [https://github.com/HBica05/cake-cottage.git]
 
2️⃣ Set up a virtual environment and install dependencies:
    
    `python -m venv env`

    `source env/bin/activate` --> On Windows use: `env\Scripts\activate`

    `pip install requirements.txt`

3️⃣ Configure the database: `python manage.py migrate`
   
4️⃣ Run the development server: `python manage.py runserver`
 
5️⃣ Open your browser and visit: [ ]

## 🤝 Contributing
- 🎉 We welcome contributions! Feel free to submit pull requests, report issues, or suggest new features.
  
 
 ##### 📌 Back to [top](##table-of-contents)