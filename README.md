1)Install docker 


https://docs.docker.com/desktop/install/mac-install/

2) Start docker from desktop app or terminal 
3)Navigate to root directory (The one containing the Dockerfile)
4) Run 
-- docker build . -t cryptocons

5) Run
-- docker run -p 8001:8000 -it –rm cryptocons

6) Service should be up on your local ip probably 127.0.0.1:8001

// run the manage.py in the root folder 

// Theres another readme in the folder with the main methods 
