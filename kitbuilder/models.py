from django.db import models
from decimal import Decimal
from userprofile.models import UserProfile

# Classes and Functions for Kit Model

def upload_kit_image(instance, filename):
    return "kits/" + instance.name + "/" + filename

# Create your models here.
#class video(models.Model):
# url = models.CharField()


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
    tags = models.ManyToManyField(Tag)
    new = models.BooleanField(default=True)
    on_sale = models.BooleanField(default=False)
    soundcloud = models.CharField(max_length=200)
    image = models.FileField(upload_to=upload_kit_image)
    price = models.ForeignKey(Price)
    description = models.ForeignKey(KitDescription)
    sale = models.ForeignKey(Sale)
    choices = [1, 2, 3, 4, 5]
    rating = models.DecimalField(max_digits=5, decimal_places=4, default=0)


# Classes and Functions for Sample Model

def upload_sample_demo(instance, filename):
    return "kits/" + instance.kit.name + "/samples/demo/" + filename


def upload_sample(instance, filename):
    return "kits/" + instance.kit.name + "/samples/wav/" + filename


class Sample(models.Model):
    name = models.CharField(max_length=50)
    demo = models.FileField(upload_to=upload_sample_demo)
    wav = models.FileField(upload_to=upload_sample)
    kit = models.ForeignKey(Kit)
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
    user = models.ForeignKey(UserProfile)
    date = models.DateField(auto_now_add=True)
    samples = models.ManyToManyField(Sample)

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




