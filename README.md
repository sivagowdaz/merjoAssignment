# Blog API Documentation

## Setup

### Clone the repository and install all the dependancies listed in `requirements.txt`
```
pip install -r requirements.txt
```

### Perform database migrations
```
python manage.py makemigrations
python manage.py migrate
```
### Run development server
```
python manage.py runserver
```

### Creating the super user to access django admin
```
python manage.py createsuperuser
```

## API Documentation
### Creating or registering user
Send post request to `http://127.0.0.1:8000/api/users/register/` with json data
```
{
    "username":"karun",
    "email":"karun@gmail.com",
    "password":"password"
}
```
### Getting jwt token
To get jwt token send a POST request to `http://127.0.0.1:8000/api/users/authenticate/` with login credentials as json data.
```
{
    "username":"karun",
    "password":"password"
}
```
### List all blogs
To list all blogs, send GET request to `http://127.0.0.1:8000/api/blogs`. Response would look like
```
{
    "message": [
        {
            "id": 2,
            "title": "Test2",
            "content": "test",
            "created_at": "2023-08-21T15:50:30.891199Z",
            "updated_at": "2023-08-21T14:52:49.950486Z",
            "auther": 2,
            "comments": []
        },
        {
            "id": 3,
            "title": "test content",
            "content": "test content",
            "created_at": "2023-08-21T15:25:10.050163Z",
            "updated_at": "2023-08-21T15:25:10.050163Z",
            "auther": 1,
            "comments": []
        },
        {
            "id": 4,
            "title": "test content2",
            "content": "test content2",
            "created_at": "2023-08-21T18:27:45.191349Z",
            "updated_at": "2023-08-21T15:31:04.272362Z",
            "auther": 1,
            "comments": [
                4,
                5
            ]
        }
    ]
}
```
### Creating blog
This is a protected route. To create a blog user should be registered. POST request to `http://127.0.0.1:8000/api/blogs/` should include jwt token in headers as `Authorization <jwt token>`. Request body would look like 
```
{
    "title":"new blog",
    "content":"content of new blog"
}
```
### Updating a blog
A blog can only be updated by its author. To update a blog send a PUT request to `http://127.0.0.1:8000/api/blogs/<blog_id>/` with jwt token at the header. Request body would look like
```
{
    "title":"new title",
    "content":"new content"
}
``` 
NOTE : Replace `<blog_id>` with valid blog id

### Deleting a blog
A blog can only be deleted by its author. To delete a blog send a DELETE request to `http://127.0.0.1:8000/api/blogs/<blog_id>/` with jwt token at the header.

NOTE : Replace `<blog_id>`` with valid blog id


### List all comments of a particular blog.
To list all blogs, send GET request to `http://127.0.0.1:8000/api/comments/<blog_id>`.  `<blog_id>` is the id of the blog for which you want to list the comments. Response would look like
```
{
    "message": [
        {
            "id": 4,
            "content": "new content new content",
            "created_at": "2023-08-21T18:24:49.375267Z",
            "updated_at": "2023-08-21T18:23:12.810339Z",
            "auther": 1
        },
        {
            "id": 5,
            "content": "new content new new jdfjdfj dfjdkjfcontent",
            "created_at": "2023-08-21T18:28:42.408071Z",
            "updated_at": "2023-08-21T18:27:45.176316Z",
            "auther": 3
        }
    ]
}
```
### Creating a  comment
This is a protected route. To create a comment, user should be registered. POST request to `http://127.0.0.1:8000/api/comments/` should include jwt token in headers as `Authorization <jwt token>`. Request body would look like 
```
{
    "content":"blog is very informative.",
    "blog_id": 4
}
```
### Updating a comment
A blog can only be updated by its author. To update a blog send a PUT request to `http://127.0.0.1:8000/api/comments/<comment_id>/` with jwt token at the header. Request body would look like
```
{
    "content":"This blog is life saver for me!!"
}
``` 
NOTE : Replace `<comment_id>` with valid comment id

### Deleting a comment
A comment can only be deleted by its author. To delete a blog send a DELETE request to `http://127.0.0.1:8000/api/comments/<comment_id>/` with jwt token at the header.

NOTE : Replace `<commet_id>` with valid comment id