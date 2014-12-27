from django.db import models
from userprofile.models import UserProfile
import os
from django.conf import settings
from django.core.files.storage import FileSystemStorage


class OverwriteStorage(FileSystemStorage):

    def get_available_name(self, name):
        """
        Returns a filename that's free on the target storage system, and
        available for new content to be written to.
        """
        # If the filename already exists, remove it as if it was a true file system
        if self.exists(name):
            os.remove(os.path.join(settings.MEDIA_ROOT, name))
        return name


# Classes and Functions for Kit Model

def upload_kit_image(instance, filename):
    return "kits/" + instance.name + "/" + filename


class CommonInfo(models.Model):
    name = models.CharField(max_length=100)

    def __unicode__(self):
        return self.name

    class Meta:
        abstract = True


class Price(CommonInfo):
    cost = models.DecimalField(max_digits=10, decimal_places=2)


class Sale(CommonInfo):
    percent_off = models.DecimalField(max_digits=10, decimal_places=2)


class Tag(models.Model):
    name = models.CharField(max_length=50)

    def __unicode__(self):
        return self.name


class KitDescription (CommonInfo):
    selling_point1 = models.TextField(blank=True)
    selling_point2 = models.TextField(blank=True)
    selling_point3 = models.TextField(blank=True)
    author = models.CharField(max_length=50, blank=True)
    date_created = models.CharField(max_length=50, blank=True)


class Kit (CommonInfo):
    new = models.BooleanField(default=True)
    on_sale = models.BooleanField(default=False)
    soundcloud = models.CharField(max_length=500)
    image = models.FileField(upload_to=upload_kit_image, storage=OverwriteStorage())
    tags = models.ManyToManyField(Tag)
    description = models.ForeignKey(KitDescription)
    price = models.ForeignKey(Price)
    sale = models.ForeignKey(Sale)
    user_rating = models.DecimalField(max_digits=5, decimal_places=4, default=0)


# Classes and Functions for Sample Model

def upload_sample_demo(instance, filename):
    return "kits/" + instance.kit.name + "/samples/demo/" + filename


def upload_sample(instance, filename):
    return "kits/" + instance.kit.name + "/samples/wav/" + filename


class Sample(models.Model):
    name = models.CharField(max_length=50)
    demo = models.FileField(upload_to=upload_sample_demo, storage=OverwriteStorage())
    wav = models.FileField(upload_to=upload_sample, storage=OverwriteStorage())
    kit = models.ForeignKey(Kit, related_name="samples")
    KICK = 'KD'
    SNARE = 'SD'
    CLAP = 'CP'
    OVERHEAD = 'OH'
    PERCUSSION = 'PC'
    SOUNDFX = 'FX'
    LOOP = 'LO'
    SAMPLE_TYPE_CHOICES = (
        (KICK, 'Kick'),
        (SNARE, 'Snare'),
        (CLAP, 'Clap'),
        (PERCUSSION, 'Percussion'),
        (SOUNDFX, 'Sound FX'),
        (LOOP, 'Loop'),
    )
    type = models.CharField(max_length=2, choices=SAMPLE_TYPE_CHOICES)

    def __unicode__(self):
        return self.name

# Classes and Functions for Custom Kit Model


class CustomKit(CommonInfo):
    user = models.ForeignKey(UserProfile, related_name='custom_kits')
    date = models.DateField(auto_now_add=True)
    samples = models.ManyToManyField(Sample)


######## SIGNALS (for model deletion etc.)
# Receive the pre_delete signal and delete the file associated with the model instance.
from django.db.models.signals import pre_delete
from django.dispatch.dispatcher import receiver


@receiver(pre_delete, sender=Sample)
def sample_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.demo.delete(False)
    instance.wav.delete(False)


@receiver(pre_delete, sender=Kit)
def kit_delete(sender, instance, **kwargs):
    # Pass false so FileField doesn't save the model.
    instance.image.delete(False)



# class Unit (models.Model):
#     title = models.CharField(max_length=50)
#     course = models.ForeignKey(Course)
#
#     def __unicode__(self):
#         return self.title
#
#
# class Lesson (models.Model):
#     title = models.CharField(max_length=50)
#     course = models.ForeignKey(Course)
#     unit = models.ForeignKey(Unit)
#
#     def __unicode__(self):
#         return self.title
#
#     @property
#     def sorted_video_set(self):
#         return self.video_set.order_by('ordering_number')
#
#
# class Video (models.Model):
#     title = models.CharField(max_length=50)
#     course = models.ForeignKey(Course)
#     unit = models.ForeignKey(Unit)
#     lesson = models.ForeignKey(Lesson)
#     embed_url = models.CharField(max_length=150)
#     instructor_notes = models.TextField(max_length=None)
#     ordering_number = models.IntegerField()
#
#     def __unicode__(self):
#         return self.title
#
#     def has_quiz(self):
#         if len(self.multiplechoice_set.all()) < 1:
#             return False
#         else:
#             return True
#
#     def type_quiz(self):
#         quiz = self.multiplechoice_set.all()[0]
#         return quiz.type
#
# class Resource (models.Model):
#     title = models.CharField(max_length=100)
#     description = models.TextField()
#     link = models.CharField(max_length=150)
#     video = models.ForeignKey(Video)
#
#     def __unicode__(self):
#         return self.title
#
#
# class Quiz (models.Model):
#     video = models.ForeignKey(Video)
#     question_instructions = models.TextField()
#
#     class Meta:
#         abstract = True
#
# class MultipleChoice (Quiz):
#     a = models.TextField(blank=True)
#     b = models.TextField(blank=True)
#     c = models.TextField(blank=True)
#     d = models.TextField(blank=True)
#     correct_answer = models.CharField(max_length=1)
#     type = "MultipleChoice"
#
# class UserCourse():
#     message = "idontknowyet"
#
# class ActiveCourses():
#     courses = []
#     def add_course(self, user_course):
#         courses.append(user_course)




