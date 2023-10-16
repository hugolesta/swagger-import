variable "env" {
  default = {
    name           = "eg-apigw"
    environment    = "dev"
    role           = "DevOps"
    costCenter     = "sys-team"
    tagVersion     = "0.0.1"
    owner          = "hlesta@icloud.com"
    project        = "swagger-import"
    expirationDate = "22/01/2030"
    region         = "eu-west-1"
  }
}
