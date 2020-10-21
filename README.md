# Blog App Server (Django REST)

This application is built on django-rest framework. It implements a REST API using which a user can create,update, delete, list **Blogs**. It implements a simple _CRUD_ (Create, Read, Update, Delete) API with a local database.

**Note**: This application also has a fronend made in React and Redux available at [Blog Application Fronend](https://github.com/ahmadx16/blog_app_react/tree/blog-app-react)

## Instructions

Following are the instructions that you need perform in order to run the application

1. [Clone the repository](#cloning-the-repository)
1. [Python Environment Setup](#python-environment-setup)
1. [Launching the Application](#launching-the-application)
1. [Calling the APIs](#calling-the-apis)

## Cloning the Repository

Clone this repository and switch to the `blog_server` branch as it currently contains the latest code. Run the following commands on your shell

```shell
git clone https://github.com/ahmadx16/blog_app_server.git
cd blog_app_server/
git checkout blog_server
```

The above commands will download the repository and switch the branch.

## Python Environment Setup

It is recommended to create a virtual environment before installing django. This project uses [virtualenv](https://pypi.org/project/virtualenv/) for this purpose. You can create a python virtual environment by giving path where you want to create a virtual environment and run following commands.

```shell
python3 -m venv /path-to-new-virtual-environment
source /path-to-new-virtual-environment/bin/activate
```

The above commands will create and activate a new virtual environment. Learn more about virtual environment virtualenv [here](https://pypi.org/project/virtualenv/).

Now install application requirements using following command.

```shell
pip install -r requirements.txt
```

## Launching the Application

Before launching the application run the following command on terminal.

```shell
cd blog_app_server
python manage.py migrate
```

This command will create the database tables that we have specified in the models of our application.

Now run command.

```shell
python manage.py runserver
```

This command will start the backend server at 127.0.0.1:8000

## Calling the APIs

Following are the APIs that user can call when the server is started.

### Add Blog:

Adds a new blog.

```
POST /blogs/
```

The request needs to have JSON data in following format:

```JSON
{
    "title":"title",
    "blog_markdown":"Content in markdown syntax"
}
```

**Example:**

Lets call following API to provide an example.

```shell
POST http://localhost:8000/blogs/
```

with following data.

```JSON
{
    "title":"title",
    "blog_markdown":"Content in markdown syntax"
}
```

It will return a added blog's data in following format.

```JSON
{
    "id": 1,
    "title":"title",
    "blog_markdown":"Content in markdown syntax",
    "created": "2020-10-21T13:57:34.189084Z",
    "modified": "2020-10-21T13:57:34.189119Z"
}
```

### List All Blogs:

Returns array containing all blogs.

```
GET /blogs/
```

**Example:**

Lets call following API to provide an example.

```shell
GET http://localhost:8000/blogs/
```

It will return a added blog's data in following format.

```JSON
[
    {
        "id": 1,
        "title":"title",
        "blog_markdown":"Content in markdown syntax",
        "created": "2020-10-21T13:57:34.189084Z",
        "modified": "2020-10-21T13:57:34.189119Z"
    }
]
```

### Retrieve Blog:

Returns a specific blog.

```
GET /blogs/:blog_id/
```

**Example:**

Lets call following API to provide an example.

```shell
GET http://localhost:8000/blogs/1/
```

It will return a added blog's data in following format.

```JSON
{
    "id": 1,
    "title":"title",
    "blog_markdown":"Content in markdown syntax",
    "created": "2020-10-21T13:57:34.189084Z",
    "modified": "2020-10-21T13:57:34.189119Z"
}
```

### Delete Blog:

Deletes a specific blog.

```
DELETE /blogs/:blog_id/
```

**Example:**

Lets call following API to provide an example.

```shell
DELETE http://localhost:8000/blogs/1/
```

It will return response status `204 No Content` after deleting the blog from database

### Update Blog:

Updates a blog.

```
PATCH /blogs/:blog_id/
```

The request needs to have JSON data in following format:

```JSON
{
    "title":"title",
    "blog_markdown":"Content in markdown syntax"
}
```

Since it is a `PATCH` request it can have any of the keys to update that specific key.

**Example:**

Lets call following API to provide an example.

```shell
PATCH http://localhost:8000/blogs/1/
```

with following data.

```JSON
{
    "title":"title(updated)",
    "blog_markdown":"Content in markdown syntax"
}
```

It will return a added blog's data in following format.

```JSON
{
    "id": 1,
    "title":"title(updated)",
    "blog_markdown":"Content in markdown syntax",
    "created": "2020-10-21T13:57:34.189084Z",
    "modified": "2020-10-21T13:57:34.189119Z"
}
```
