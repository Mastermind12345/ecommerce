# CRUD API WITH DJANGO REST FRAMEWORK
[Django REST framework](http://www.django-rest-framework.org/) is a powerful and flexible toolkit for building Web APIs.

## Installation
After you cloned the repository, you want to create a virtual environment, so you have a clean python installation.
You can do this by running the command:-
```
python -m venv env
```

After this, it is necessary to activate the virtual environment, you can get more information about this [here](https://docs.python.org/3/tutorial/venv.html)

You can install all the required dependencies by running:-
```
pip install -r requirements.txt
```
After this we have to populate our models by running migrations command:-
```
python manage.py migrate
```
Finally, We can run our  Django server by running:-
```
python manage.py migrate
```

## Fixture 
We have a fixture in our api app for our base data and can populate by running command:-
```
python manage.py loaddata data.json
```

## Serializing the Product model
You will need serializers to convert model instances to JSON so that the frontend can work with the received data.

Create a api/serializers.py file with your code editor. Open the serializers.py file and update it with the following lines of code:
```
from rest_framework import serializers
from .models import Products

class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Products
        fields = '__all__'
```

## Creating the View
In the api/views.py file, we are going to write the logic for the CRUD functionality for our app. Django Rest framework comes with inbuilt classes that make building the CRUD functionality very easy.

```
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from .serializers import ProductSerializer
from .models import Products

class ProductViewSet(viewsets.ModelViewSet):
    serializer_class = ProductSerializer
    queryset = Products.objects.all().order_by('id')
    permission_classes = [IsAuthenticated]
    authentication_classes = [TokenAuthentication]   # Authentication By Token
```

## Structure
In a RESTful API, endpoints (URLs) define the structure of the API and how end users access data from our application using the HTTP methods - GET, POST, PUT, DELETE. Endpoints should be logically organized around _collections_ and _elements_, both of which are resources.

In our case, we have one single model, `Products`, so we will use the following URLS - `/products/` and `/products/<id>` for collections and elements, respectively:

Endpoint |HTTP Method | CRUD Method | Result
-- | -- |-- |--
`products/` | GET | READ | Get all products
`products/:id` | GET | READ | Get a single product
`products/`| POST | CREATE | Create a new product
`products/:id` | PUT | UPDATE | Update a product
`products/:id` | DELETE | DELETE | Delete a product

 Also For the product list api we have pagination
 ```
 REST_FRAMEWORK = {
    'DEFAULT_PAGINATION_CLASS': 'rest_framework.pagination.PageNumberPagination',
    'PAGE_SIZE': 6,
}
 ```

## Documenting our endpoints
We will use coreapi to document our endpoints, install coreapi in our environment:-

``` pip install coreapi ```

Add this to installed apps in ecommerce/settings.py

Also add the rest framework configuration to enable documentation autogeneration in ecommerce/settings.py:
```
REST_FRAMEWORK = {
    .....
    'DEFAULT_SCHEMA_CLASS': 'rest_framework.schemas.coreapi.AutoSchema'
}
```
Open the api/urls.py file and add docs URL:
```
urlpatterns = [
    .....
    path('docs/', include_docs_urls(title='CRUD API')),
]
```

By navigating to http://localhost:8000/api/documentation/ in the browser we’ll be able to see the full documentation of our CRUD API endpoint:-

![api](https://user-images.githubusercontent.com/86952339/221319127-d10e31f3-671a-4416-a693-7d047d5c9a63.png)


## Docker
We have Dockerfile and docker-compose.yml as our project is dockerize

To Run project through docker run command:-
```
docker-compose up -d
```
