## Installation

1. Install requirements and create virtual environment:
    pipenv install
    pipenv shell
2. Create and fill out the local settings `.env` file placed at root directory, obligatory environment variables:
    - django secret key `SECRET_KEY`
    - debug setting `DEBUG`
    - list of allowed hosts `ALLOWED_HOSTS`
    - database url `DATABASE_URL`
    - ip stack user access key `IPSTACK_ACCESS_KEY`
    
3. Run database migrations using `./manage.py migrate`
4. Run tests to make sure that everything is ok `./manage.py test`
5. Run server using `./manage.py runserver`

## App description and usage
### Description

This is API to check and store geolocation based on IP or url.

### Authorization - authorization for users is done via JWT which uses access token (short-lived token)
and refresh token (long-lived token). Using provided user credentials (`'username` and `password`)
request has to be made at `/token/` endpoint. In response, we get `access` token and `refresh` token.
Access token is necessary to gain access to geolocation endpoint.
Refresh token is necessary to obtain new access token when current one is expired. To obtain new access token request
`/token/refresh/` using `refresh` parameter as key and our refresh token as value. Response returns new access token.
If refresh token is expired as well the process needs to be repeated.
### Endpoints - requests can be made to list all stored in database records of IP geolocations, add new ones, delete or retrieve
specific ones (based on id of an object).
   1. LIST - endpoint: `/geolocations/`, http method: GET, functionality: provides list of all stored geolocations of IP addresses
   2. RETRIEVE - endpoint: `/geolocations/<int:id>`, http method: GET, functionality:
   3. ADD - endpoint: `/geolocations/`, http method: POST, parameter: key `ip` value is address we want to check,  functionality: 
   if provided with proper IP address, checks using ip stack API service geolocation of an IP address and store selected information in database
   4. DESTROY - endpoint: `/geolocations/<int:id>`, http method: DELETE, functionality: deletes selected IP geolocation object