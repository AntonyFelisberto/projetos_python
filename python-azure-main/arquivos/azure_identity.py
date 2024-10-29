from azure.identity import *
credential = AzureCliCredential()
credential = InteractiveBrowserCredential()
credential = VisualStudioCodeCredential()
credential = EnvironmentCredential()
credential = UsernamePasswordCredential()
credential = DefaultAzureCredential()
credential = SharedTokenCacheCredential()