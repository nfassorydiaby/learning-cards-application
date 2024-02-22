# learning-cards-application

# create virtuel envireonement 
python3 -m venv env

# activate you environement 
source env/bin/activate

# install dependency 
pip install -r requirements.txt

# lunsh back end app 

uvicorn main:app --port 8000 --reload

# to lunsh test we can do 
docker exec -it learning-cards-application-app-1 pytest -s test_app.py
