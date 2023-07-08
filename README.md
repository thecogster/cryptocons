1)Install docker 


https://docs.docker.com/desktop/install/mac-install/

2) Start docker from desktop app or terminal 
3)Navigate to root directory (The one containing the Dockerfile)
///// ATTENTION MCGINT 
//// 
4) Run: docker-compose up --build -d
///// ATTENTION MCGINT 
//// 

// run the manage.py in the root folder 

// Theres another readme in the folder with the main methods


## For Deployment 

## 5) Run this command: docker-compose run --rm app sh -c "python manage.py collectstatic"
## So by running the collect static it calls the working_dir in settings.py to find the static for the given app. It then copies this to the static_root specified in settings.py. This is then put inside the docker container at root under /static.

## 6) This command deploys the app to google app engine inside the project_id 'project midyear-system-298910': docker-compose -f docker-compose-deploy.yml run --rm gcloud sh -c "gcloud app deploy --project midyear-system-298910"






