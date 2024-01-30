# Recipe Repository Backend

[Click here for the Frontend Repository](#https://github.com/Moonchichiii/backend_postit_repository)

[Click here for Live site](#)

## Table of Contents

1.  [Project Goals](#project-goals)
2.  [User Stories](#user-stories)
3.  [Database Management](#database-management)
4.  [Backend Structure and Setup](#backend-structure-and-setup)
5.  [API Endpoints](#api-endpoints)
6.  [Technologies Used](#technologies-used)
7.  [Dependencies](#dependencies)
8.  [Testing](#testing)
9.  [Deployment](#deployment)
10.  [Credits & Tutorials](#credits-&-tutorials)

----------

## Project Goals  

The goal of this project is to develop a simple snappy, mobile-first social food posting website/application. 
The platform allows users to view and search for food posts without logging in.
Once logged in, users are directed to a dashboard with functionalities such as feed, liked posts, profile page, and post new recipe post.

----------

## User Stories 

1.  **As a Visitor**, I want to view and search for food posts without logging in, so I can explore content freely.  
2.  **As a User**, I need to register and log in, so I can access personalized features like my dashboard. 
3.  **As a User**, I want to navigate through different sections such as feed, liked posts, and my posts, for an organized view of content.
4.  **As a User**, I wish to post new recipes, so I can share my culinary creations with the community.
5.  **As a User**, I want to follow other profiles and like posts, to engage with the community.

[Back to top](#table-of-contents)
----------

## Database Management



<img src="https://github.com/Moonchichiii/backend_postit_repository/blob/main/readmecontent/images/dbvisual.png?raw=true" alt="database schema" width="320">


[Back to top](#table-of-contents)
----------

## Backend Structure and Setup

## Overview

-   **backend**: This is the main project folder. It contains the global settings and configurations that apply to the entire project.    
-   **utils**: This app provides shared services across the project. It includes important functions like handling images for both profiles and posts, managing permissions within the app, and validating image uploads.
-   **users**: App that handles user registration, along with login and logout processes. It ensures users can securely access their accounts.    
-   **profiles**: Manages everything related to user profiles. This includes updating public profile information and displaying it to other users.    
-   **posts**: The core app where recipe posts are managed. Here, users can create, view, update, or delete recipe posts.    
-   **comments**: Responsible for managing comments. This app allows users to add comments to posts and also links these comments with the respective posts.    
-   **likes**: This app takes care of the 'likes' feature. Users can 'like' posts, and this app manages these interactions and links them with the relevant posts.    
-   **followers**: Handles the functionality that lets profiles follow other profiles. About creating connections between different profiles.    


### Setting Up the Project
To set up the project, follow these steps:
1.  **Start a Django Project**:
`django-admin startproject backend .`
This creates the main project folder and the necessary files for the Django project.
2.  **Create Django Apps**: Navigate to the project directory and create the Django apps.
`django-admin startapp comments`

`django-admin startapp followers`
`django-admin startapp likes`
`django-admin startapp posts`
`django-admin startapp profiles`
`django-admin startapp users`
`django-admin startapp utils `
Each command creates a new app with its respective folder and basic files.
Then add urls.py and serializers.py in each app folder and link it back to the project urls.py. 

3.  **Configure Installed Apps**: Add the created apps to the `INSTALLED_APPS` list in `settings.py`
INSTALLED_APPS = [
`'cloudinary_storage',`
`'django.contrib.staticfiles',`
`'cloudinary',`

`'corsheaders',`

`'rest_framework',`
`'rest_framework_simplejwt',`

`'users',`
`'profiles',`
`'comments',`
`'followers',`
`'likes',`
`'posts',`

`'utils',`
]

4.  **Database Migrations**: After creating your models, run migrations to create the necessary database tables.
`python manage.py makemigrations`
`python manage.py migrate`
5.  **Run the Development Server**: To start the Django development server, run:
`python manage.py runserver`
This will start a local server

[Back to top](#table-of-contents)

----------

#### 1. Core Entities:

In the application, the primary entities are `users`, `profiles`, `posts`, `comments`, `likes`, and `followers`. Each of these plays a crucial role in the functionality and structure of the platform.

#### 2. Define Relationships:

-   **Profile and Posts**: A Profile can create more than one post, but each post is associated with one profile.
-   **Profile and Comments**: Each post can have many comments, linking back to both the post and the commenting profile.
-   **Profile and Likes**: Profile can 'like' multiple posts, and each post can be 'liked' by multiple profiles.
-   **Profile and Followers**: Profiles can follow and be followed by multiple other Profile, a network of connections.



[Back to top](#table-of-contents)
----------

## API Endpoints

-  GET /api/posts/: Retrieve a list of posts. -
-  POST /api/posts/: Create a new post. Title and content in the request. -
-  GET /api/posts/{id}/: Retrieve details of a specific post. -
-  PUT /api/posts/{id}/: Update a specific post. Title and content in the request. -
-  DELETE /api/posts/{id}/: Delete a specific post.

[Back to top](#table-of-contents)
----------

## Technologies Used
  
The backend repository is built and managed using these technologies.
-  Python: The core programming language of the project.
-  Vs Code: Visual Studio Code editor.
-  Django: A Python web framework employed for its ability to facilitate rapid development, serving as the backbone of the backend architecture.
-  Heroku: Utilized as the cloud platform for deploying and hosting the application.

-  PostgreSQL on Heroku: Reliability, serves as the primary database for the application, hosted on Heroku.
-  Cloudinary: Integrated for management and hosting of images, ensuring optimized media storage and delivery.
-  GitHub: Used for version control and source code management, tracking of changes throughout the development.

[Back to top](#table-of-contents)
----------

## Dependencies

Various libraries and frameworks used in this project:

1.  asgiref==3.7.2: Provides asynchronous support to Django, enabling features like async views and middleware.
2.  Django==5.0.1: The primary web framework used for building this application.
3.  django-cors-headers==4.3.1: Manages Cross-Origin Resource Sharing (CORS) settings, allowing for controlled access from different domains.
4.  djangorestframework==3.14.0: A powerful toolkit for building Web APIs, used for handling RESTful API endpoints.
5.  python-decouple==3.8: Helps in separating configuration parameters from code, enhancing security and flexibility.
6.  Pillow==10.1.0: A Python Imaging Library, used for image processing tasks in the application.
7.  cloudinary==1.37.0: Integrates Cloudinary services for efficient image and media asset management.
8.  dj3-cloudinary-storage==0.0.6: An extension for Cloudinary integration.
9.  django-filter==23.5: Utilized for filtering querysets in Django views or Django REST Framework viewsets.
10.  djangorestframework-simplejwt==5.3.1: Provides JSON Web Token (JWT) authentication for Django REST Framework.
11.  drf-spectacular==0.27.0: A Django REST Framework extension for generating API documentation.
12.  dj-database-url==2.1.0: Simplifies database configuration management, crucial for deployment scenarios.
13.  gunicorn==21.2.0: A Python WSGI HTTP Server for UNIX, serving the Django application in production environments.
14.  psycopg2-binary==2.9.9: A PostgreSQL database adapter, essential for PostgreSQL database integration.
15.  pytz==2023.3: Provides timezone support for Django, important for time-sensitive applications.
16.  sqlparse==0.4.2: A non-validating SQL parser, used for SQL formatting and parsing within Django.
17.  urllib3==1.26.9: Used for making HTTP requests, integral for communicating with external services.
18.  requests==2.26.0: A library for making HTTP requests.

[Back to top](#table-of-contents)
----------

## Testing
I've used Postman and Pytest for testing the project to make sure everything works.

### Postman for API Testing
Postman was used for checking the API endpoints. 

User Registration:
Method: POST

<img src="https://github.com/Moonchichiii/backend_postit_repository/blob/main/readmecontent/images/Postman-finaltest%20registration.png?raw=true" alt="registration" width="320">



User Login:
Method: POST

<img src="https://github.com/Moonchichiii/backend_postit_repository/blob/main/readmecontent/images/Postman-token.png?raw=true" alt="login" width="320">


### Pytest for Unit Testing

Pytest for unit testing.

<img src="coverage" alt="coverage" width="320">



[Back to top](#table-of-contents)
----------

## Deployment

### Key Settings and Preparations

Before deploying, check the following:

-   Environment Variables: Sensitive information and configuration settings are managed using decouple. Ensures sensitive variables are not exposed in the codebase.
-   Production Settings: Switch off any development settings, like DEBUG, for security and performance optimization.

### Deployment Process

The deployment involves the following steps:

1.  Local Development: After making changes locally, push the updated code to GitHub.
2.  GitHub to Heroku: Connect the GitHub repository to Heroku. This can be done via the Heroku dashboard.
3.  Deploy on Heroku: Used Herokus dashboard to deploy the application. Allows for viewing of logs and managing deployments.
4.  Monitoring: Post-deployment, Heroku logs are useful for monitoring and troubleshooting any issues not encountered during development.

[Back to top](#table-of-contents)
----------

## Credits & Tutorials




### README Management
- [https://stackedit.io](https://stackedit.io/)

[Back to top](#table-of-contents)
