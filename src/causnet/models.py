from django.db import models


class SWM(models.Model):
    agent_name = models.CharField('agent name', max_length=128)
    creation_date = models.DateTimeField('creation date')

    def __str__(self):
        return 'swm_' + self.agent_name


class SWMFragment(models.Model):
    swm = models.ForeignKey(SWM, on_delete=models.CASCADE)
    content = models.TextField(max_length=2048)
    activation = models.IntegerField(default=0)

    def __str__(self):
        return str(self.swm) + '_' + str(self.pk)
