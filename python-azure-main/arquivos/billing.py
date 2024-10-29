from azure.identity import AzureCliCredential
from azure.mgmt.resource import ResourceManagementClient
from azure.mgmt.billing import BillingManagementClient

AZURE_SUBSCRIPTION_ID = ""

credential = AzureCliCredential()
resource_client = BillingManagementClient(credential,AZURE_SUBSCRIPTION_ID)

