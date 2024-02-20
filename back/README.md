# learning-cards-application

# create virtuel envireonement 
python3 -m venv env

# activate you environement 
source env/bin/activate

# install dependency 
pip install -r requirements.txt

# lunsh back end app 

uvicorn main:app --port 80001 --reload

