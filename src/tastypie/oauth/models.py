from django.db import models

class OAuthConsumer(models.Model):

    name = models.CharField(max_length=255)
    key = models.CharField(max_length=255)
    secret = models.CharField(max_length=255)
    active = models.BooleanField(default=True)

    class Meta:
        db_table = "api_oauth_consumer"

    def __unicode__(self):
         return u'%s' % (self.name)

