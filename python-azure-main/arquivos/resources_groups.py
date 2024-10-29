from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient

AZURE_SUBSCRIPTION_ID = ""

credential = AzureCliCredential()
resource_client = ResourceManagementClient(credential,AZURE_SUBSCRIPTION_ID)

def creates():
    rg_result = resource_client.resource_groups.create_or_update(
        "test-resource-group",
        {"location":"eastus"}
    )
    rg_result = resource_client.resource_groups.create_or_update(
        resource_group_name="test-resource-group",
        parameters={
            "location": "eastus",
            "tags":{
                "environment":"development",
                "type":"genereal",
                "source":"udemy"
            }
        }
    )

def lists():
    group_list = resource_client.resource_groups.list()
    print("Resource group name:location")
    for group in group_list:
        print(f"{group.name}:{group.location}")

def deletes():
    for group in resource_client.resource_groups.list():
        print(group)

    rg_result = resource_client.resource_groups.begin_delete(resource_group_name="test-resource-group")
    rg_result.wait()