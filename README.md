# Swagger import

This project is a tool that helps to import swagger files dynamically 

## Requirements

- [Python](https://www.python.org/downloads/) should be installed

## Usage

Make sure to install the requirements listed above.

Execute the following command to test it.

```bash
 make test PROJECT_SWAGGER_NAME=clothStore PROJECT_SWAGGER_PARAMETERS="{'basePath': 'Prepend','endpointConfigurationTypes': 'REGIONAL'}" PROJECT_API_GTW_ID=0jydhv3wp3 REGION=eu-west-1
```

Execute the following command to run in your local machine.

```
PROJECT_SWAGGER_NAME=clothStore PROJECT_SWAGGER_PARAMETERS="{'basePath': 'Prepend','endpointConfigurationTypes': 'REGIONAL'}" PROJECT_API_GTW_ID=0jydhv3wp3 python src/app.py
```


Firstly build the project running the following command

```bash
docker build -t swagger_import .
```

Then run the following command to run the container.

```bash
docker run \
    --rm -it \
    -e AWS_ACCESS_KEY_ID=XXXXXXXXXXXXXXXXXX \
    -e AWS_SECRET_ACCESS_KEY=XXXXXXXXXXXXXXXXXX \
    -e PROJECT_SWAGGER_NAME=clothStore \
    -e PROJECT_SWAGGER_PARAMETERS="{'basePath': 'Prepend','endpointConfigurationTypes': 'REGIONAL'}" \
    -e PROJECT_API_GTW_ID=0jydhv3wp3 \
    -e REGION=eu-west-1 \
    -e AWS_REGION=eu-west-1 \
    swagger_import \
    python app.py
```

## How to prepare a new swagger import process.

    - Make sure you are storing your `JSON` swagger files into `./tasks/swagger_files`.
    - You should create a new file with the same content of for instance `clothStore.py` and dont forget to add the same name that the `PROJECT_SWAGGER_NAME` environment variable.
    - Once you have created this new file, you should change the class name to the value of the environment variable `PROJECT_SWAGGER_NAME`.


The whole directory looks like the following.

```
|____infra
| |____dev
| | |____outputs.tf
| | |____main.tf
| | |____providers.tf
| | |____.gitignore
| | |____variables.tf
| | |____labels.tf
|____requirements.txt
|____Dockerfile
|____Makefile
|____README.md
|____.gitignore
|____src
| |____swagger
| | |____tasks
| | | |____swagger.py
| | | |____clothStore.py
| | | |____swagger_files
| | | | |____clothStore.json
| | | | |____petStore.json
| | | |____petStore.py
| | |____libs
| | | |____utils.py
| |____app.py
```


| Environment Variable  | Description  |
|---|---|
| PROJECT_SWAGGER_NAME | The name of the swagger file |
| PROJECT_SWAGGER_PARAMETERS | The parameters we need to import on Api Gateway  |
| PROJECT_API_GTW_ID  |  The id of Api Gateway |
| AWS_REGION  | The region where the API gateway was deployed |