YOUTUBE API

It is an API to fetch latest videos sorted in reverse chronological order of their publishing date-time from YouTube for a given tag/search query in a paginated response.
Server should call the YouTube API continuously in background (async) with some interval for fetching the latest videos for a given search query and should store the data of videos (specifically these fields - Video title, description, publishing datetime, thumbnails urls and any other fields you require) in a database with proper indexes.
A GET API which returns the stored video data in a paginated response sorted in descending order of published datetime.
It should be scalable and optimized.

STEPS TO FOLLOW:

How to use it : 
Download the repository or clone it with the below command

Open the terminal, paste the below code and hit "enter"

git clone https://github.com/Mahesh61437/youtubeapi.git

extraxt the file and navigate into collabmates
now activate the virtual environment by typing

source bin/activate and press enter

now install the required packages for the application with the below command

pip3 install -r requirements.txt 

navigate into youtubeapi folder , it will be like collabmates/youtubeapi

and then enter the below code

python 3 manage.py makemigartions
python3 manage.py migrate
python3 manage.py runserver

after running "python3 manage.py runserver" , ensure the django server is running
the terminal looks like 

System check identified no issues (0 silenced).
May 31, 2019 - 12:37:36
Django version 2.2.1, using settings 'youtubeapi.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

now open any browser and search for   http://127.0.0.1:8000/

enter the query you want and hit enter

the data will be displayed there

then you can navigate to the next page with ppage numbers below in that page