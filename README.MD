# Python Selenium Framework for Automated Tests

#### Recommended python:
    3.6
#### Required pip packages:

    behave - gherkin
    selenium - browser automation
    pyhamcrest - more detailed assertions
    python-dotenv - parsing .env file

#### Running tests
If this is the first time when you want to run the tests make sure you create a .env file next to .env.dist and fill the variables by 
required data.

```
E2E_URL= add staging url
SCREEN_WIDTH=1350
SCREEN_HEIGHT=950

TEST_USER_EMAIL= add user email
TEST_USER_PASSWORD= add user password
```

To run tests use this command

    behave --no-capture --tags @staging features