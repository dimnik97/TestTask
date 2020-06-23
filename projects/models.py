from django.db import models
import asana
import os

class Project(models.Model):
    asana_id = models.CharField(default=None, blank=True, max_length=40)
    name = models.CharField(max_length=40)

    def save(self, *args, **kwargs):
        if self._state.adding:
            result = self._add_project_to_asana()
            self.asana_id = result['gid']
        else:
            self._edit_asana_project()

        super().save(*args, **kwargs)

    def _add_project_to_asana(self):
        client = asana.Client.access_token(os.environ.get('ASANA_KEY'))
        data_to_send = {
            "archived": False,
            "color": "light-green",
            "current_status": {
                "author": {
                    "name": "Greg Sanchez"
                },
                "color": "green",
                "created_by": {
                    "name": "Greg Sanchez"
                },
                "html_text": "<body>The project <strong>is</strong> moving forward according to plan...</body>",
                "modified_at": None,
                "text": "The project is moving forward according to plan...",
                "title": "Status Update - Jun 15"
            },
            "default_view": "calendar",
            "due_date": "2019-09-15",
            "due_on": "2019-09-15",
            "followers": "",
            "html_notes": "<body>These are things we need to purchase.</body>",
            "is_template": False,
            "name": self.name,
            "notes": "These are things we need to purchase.",
            "owner": "1181390481219415",
            "public": False,
            "start_on": "2019-09-14",
            "team": os.environ.get('TEAM_ID')
        }

        result = client.projects.create_project(data_to_send, opt_pretty=True)
        return result

    def _edit_asana_project(self):
        client = asana.Client.access_token(os.environ.get('ASANA_KEY'))

        data_to_send = {
            'name': self.name
        }

        result = client.projects.update_project(str(self.asana_id), data_to_send, opt_pretty=True)
        return result
