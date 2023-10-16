.PHONY: all

DEFAULT_TARGET: all
PY_BIN ?= python
APP_VARS = AWS_SDK_LOAD_CONFIG=1

check-env:
  ifndef PROJECT_SWAGGER_NAME
    $(error PROJECT_SWAGGER_NAME is undefined. Use 'PROJECT_SWAGGER_NAME=<swagger-name>')
  endif

  ifndef PROJECT_SWAGGER_PARAMETERS
    $(error PROJECT_SWAGGER_PARAMETERS is undefined. Use 'PROJECT_SWAGGER_PARAMETERS=<json parameters>')
  endif

 ifndef PROJECT_API_GTW_ID
    $(error PROJECT_API_GTW_ID is undefined. Use 'PROJECT_API_GTW_ID=<api-gateway-id>')
  endif

 ifndef REGION
    $(error REGION is undefined. Use 'REGION=<aws-region>')
  endif

test:
	PROJECT_SWAGGER_NAME=$(PROJECT_SWAGGER_NAME) PROJECT_SWAGGER_PARAMETERS="$(PROJECT_SWAGGER_PARAMETERS)" PROJECT_API_GTW_ID=$(PROJECT_API_GTW_ID) AWS_REGION=$(REGION) $(APP_VARS) $(PY_BIN) src/app.py
	# PROJECT_SWAGGER_NAME=clothStore PROJECT_SWAGGER_PARAMETERS="{'basePath': 'Prepend','endpointConfigurationTypes': 'REGIONAL'}" PROJECT_API_GTW_ID=0jydhv3wp3 AWS_REGION=eu-west-1 $(APP_VARS) $(PY_BIN) src/app.py
