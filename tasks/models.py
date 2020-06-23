from django.db import models
from projects.models import Project
from profiles.models import Profile
import asana
import os

class Task(models.Model):
    asana_id = models.CharField(default=None, blank=True, max_length=40)
    name = models.CharField(default=None, max_length=40)
    text = models.TextField(default=None)
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    user = models.ForeignKey(Profile, blank=True, default=None, on_delete=models.NOT_PROVIDED)

    def save(self, *args, **kwargs):
        if self._state.adding:
            result = self._add_task_to_asana()
            self.asana_id = result['gid']
        else:
            self._edit_asana_task()

        super().save(*args, **kwargs)

    def _add_task_to_asana(self):
        client = asana.Client.access_token(os.environ.get('ASANA_KEY'))
        data = {
            "approval_status": "pending",
            "assignee": str(self.user.asana_id),
            "assignee_status": "upcoming",
            "completed": False,
            "due_at": "2020-09-15T02:06:58.147Z",
            "followers": [
            ],
            "html_notes": "<body>{}</body>".format(self.text),
            "liked": True,
            "name": self.name,
            "notes": "Mittens really likes the stuff from Humboldt.",
            "parent": None,
            "projects": [
                str(self.project.asana_id)
            ],
            "resource_subtype": "default_task",
            "start_on": "2020-09-14",
            "workspace": os.environ.get('WORKSPACE_ID')
        }

        result = client.tasks.create_task(data, opt_pretty=True)

        return result

    def _edit_asana_task(self):
        client = asana.Client.access_token(os.environ.get('ASANA_KEY'))

        data = {
            "assignee": str(self.user.asana_id),
            "name": self.name,
            "html_notes": "<body>{}</body>".format(self.text),
        }

        client.tasks.update_task(str(self.asana_id), data, opt_pretty=True)