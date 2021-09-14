# Predicting-MBTI-Personality-through-Text-Styles-WebPublic



## How to set on your local computer
### Prerequisites

* python == 3.8.x (tested on 3.8.10)
* node == v14.16.X (tested on v14.16.0)

1. clone this repository on your computer

     ### frontend
    1. Move to frontend folder
        ```bash
        cd frontend
        ```
    2. install npm modules
        ```
        npm install
        ```
    3. run dev server
        ```
        npm run serve
        ```
    ### backend
        1. Move to backend folder
            ```bash
            cd backend
            ```
        2-0 For Linux prepare some packages
            ```bash
            sudo apt upgrade
            sudo apt update
            sudo apt-get install build-essential
            sudo apt-get install python3-dev
            # you can get more specific dev version
            # for me) sudo apt-get install python3.8-dev
            ```
        2. Make python3 virtualenv folder and run it
            * make virtualenv
            ```bash
            python3 -m venv <your virtualenv name>
            #or
            #python -m venv <your virtualenv name>
            #python3 -m venv mbti
            ```
            * activate
            ``` bash
            # Windows
            $.\mbti\Scripts\activate
            # Linux or MacOS
            $ source mbti/bin/activate
            ```
        3. Install the moduels in requirements.txt
            ```bash
            pip install -r ./requirements.txt
            ```
        4. Activate fastapi server
            ```bash
            cd app
            #dev
            uvicorn main:app --host=0.0.0.0 --port=8000 &
            #see http://your-ip(127.0.0.1):8000
            #Swagger UI is on the http://your-ip(127.0.0.1):8000/docs
            #READ and get the api http://your-ip(127.0.0.1):8000/<api>
            #deployment<TODO>
            #see https://www.uvicorn.org/deployment/
            #use gunicorn
            ```


## demo

## Screenshot

## further more

## Notice
