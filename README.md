# README Byron Store!
This is a CRUD project in Python. It was developed as a final challenge for the Google Cloud Platform Boot Camp offered by Magazine Luiza and Gama Academy. Here you'll find your working environment settings instructions and how to navigate in our website.

## Table of Content - [Byron Store!](#welcome-to-byron-store)
- [README Byron Store!](#readme-byron-store)
	- [Table of Content - Byron Store!](#table-of-content---byron-store)
- [Developer Tools](#developer-tools)
		- [Python](#python)
			- [pip](#pip)
			- [.yaml](#yaml)
	- [DataBase Settings](#database-settings)
		- [DB Modeling](#db-modeling)
	- [Frameworks](#frameworks)
		- [Django](#django)
		- [Bootstrap](#bootstrap)
	- [Containerization Tools](#containerization-tools)
		- [Docker](#docker)
		- [MiniKube](#minikube)
- [How to run the project](#how-to-run-the-project)
		- [1. Commands](#1-commands)
		- [2. Coding](#2-coding)
			- [2.1. Starting up](#21-starting-up)
			- [2.2. Models and migrations](#22-models-and-migrations)
			- [2.3. Docker image](#23-docker-image)
			- [2.4. Kubernetes](#24-kubernetes)
- [How to use](#how-to-use)
	- [Home Page](#home-page)
				- [You can always navigate back and forth from the sections in our site trought the main buttons.](#you-can-always-navigate-back-and-forth-from-the-sections-in-our-site-trought-the-main-buttons)
	- [Product](#product)
		- [Products Button](#products-button)
		- [Product Registration button](#product-registration-button)
	- [Company](#company)
		- [Companies button](#companies-button)
		- [Company Registration button](#company-registration-button)
- [Our Team](#our-team)



# Developer Tools

### Python 
First you'll need to install **PyCharm** as your working IDE. Then, make sure to have **Pyhton** installed too. You can look in the following links to download and install:
- [PyCharme](https://www.jetbrains.com/pycharm/download/), you're looking for Community version.
- [Pyhton](https://www.python.org/downloads/), you'll want the version compatible with you Operational System

#### pip
For this project we'll need pip as our **package-management system**, and sometimes it may not be installed automatically when you download Pyhton. To make sure it's installed follow this [link](https://pip.pypa.io/en/stable/installation/).

#### .yaml
Now we'll install yaml as an **environment marker support**. Click [here](https://yaml.readthedocs.io/en/latest/install.html) to see how to install.

## DataBase Settings
For this project, we used **SQLite**, since it's already integrated with Python. You can look up for the **Precompiled Binaries** in the following [link](https://www.sqlite.org/download.html). Be sure to download and install the version compatible with you Operational System.

### DB Modeling
If you want to draw a model for you DB, we suggest [Diagrams](https://app.diagrams.net/), as it's a free online diagram software.

## Frameworks
Now that we set up our working enviroment and database tool, it's time to set up our framework. Frameworks are structures intended to serve as a support or guide developing our project. In our project we used Django and Bootstrap.

**Note: Frameworks are project specific, therefore you should remember to install it in your project folder. You can use the terminal in PyCharm to do it.**

### Django
Django is a high-level Python web framework that enables rapid development of secure and maintainable websites. You'll find all the instructions to set it up [here](https://docs.djangoproject.com/en/3.2/intro/install/). 

### Bootstrap
[Here](https://getbootstrap.com/) you'll find Bootstrap's official site, you can use it to build responsive, mobile-first sites. 
- You can click in the **[Download](https://getbootstrap.com/docs/5.1/getting-started/download/)** button and install it in your project folder; 
- or you can click in the **[Get started](https://getbootstrap.com/docs/5.1/getting-started/introduction/)** button to see the CSS stylesheet link and add it into your HTML

## Containerization Tools
### Docker
You can install Docker following the instructions from the following link:
[Docker Engine](https://docs.docker.com/get-docker/)

If you use Linux systems you'll probably need to install [Docker Compose](https://docs.docker.com/compose/install/) manually. In Mac and Windows versions of Docker, Compose is already included.

### MiniKube
For this project we used **Minikube** as a local Kubernetes for **Docker**, althought it can also be used in VM enviroment. Follow the [link](https://minikube.sigs.k8s.io/docs/start/) to the documentation and installation instructions.

# How to run the project
### 1. Commands
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

### 2. Coding
#### 2.1. Starting up
Run the server in your VM terminal
```
python3 manage.py runserver
```

Create a **Template** folder inside the **app** folder. Now, inside the **Template** folder create your index.html and paste Bootstrap's CDN in it.
Modify views.py file to connect the index.html file.

#### 2.2. Models and migrations
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


#### 2.3. Docker image
If you don't create a tag for the image like **user_docker_hub/image_name**, you may have some problems. To avoid it when doing the build create the image with that name pattern.
```
docker build -t django-kube .
docker tag django-kube user_docker_hub/django-kube:django-kube
```

Now we run it
```
docker run django-kube
```


#### 2.4. Kubernetes
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


# How to use 

## Home Page
In the home page of **Byron Store** you'll find the following:
 - Three main buttons:
	 - Home
	 - Products
	 - Companies
 - A section of products named **Best Sellers**
 - A section for the companies named **Companies** containing two buttons:
	 - Product Registration
	 - Company Registration
##### You can always navigate back and forth from the sections in our site trought the main buttons.


## Product
### Products Button
If you click in the **Products** button, it'll show you a list with the products with it's respective id, code, name, company, description and value. In this page you can also find a searchbar. On the right side of the value column you'll find three more buttons which represents the features:
 - View Info
 - Edit Info
	 - here you'll be able to edit any log on the product, except for the **id** and will find a **Save** button
 - Delete Product 
	 - which will automatically delete the product, so be careful with that

### Product Registration button
If you click in the **Product Registration** button, it'll show you a form page with fields that must be completed and a **Save** button for when you finish filling it.
When you click the **Save** button, it'll take you to the **Registered Products** page, that now contains the product you just added and the products that were already registered.


## Company 
### Companies button
If you click in the **Companies button**, it'll show you a list with the companies with it's respective id, code, CNPJ, name, addres, e-mail and phone. In this page you can also find a searchbar. On the right side of the value column you'll find three icon buttons which represents the features:
 - View Info
 - Edit Info
	 - here you'll be able to edit any log on the company, except for the **id** and will find a **Save** button
 - Delete Company  
	 - which will automatically delete the product, so be careful with that
### Company Registration button
If you click in the **Company Registration** button, it'll show you a form page with fields that must be completed and a **Save** button for when you finish filling it.
When you click the **Save** button, it'll take you to the **Registered Companies** page, that now contains the company you just added and the companies that were already registered.



# Our Team
- Tania Eliza Oliveira - [GitHub](https://github.com/elizaoliveira88)
- Milena Maria Costa Pininga - [GitHub](https://github.com/mmcpininga)
- Maria Fernanda Soares - [GitHub](https://github.com/mafesoares)
- Bruna Logatti - [GitHub](https://github.com/brulogatti)
- Beatriz Abne Alqueres Cruz - [GitHub](https://github.com/Abne-b)
