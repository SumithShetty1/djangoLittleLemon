Hello Reviewers,

You can run available unittests from VS terminal using command: python manage.py test

Django Admin
Superuser:
    Username: Admin  
    Password: admin123

You can use the following API paths for testing purposes using Insomnia or Postman clients
OR just browse using your favorite browser.

Djoser endpoint, for example, to make POST request and create new user
/auth/users/ 

To login and auth get token
/api-token-auth/ 

To login using djoser endpoint
/auth/token/login 

# menu items
/menu/
/menu/{menuItemId}

# table booking 
/booking/tables/
/booking/tables/{bookingId}