from django.db import models


class TFilm(models.Model):
    fid = models.CharField(max_length=255)
    actor = models.CharField(max_length=255, blank=True, null=True)
    cata_log_name = models.CharField(max_length=255)
    cata_log_id = models.CharField(max_length=255, blank=True, null=True)
    evaluation = models.FloatField()
    image = models.CharField(max_length=255, blank=True, null=True)
    is_use = models.IntegerField()
    loc_name = models.CharField(max_length=255, blank=True, null=True)
    loc_id = models.CharField(max_length=255, blank=True, null=True)
    name = models.CharField(max_length=255, blank=True, null=True)
    on_decade = models.CharField(max_length=255, blank=True, null=True)
    plot = models.TextField(blank=True, null=True)
    resolution = models.CharField(max_length=255, blank=True, null=True)
    status = models.CharField(max_length=255, blank=True, null=True)
    sub_class_name = models.CharField(max_length=255, blank=True, null=True)
    sub_class_id = models.CharField(max_length=255, blank=True, null=True)
    type_name = models.CharField(max_length=255, blank=True, null=True)
    type_id = models.CharField(max_length=255, blank=True, null=True)
    update_time = models.CharField(max_length=255, blank=True, null=True)
    is_vip = models.IntegerField(blank=True, null=True)

    class Meta:
        db_table = 't_film'


"""
        "_id": "5be14edb9d21223dd50660f8",
        "createdAt": "2018-11-06T08:20:43.656Z",
        "desc": "2018-11-06",
        "publishedAt": "2018-11-06T00:00:00.0Z",
        "source": "web",
        "type": "福利",
        "url": "https://ws1.sinaimg.cn/large/0065oQSqgy1fwyf0wr8hhj30ie0nhq6p.jpg",
        "used": true,
        "who": "lijinshanmx"

"""


class Girl(models.Model):
    created_date = models.CharField(max_length=255)
    desc = models.CharField(max_length=255)
    published = models.CharField(max_length=255)
    source = models.CharField(max_length=20, null=True)
    type = models.CharField(max_length=30)
    url = models.CharField(max_length=255)
    used = models.BooleanField(default=True)
