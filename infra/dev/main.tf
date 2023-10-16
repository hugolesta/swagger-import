resource "aws_api_gateway_rest_api" "example" {

  name = "${module.eg_dev_api_gtw.tags.name}-${module.eg_dev_api_gtw.tags.project}"

  endpoint_configuration {
    types = ["REGIONAL"]
  }
}