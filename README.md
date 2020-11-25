**Project based in API REST - PYTHON/DJANGO**

- API that can register and associated resellers and sales. It also has the functionality to bring cashback data from an external api.

---

# CASHBACK API REST 

The main functionalities of this API are:

1. Register a reseller. The reseller data input is its CPF (which can’t be repeated), name, email and password.
2. Register a new sale related to a reseller. The data inputs of each sale are code, value, date and reseller's CPF. For each new sale registered, if the reseller's CPF is 153.509.460-56, the sale status is registered as 'approved', otherwise it will be registered as 'awaiting_approval'.
3. Return all sales, showing their code, value, date, cashback percentage, cashback value and status.
4. Integration to return some companie's accumulated cashback from an external API.

Cashback criteria:

1. 10% cashback: $1000 => sale
2. 15% cashback: $1000 > sale > $1500
3. 20% cashback: sale => $1500

---

## JWT Authentication

This API uses JWT to authentication. It means that you have to use one JSON Web Token to call every endpoint. In order to do that, you'll have to follow this procedure:

1. Get access token from **_"/api/token/"_**:

```
{
  "email": "admin@email.com",
  "password": "cash1234"
}
```

2. Insert this token in the request's HEADER after 'Bearer ', like the example below:

```
Authorization: Bearer aaaaaaaaaaaaa.bbbbbbbbbbb.ccccccccccc
```

3. If your token expires, you'll have to use the refresh token from the first step into the **_"/api/token/refresh/"_** call:

```
{
  "refresh": "ddddddddddddd.eeeeeeeeeeeeeee.fffffffffffff"
}
```
_This call will return another access token, that you'll have to use in the second step._

---

## Swagger

This API uses Swagger as a documentation tool. In order to use JWT Authentication and Swagger UI, you have to follow the steps in previous section and use the Authorize button (in Swagger UI) to increment the requisition's header.

* In this project the root is redirecting to this swagger documentation endpoint. It can be accessed in http://localhost:8000/ 

---

## Endpoints

If you rather use Postman to test the endpoints, they are listed below:

1. **(POST)** **_"/api/token/"_** - *Authenticate sending email and password to get access token and refresh token (JWT).*
2. **(POST)** **_"/api/token/refresh/"_** - *Send refresh token to get another access token (JWT).*
3. **(GET)** **_"/resellers/"_** - *Returns all resellers registered.*
4. **(POST)** **_"/resellers/"_** - *Register new reseller.*
5. **(GET)** **_"/sales/"_** - *Returns all sales registered.*
6. **(GET)** **_"/sales/{code}/"_** - *Returns an specific sale.*
7. **(POST)** **_"/sales/"_** - *Register new sale sending code, value, date and reseller's cpf. The API will calculate the sale status, cashback percentage and cashback value.*
8. **(GET)** **_"/accumulated-cashback-integration/"_** - *Integration with an external API. It should return the accumulated cashback of the company.*

---

## Endpoints - EXTRA

Some filters were implemented in the: **(GET)** **_"/sales/"_** endpoint. 

Filter by attributes:

* reseller (reseller's CPF)
* status (options: [awaiting_approval,approved])
* cashback_percentage 

Filter by an specific date, or between dates :

_date format: 2020-01-01_

* date
* date_before
* date_after 

_If you would like, you can also use them in the **Swagger UI**._

---

## Utils

I've created 15 Makefile commands to use in this project. However, you'll just need to use 5 of them to run locally:

* **_make setup_**: To set up the entire environment to run the project. Only need to use this command once.
* **_make start_**: Create the project's container and run the project.
* **_make stop_**: Stop the project's container.
* **_make tests_**: Run all tests in the project.
* **_make clean_**: Clean this project's containers, image, volumes and network from your computer. It's recommended to read this Makefile command before you use it, to make sure that you do not have other projects with similar names.

---

## Django Admin

All API functionalities were also registered on the Django Admin.

_To make it easy to analyse this project... when the project runs for the first time, one super user is automatically created (email:admin@email.com, password:cash1234). You'll have to use this user to access this admin area. If you'ld like, you can create your own super user with the "make createsuperuser" command and delete the previous one in the Django admin._

_Django's admin can be accessed in:_ http://localhost:8000/admin/

---

## Run Locally


1. Make sure you have the Docker and Docker-compose installed.
2. You'll also need to generate one Django **SECRET KEY** and insert it in the **_develop.env_** file. I've already inserted a random secret key in the file, however is highly recommended to change it by a new one. (The key can be generated here: https://djecrety.ir/)
3. In the first time running the project (and just in the first one) you will have to use the command _make setup_ to create the project's image.
4. Then, use _make start_ to run it locally. Next time, you will just have to use _make start_ and _make stop_ commands.
5. This project runs in: http://localhost:8000/

---

## Tests

There are 15 tests being tested in this project. The characteristics of this tests can be readden below:

1. Three unit tests running in users app.
2. Three unit tests and two integration tests running in resellers app.
3. Three unit tests and four integration tests running in sales app.
4. There is a specific command to run the tests (**_make tests_**). However, the tests also runs when it's necessary to build the project's image. 

---

## Logs

There are 3 ways to analyse logs in this application:

1. **_make start_api_**.
2. **_make start_**, then **_make logs_**.
3. **_make start_api_** and **_make logs_** (in separated tabs).

---

## Requirements

* **DOCKER-COMPOSE**: 1.27.4
* **DOCKER**: 19.03.13

