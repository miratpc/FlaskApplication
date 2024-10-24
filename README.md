# Using MongoDB on Kubernetes for a Containerized Python Application with Flask

## Abstract
This project demonstrates the development, deployment, and containerization of a Python Flask application that interacts with MongoDB on a Kubernetes cluster. The solution uses Docker for containerization and Kubernetes for orchestration, providing a scalable architecture for a bookshop database.

## Task 1: MongoDB Deployment

### MongoDB StatefulSet
We deployed MongoDB using Kubernetes StatefulSet to ensure stateful operation and data persistence.
- **Replicas**: 1 MongoDB pod
- **ServiceName**: `mongodb`
- **VolumeClaimTemplates**: Storage provision of 1GB

### MongoDB Service
A Kubernetes service (`mongo-service.yaml`) was created to provide access to the MongoDB instance.
- **Protocol**: TCP
- **Port**: 27017

## Task 2: Develop Python Application

### Flask Application Overview
This bookstore management system performs CRUD operations on a MongoDB database using Flask.
- **app.py**: Initializes Flask and connects to MongoDB via PyMongo.
- **routes.py**: Defines URL routes for book management.
- **model.py**: Contains the `Book` class for data modeling.
- **forms.py**: Defines forms for adding, editing, and deleting books.

### Docker Containerization
The Python Flask app was containerized using Docker.
- **Dockerfile**: Specifies the base image and dependencies.
- **Port**: 5000

## Task 3: Kubernetes Deployment

The Python application was deployed on Kubernetes using the following files:
- `app-deployment.yaml`
- `flask-app-configmap.yaml`
- `mongo-service.yaml`
- `mongo-statefulset.yaml`

### ConfigMaps
Kubernetes ConfigMaps were used for configuration management, enabling a clean separation of concerns.

## Task 4: Service Discovery

Kubernetes Services were utilized for dynamic communication between Flask and MongoDB.
- **MongoDB Service**: Exposes MongoDB for the Flask app using the DNS name `mongo-service`.

## Conclusion
This project demonstrates a scalable, containerized Python Flask application with MongoDB using Kubernetes. It leverages Docker for containerization and Kubernetes for dynamic orchestration, showcasing modern microservice deployment strategies.
