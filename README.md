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
