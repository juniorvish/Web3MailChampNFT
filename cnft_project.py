```python
import requests
from underdog import underdogApi

class CNFTProject:
    def __init__(self, project_name, metadata_link):
        self.project_name = project_name
        self.metadata_link = metadata_link

    def create_project(self):
        payload = {
            "project_name": self.project_name,
            "metadata_link": self.metadata_link
        }
        response = requests.post(f"{underdogApi}/projects", data=payload)
        return response.json()

    def get_project(self, project_id):
        response = requests.get(f"{underdogApi}/projects/{project_id}")
        return response.json()

    def update_project(self, project_id, new_metadata_link):
        payload = {
            "metadata_link": new_metadata_link
        }
        response = requests.patch(f"{underdogApi}/projects/{project_id}", data=payload)
        return response.json()

    def delete_project(self, project_id):
        response = requests.delete(f"{underdogApi}/projects/{project_id}")
        return response.json()
```