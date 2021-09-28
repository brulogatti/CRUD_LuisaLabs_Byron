# README Byron Store!
This is a CRUD project in Python. It was developed as a final challenge for the Google Cloud Platform Boot Camp offered by Magazine Luiza and Gama Academy. Here you'll find your working environment settings instructions and how to navigate in our website.

## Table of Content - [Byron Store!](#welcome-to-byron-store)
- [README Byron Store!](#readme-byron-store)
	- [Table of Content - Byron Store!](#table-of-content---byron-store)
- [How to run the project](#how-to-run-the-project)
	- [1. Commands](#1-commands)
	- [2. Coding](#2-coding)
		- [2.1. Starting up](#21-starting-up)
		- [2.2. Models and migrations](#22-models-and-migrations)
		- [2.3. Docker image](#23-docker-image)
		- [2.4. Kubernetes](#24-kubernetes)
- [Our Team](#our-team)


# How to run the project
## 1. Commands
When you create your VM in the project, you use the command 
```
-m venv project_name
```

Every time you open the project after restarting the computer, you should go to project folder and reactivate you VM using the following commands:

**Windows**
```
project_name\Scripts\activate    
project_name\Scripts\activate.bat
```

**Unix or MacOS**
```
source tutorial-env/bin/activate
```

**Django in the VM enviroment**
First install Django with the following command:
```
python -m pip install Django
```

Then start it in project folder without creating a separated folder using the following
```
django-admin startproject project .
```

Finaly, run the app file 
```
python manage.py startapp app
```

- **Obs:** This app file should be created in a folder named settings.py, so Python recognize it as a part of our project.

**Git and GitHub**
Now, you should push the project to your repo in GitHub using the following commands:
```
git remote add origin <repository_link>
git branch -M main
git add .
git commit -m 'message'
git push -u origin main
```

## 2. Coding
### 2.1. Starting up
Run the server in your VM terminal
```
python3 manage.py runserver
```

Create a **Template** folder inside the **app** folder. Now, inside the **Template** folder create your index.html and paste Bootstrap's CDN in it.
Modify views.py file to connect the index.html file.

### 2.2. Models and migrations
We followed this [link](https://docs.djangoproject.com/en/3.2/topics/db/models/#field-types) to work in an existing Django model, the we run the migrations with
```
python manage.py makemigrations
```

Following, we create DB tables and run
```
python manage.py migrate
```
This will start the SQLite automatically, which we now work with in the settings folder to see the ENGINE attribute. Next open the DB browser and put db.sqlite3 file in it to connect with our app database.

Next, go to this [link](https://docs.djangoproject.com/en/3.2/topics/forms/modelforms/) and import the model in the views.
Inside the views redirect we insert route name.


### 2.3. Docker image
If you don't create a tag for the image like **user_docker_hub/image_name**, you may have some problems. To avoid it when doing the build create the image with that name pattern.
```
docker build -t django-kube .
docker tag django-kube user_docker_hub/django-kube:django-kube
```

Now we run it
```
docker run django-kube
```


### 2.4. Kubernetes
Create a file **deployment.yaml** :
```
apiVersion: v1 
kind: Service 
metadata: 
	name: django-test-service 
spec: 
	selector: 
		app: python-crud 
	ports: 
		- protocol: "TCP" 
		port: 6000 
		targetPort: 5000 
	type: LoadBalancer

--- 

apiVersion: apps/v1 
kind: Deployment 
metadata: 
	name: python-crud 
spec: 
	selector: 
		matchLabels: 
			app: python-crud 
	replicas: 3 
	template: 
		metadata: 
			labels: 
				app: python-crud 
		spec: 
			containers: 
				- name: python-crud 
				image: user_docker_hub/image_name 
				imagePullPolicy: IfNotPresent 
				ports: 
					- containerPort: 5000
```

Then run Kubernetes through minikube
```
minikube start
```

Read the file with:
```
kubectl apply -f deployment.yaml
```

Give the project image to minikube
```
docker save django-kube | (eval $(minikube docker-env) && docker load)
```

And finish calling the dashboard to open Kubernetes
```
minikube dashboard
```

# Our Team
- Tania Eliza Oliveira - [GitHub](https://github.com/elizaoliveira88)
- Milena Maria Costa Pininga - [GitHub](https://github.com/mmcpininga)
- Maria Fernanda Soares - [GitHub](https://github.com/mafesoares)
- Bruna Logatti - [GitHub](https://github.com/brulogatti)
- Beatriz Abne Alqueres Cruz - [GitHub](https://github.com/Abne-b)
