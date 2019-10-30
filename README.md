# td-workflow

Unofficial Treasure Workflow API client.

```py
import os

from tdworkflow.client import Client

apikey = os.getenv("TD_API_KEY")
client = Client(site="us", apikey=apikey)
projects = client.projects("pandas-df")

secrets = {"td.apikey": apikey, "td.apiserver": "https://api.treasuredata.com", "test": "secret-foo"}

client.set_secrets(projects[0], secrets)

client.secrets(projects[0])
# ['td.apikey', 'td.apiserver', "test"]
wf.delete_secrets(["test", "td.apiserver"])
```
