module "eg_dev_api_gtw" {
  source     = "git::https://github.com/cloudposse/terraform-null-label.git?ref=master"
  namespace  = "eg"
  stage      = "dev"
  name       = "test-api-gateway"
  attributes = ["public"]
  delimiter  = "-"

  tags = {
    name           = lower(var.env["name"])
    environment    = lower(var.env["environment"])
    role           = lower(var.env["role"])
    costCenter     = lower(var.env["costCenter"])
    tagVersion     = lower(var.env["tagVersion"])
    owner          = lower(var.env["owner"])
    project        = lower(var.env["project"])
    expirationDate = lower(var.env["expirationDate"])
    region         = lower(var.env["region"])
  }
}
