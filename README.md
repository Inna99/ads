# DRF-TDD-Example
### An example Django REST framework project for test driven development.

### Test Case Scenarios
* Test to verify registration with invalid password.
* Test to verify registration with already exists username.
* Test to verify registration with valid datas.
* Tested API authentication endpoint validations.
* Tested authenticated user authorization.
* Create a ad with API.
* Update a ad with API.
* Update a ad with API.
* Delete a ad with API.
* Get ad list for a user.

### API Endpoints
### Users
    /api/users/ (User registration endpoint)
    /api/users/login/ (User login endpoint)
    /api/users/logout/ (User logout endpoint)

### Ads
    /api/ads/ (Ad create and list endpoint)
    /api/ads/{todo-id}/ (Ad retrieve, update and destroy endpoint)

### Install
    pip install -r requirements.txt

### Usage
    python manage.py test