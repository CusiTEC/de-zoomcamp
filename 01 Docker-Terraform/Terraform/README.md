
## Terraform

In this section homework we'll prepare the environment by creating resources in GCP with Terraform.

In your VM on GCP/Laptop/GitHub Codespace install Terraform. 
Copy the files from the course repo
[here](https://github.com/DataTalksClub/data-engineering-zoomcamp/tree/main/01-docker-terraform/1_terraform_gcp/terraform) to your VM/Laptop/GitHub Codespace.

Modify the files as necessary to create a GCP Bucket and Big Query Dataset.


## Question 7. Creating Resources

After updating the main.tf and variable.tf files run:

```
terraform apply
```

Paste the output of this command into the homework submission form.
This set of commands and results is related to the use of Terraform, an infrastructure as code (IaC) tool that allows you to define and provision infrastructure declaratively. It looks like you are working with Google Cloud Platform (GCP) resources using Terraform.

### terraform init

This command initializes the Terraform working directory.
Download the necessary plugins for the provider (in this case, the Google Cloud Platform provider).
Configure the backend to store Terraform state (can be local or remote, depending on configuration).
```
(base) administrador@de-zoomcamp:~/data-engineering-zoomcamp/01-docker-terraform/1_terraform_gcp/terraform/terraform_with_variables$ terraform init

Initializing the backend...

Initializing provider plugins...
- Reusing previous version of hashicorp/google from the dependency lock file
- Using previously-installed hashicorp/google v5.6.0

Terraform has been successfully initialized!

You may now begin working with Terraform. Try running "terraform plan" to see
any changes that are required for your infrastructure. All Terraform commands
should now work.

If you ever set or change modules or backend configuration for Terraform,
rerun this command to reinitialize your working directory. If you forget, other
commands will detect it and remind you to do so if necessary.
```

### terraform plan
This command runs a simulation to show the changes Terraform plans to make to your infrastructure.
In my case, no changes were detected ("No changes"). Terraform compares the declarative configuration with the current state and shows if there is a difference.

```
terraform plan
google_storage_bucket.demo-bucket: Refreshing state... [id=zoomcamp-dataengineer-terra-bucket]
google_bigquery_dataset.demo_dataset: Refreshing state... [id=projects/zoomcamp-dataengineer/datasets/demo_dataset]

No changes. Your infrastructure matches the configuration.

Terraform has compared your real infrastructure against your configuration and found no differences, so no changes are needed.
```
### terraform apply
This command applies the changes detected by terraform plan.
In my case, after running terraform apply, Terraform detects that there have been changes external to Terraform to the google_storage_bucket.demo-bucket resource. It seems that some change was made directly to the GCP bucket.

```
google_storage_bucket.demo-bucket: Refreshing state... [id=zoomcamp-dataengineer-terra-bucket]
google_bigquery_dataset.demo_dataset: Refreshing state... [id=projects/zoomcamp-dataengineer/datasets/demo_dataset]

Note: Objects have changed outside of Terraform

Terraform detected the following changes made outside of Terraform since the last "terraform apply":

  # google_storage_bucket.demo-bucket has changed
  ~ resource "google_storage_bucket" "demo-bucket" {
        id                          = "zoomcamp-dataengineer-terra-bucket"
      + labels                      = {}
        name                        = "zoomcamp-dataengineer-terra-bucket"
        # (13 unchanged attributes hidden)

        # (1 unchanged block hidden)
    }


Unless you have made equivalent changes to your configuration, or ignored the relevant attributes using ignore_changes, the following
plan may include actions to undo or respond to these changes.

─────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────────

No changes. Your infrastructure matches the configuration.

Your configuration already matches the changes detected above. If you'd like to update the Terraform state to match, create and apply
a refresh-only plan:
  terraform apply -refresh-only

Apply complete! Resources: 0 added, 0 changed, 0 destroyed.
```