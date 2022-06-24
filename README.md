# B-YEP-500-LYN-5-1-area ![Build](https://github.com/EpitechIT2020/B-YEP-500-LYN-5-1-area-enzo.doguereau/workflows/Build/badge.svg)

## Front - Web app
```Show ReadMe on front directory```

## Mobile app
### Init project
- Install dependencies:
    ```npm install```
### Build and start dev serve
- You need to install expo application for android or ios
- Install expo cli with npm:
    ```npm install -g expo-cli```
- Start dev serve:
    ```expo start```
- Scann QrCode on web page with expo application

## Back app
### Init project
- Install virtualenv and start envirronement:
    ```virtualenv .env ; source .env/bin/activate```
- Install dependencies:
    ```pip install -r back/requirement.txt```
- Make migration for db create:
    ```cd back ; ./manage.py migrate```
### Build and start project
```./manage.py runserver``` (default localhost:8000)
