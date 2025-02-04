# VisionMD_Backend

## Introduction
This repository contains the BackEnd of VisionMD software, a tool used for quantificaition of motor symtoms from videos. 

To run this repository, you also need to download the [FrontEnd](https://github.com/mea-lab/VideoAnalysisToolFrontend), which is also available in github. 

Running the BackEnd and front end toguether allows you to modify both components to fit your needs. 

## Stand alone application

If you only want to run the softare without modifying it, please visit the [dev branch](https://github.com/mea-lab/VideoAnalysisToolBackend/tree/dev). Instructions to download and run a stand alone application are avaliable there. 

The stand alone application is only available for Window and MacOS. 

## Set up the project locally

To run the project locally, clone the current repository and follow the next steps. 

<details>
<summary>Windows / MacOS</summary>

To setup the project locally, you need to install anaconda, which can be obtained from [here](https://www.anaconda.com/download/success). Please make sure to install the correct version for your OS. 

After succesfully installing anaconda, open a new terminal window in the folder containing the repository andcreate a new virtual environment with Python 3.10

```bash
conda create --name VisionMD python=3.10
```

Activate the virtual environment using the following command:

```bash
conda activate VisionMD
```

and install the requiered packages

```bash
pip install -r requirements.txt
```

Start the server using the following command:

```bash
python manage.py runserver
```

Server runs on port 8080 

To terminate the server, press ```Control``` + ```C```

</details>

<details>
<summary>Linux</summary>

To setup the project locally, you need to install Python3 before proceeding. 


Open a new terminal window in the folder containing the repository and create a vitual environment using the following command:

```bash
python3.10 -m venv VisionMD
```

Activate the virtual environment using the following command:

```bash
source VisionMD/bin/activate
```

and install the requiered packages

```bash
pip install -r requirements.txt
```

Start the server using the following command:

```bash
python manage.py runserver
```

Server runs on port 8080 


To terminate the server, press ```Control``` + ```C```
</details>



Now go to download the [FrontEnd](https://github.com/mea-lab/VideoAnalysisToolFrontend) and follow the step described there to run the local sever. 


# Running the Backend with Docker Compose

## Prerequisites
- Ensure Docker and Docker Compose are installed on your system.

## Steps

1. **Build the Docker Images:**

    ```bash
    docker compose build
    ```

    This command builds the Docker images specified in your `docker-compose.yml` file.

2. **Start the Containers:**

    ```bash
    docker compose up -d
    ```

    This command starts the containers in detached mode. The `-d` flag ensures that the containers run in the background.

3. **Stop and Remove Containers with Volumes:**

    ```bash
    docker compose down --volumes
    ```

    This command stops and removes the containers, along with any associated volumes, ensuring a clean state.

---

You can now efficiently build, start, and stop your backend using Docker Compose with these commands.
