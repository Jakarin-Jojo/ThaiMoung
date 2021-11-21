# ThaiMoung ![ThaiMoungLOGO](Logo/LOGO-thaimoung_2.png)
[![Build Status](https://app.travis-ci.com/Jakarin-Jojo/ThaiMoung.svg?branch=master)](https://app.travis-ci.com/Jakarin-Jojo/ThaiMoung)
[![codecov](https://codecov.io/gh/Jakarin-Jojo/ThaiMoung/branch/master/graph/badge.svg?token=TVQ33DAQ9M)](https://codecov.io/gh/Jakarin-Jojo/ThaiMoung)  
ThaiMoung is a web forum application that provides services to create forums for dramas in Thailand.

## Getting Started

|    Name    | Required version(s) |
| :--------: | :-----------------: |
|   Python   |   3.8 or higher     |
|   Django   |   3.2.7 or higher   |

1. Clone this repository to your computer.
    ```
    git clone https://github.com/Jakarin-Jojo/ThaiMoung.git
    ```
2. Change directory to the repository.
    ```
    cd ThaiMoung
    ```
3. Install virtualenv to your computer.
    ```
    pip install virtualenv
    ```
4. Create virtual environment.
     ```
    python -m venv venv
    ```
5. Activate virtualenv by using this command.

    for Mac OS / Linux
    ```
    source venv/bin/activate
    ```
    for Windows
    ```
    venv\Scripts\activate
6. Install all require packages by this command.
    ``` 
    pip install -r requirements.txt
    ```
7. Create .env file inside mysite (same level as settings.py) and change the debug=True.
    ```
    SECRET_KEY=YOUR_SECRET_KEY
    DEBUG=True
    SOCIAL_AUTH_FACEBOOK_KEY=YOUR_SOCIAL_AUTH_FACEBOOK_KEY
    SOCIAL_AUTH_FACEBOOK_SECRET=YOUR_SOCIAL_AUTH_FACEBOOK_SECRET

    SOCIAL_AUTH_GITHUB_KEY=YOUR_SOCIAL_SOCIAL_AUTH_GITHUB_KEY
    SOCIAL_AUTH_GITHUB_SECRET=YOUR_SOCIAL_AUTH_GITHUB_SECRET

    SOCIAL_AUTH_GOOGLE_OAUTH2_KEY=YOUR_SOCIAL_AUTH_GOOGLE_OAUTH2_KEY
    SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET=YOUR_SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET

    EMAIL_HOST_USER=YOUR_EMAIL_HOST_USER
    EMAIL_HOST_PASSWORD=YOUR_EMAIL_HOST_PASSWORD

    CLOUDINARY_URL=YOUR_CLOUDINARY_URL
    ```
8. Run this command to migrate the database.
    ```
    python manage.py migrate
    ```
9. Start running the server by this command.
    ```
    python manage.py runserver
    ```



## Project Documents

[Home](../../wiki/Home)  
[Proposal](https://docs.google.com/document/d/1rzrv2o_gZU1Uh3EQ-Ona6EIYkrj8onRlVrpoh9FInAI/edit#)  
[Vision Statement](../../wiki/Vision%20Statement)  
[Requirements](../../wiki/Requirements)   

### Code review
* [Script](../../wiki/Script)  
* [Checklist](../../wiki/Checklist)  

## Iteration

### Iteration Plans  
* [Iteration 1 Plan](../../wiki/Iteration%201%20Plan)  
* [Iteration 2 Plan](../../wiki/Iteration%202%20Plan)  
* [Iteration 3 Plan](../../wiki/Iteration%203%20Plan)
* [Iteration 4 Plan](../../wiki/Iteration%204%20Plan) 
* [Iteration 5 Plan](../../wiki/Iteration%205%20Plan)
* [Iteration 6 Plan](../../wiki/Iteration%206%20Plan)

### Iteration TaskBoards  
* [Iteration 1 TaskBoard](../../projects/2)  
* [Iteration 2 TaskBoard](../../projects/3)  
* [Iteration 3 TaskBoard](../../projects/5)  
* [Iteration 4 TaskBoard](../../projects/6)
* [Iteration 5 TaskBoard](../../projects/7)
* [Iteration 6 TaskBoard](../../projects/8)
## License
[MIT License](https://github.com/Jakarin-Jojo/ThaiMoung/blob/master/LICENSE)
