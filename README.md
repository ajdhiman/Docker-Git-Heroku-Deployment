# Docker-Git-Heroku-Deployment
This project demonstrate deployment of project on heroku and use of dockers.

Creating/Activating conda environment
```
conda create -p venv python==3.7 -y
```
conda init
```
conda activate venv/
```

Use Requirements.txt file

```
pip install -r requirements.txt
```

Git Commands
```
git add .
```
```
git commit -m "Adding files"
```
```
git push origin main
```


Build Docker Image

```
docker build -t docker-heroku-deployment:tag-first .
```

```
docker images
```

```
docker run -p 5000:5000 -e PORT=5000 02e7e313fca9
```

To check running container in docker
```
docker ps
```

To stop docker conatiner
```
docker stop <container_id>
```


To install requirements from Setup.py
```
python setup.py install
```
pip install -e.


Install ipykernel
```
pip install ipykernel
```
