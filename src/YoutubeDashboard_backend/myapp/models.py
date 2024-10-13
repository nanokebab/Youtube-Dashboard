from django.db import models

class SubscribedVideos(models.Model):
    channel_id = models.TextField(blank=True, null=True)
    channel_name = models.TextField(blank=True, null=True)
    class_field = models.TextField(db_column='class', blank=True, null=True)  # Field renamed because it was a Python reserved word.
    video_id = models.TextField(blank=True, null=True)
    video_title = models.TextField(blank=True, null=True)
    video_url = models.TextField(blank=True, null=True)
    video_date = models.TextField(blank=True, null=True)  # This field type is a guess.
    thumbnail_url = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'subscribed_videos'
