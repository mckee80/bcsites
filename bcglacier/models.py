from django.db import models
from cloudinary.models import CloudinaryField

# Create your models here.
from django.db import models

class Parks(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)  # This field type is a guess.
    latitude = models.FloatField()
    longitude = models.FloatField()

    class Meta:
        managed = True
        db_table = 'parks'

    def __str__(self):
	    return self.name

class Sites(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)  # This field type is a guess.
    park = models.ForeignKey(Parks, on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    elevation = models.IntegerField(blank=True, null=True)
    fires = models.CharField(max_length=5, blank=True, null=True)  # This field type is a guess.
    code = models.CharField(max_length=3, blank=True, null=True)  # This field type is a guess.
    area = models.CharField(max_length=40, blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'sites'

    def __str__(self):
	    return self.name


class Ratings(models.Model):
    sid = models.ForeignKey(Sites, on_delete=models.CASCADE)
    rating = models.IntegerField()
    user = models.CharField(max_length=40, blank=True, null=True)
    address = models.CharField(max_length=40, blank=True, null=True)
    comments = models.TextField(blank=True, null=True)
    comment_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'ratings'

    def __str__(self):
	    return str(self.rating)

class Information(models.Model):
    sid = models.ForeignKey(Sites, on_delete=models.CASCADE)
    user = models.CharField(max_length=40, blank=True, null=True)
    address = models.CharField(max_length=40, blank=True, null=True)
    info = models.TextField(blank=True, null=True)
    info_date = models.DateTimeField(blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'information'

    def __str__(self):
	    return str(self.info)

class Photo(models.Model):
    ## Misc Django Fields
    create_time = models.DateTimeField(auto_now_add=True)
    title = models.CharField("Title (optional)", max_length=200, blank=True)
    sid = models.ForeignKey(Sites, on_delete=models.CASCADE)

    ## Points to a Cloudinary image
    image = CloudinaryField('image')
    user = models.CharField(max_length=40, blank=True, null=True)

    """ Informative name for model """
    def __unicode__(self):
        try:
            public_id = self.image.public_id
        except AttributeError:
            public_id = ''
        return "Photo <%s:%s>" % (self.title, public_id)

class Sitesavgrating(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    park_id = models.IntegerField(blank=True, null=True)
    area = models.CharField(max_length=40, blank=True, null=True)
    fires = models.CharField(max_length=5, blank=True, null=True)
    elevation = models.IntegerField(blank=True, null=True)
    code = models.CharField(max_length=3, blank=True, null=True)
    avgrating = models.DecimalField(max_digits=65535, decimal_places=65535, blank=True, null=True)

    class Meta:
        managed = False  # Created from a view. Don't remove.
        db_table = 'SitesAvgRating'
