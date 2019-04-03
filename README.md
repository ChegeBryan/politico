[![GitHub
license](https://img.shields.io/github/license/ChegeBryan/politico.svg)](https://github.com/ChegeBryan/politico/blob/master/LICENSE)
![](https://img.shields.io/website-up-down-green-red/https/chegebryan.github.io/politico/UI/.svg?colorB=blue&style=flat)
![](https://img.shields.io/github/languages/count/ChegeBryan/politico.svg?style=flat)
![](https://img.shields.io/github/languages/top/ChegeBryan/politico.svg?colorB=blue&style=flat)
![](https://img.shields.io/github/repo-size/ChegeBryan/politico.svg?style=flat)
![](https://img.shields.io/badge/Andela%20Cohort-NB0--37-blue.svg)<br>
[![Build
Status](https://travis-ci.org/ChegeBryan/politico.svg?branch=develop)](https://travis-ci.org/ChegeBryan/politico)
[![Coverage
Status](https://coveralls.io/repos/github/ChegeBryan/politico/badge.svg?branch=develop)](https://coveralls.io/github/ChegeBryan/politico?branch=develop)
[![Codacy Badge](https://api.codacy.com/project/badge/Grade/1eeb18d72ffe4309812fd2ee5f9d0437)](https://www.codacy.com/app/ChegeBryan/politico?utm_source=github.com&amp;utm_medium=referral&amp;utm_content=ChegeBryan/politico&amp;utm_campaign=Badge_Grade)
[![Maintainability](https://api.codeclimate.com/v1/badges/3315f3314f723a7c6136/maintainability)](https://codeclimate.com/github/ChegeBryan/politico/maintainability)
<br><br>

# Politico
<p align=center>
<br>
<img src="./screenshot.png">
<a href="https://chegebryan.github.io/politico/UI">View UI</a> Hosted with ❤️ at Github pages
</br>

</p>

### Project Description
Politico enables citizens give their mandate to politicians running for
different government offices while building trust in the process through
transparency.

### Features
1. Users can sign up.
2. Users can login.
3. Admin (electoral body) can create political parties.
4. Admin (electoral body) can delete a political party.
5. Admin (electoral body) can create different political offices .
6. Users can vote for only one politician per political office .
7. Users can see the results of election.

### Bonus features
1. User can reset password.
2. A politician can create a petition against a concluded political office
   election.


## Getting started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

## Prerequisites

- python 3.6
- pip3
- Postgres database

If you wish to clone the repo please satisfy the requirements in the requirements.txt

## Installing
```
clone the repo to local machine

git clone https://github.com/ChegeBryan/politico.git

pip3 install virtualenv

```
### Create a virtual environment and install requirements
- Navigate to the cloned repo directory and open terminal from there.
- run `virtualenv venv` to create virtual environment with the name `venv`
- activate the virtualenv by `source venv/bin/activate`
- `pip3 install -r requirements.txt` to install app requirements on your virtual environment

### Starting the server (development enviroment)
while still at the terminal:
- set enviroment variables from your platform specific dotenv file `source {your dotenv}`
- set APP_SETTING variable `export APP_SETTING=development`
- Start the app by running `python run`

### Running the tests
To run the application unit_tests
- run `pytest` at the app root directory
- run with coverage `pytest --cov=app/api app/tests`

### Api endpoints (Persistent)
This are the currently available v2 endpoints. The data is written into a database.

- #### Open endpoints

| HTTP Method   | URL Endpoint  | Description  |
| -------- | ----------------------------------- | ---------------- |
| `POST`   | `/api/v2/auth/signup`               | Create new user |
| `POST`   | `/api/v2/auth/signin`               | Sign in existing user |
| `POST`   | `/api/v2/auth/signout`              | Sign out logged in user |

- #### Open to Admin only endpoints

| HTTP Method   | URL Endpoint  | Description  |
| -------- | -------------------- | ---------------- |
| `POST`   | `/api/v2/parties`                     | Create a new party |
| `POST`   | `/api/v2/offices`                     | Create a new office |
| `PATCH`  | `/api/v2/parties/<int:party_id>/name` | Update a party name |
| `DELETE` | `/api/v2/parties/<int:party_id>`      | Delete a party |
| `POST`   | `/api/v2/office/<int:_id>/register`   | Register office candidate |


- #### Open to logged in user

| HTTP Method   | URL Endpoint  | Description  |
| -------- | ----------------------------------- | ---------------- |
| `GET`    | `/api/v2/offices`                    | Fetch offices records |
| `GET`    | `/api/v2/offices/<int:office_id>`    | Fetch a specific office |
| `GET`    | `/api/v2/parties`                    | Fetch all parties created |
| `GET`    | `/api/v2/parties/<int:party_id>`    | Fetch specific party |
| `GET`    | `/api/v2/parties/<int:party_id>`    | Fetch specific party |
| `GET`    | `/api/v2/office/<int:office_id>/result` | Fetch office results |
| `POST`   | `/api/v2/votes`                        | Cast a vote |
| `POST`   | `/api/v2/petitions`                    | Create a petition |


### API hosting
[![](https://img.shields.io/badge/Heroku-v2-blue.svg)](https://politico-v2-heroku.herokuapp.com)

### API Documentation
[![](https://img.shields.io/badge/Apiary-Documentation-yellowgreen.svg)](https://politico5.docs.apiary.io/#)

### Powered by

<a href="http://flask.pocoo.org/"><img
   src="http://flask.pocoo.org/static/badges/flask-powered.png"
   border="0"
   alt="Flask powered"
   title="Flask powered"></a>

### Contributing
![](https://img.shields.io/badge/PR%27s-Welcome-blue.svg)<br>Contributions will be highly appreciated. Make a pull request and lets build
software together.

### Changelog
see [Changelog](./CHANGELOG.md)

### Authors
[Chege Bryan](https://github.com/ChegeBryan)

