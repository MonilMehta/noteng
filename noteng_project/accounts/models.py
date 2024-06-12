from django.db import models
from authentication.models import User
from cloudinary_storage.storage import RawMediaCloudinaryStorage
class VideolinksModel(models.Model):
    video_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100)
    sem = models.IntegerField()
    topics = models.CharField(max_length=100)
    links = models.URLField()

class PostModel(models.Model):
    post_id = models.AutoField(primary_key=True)
    # POST_TYPES = [
    #     ('Job', 'job_board'),
    #     ('Event', 'event')
    # ]
    ORGANIZERS = [
        ('college', 'college'),
        ('commitee', 'commitee')
    ]
    EVENT_TYPES = [
        ('hackathon', 'hackathon'),
        ('cultural', 'cultural'),
        ('datathon', 'datathon'),
        ('startup', 'startup')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.TextField()
    deadline = models.DateTimeField()
    post_url = models.URLField()
    description = models.TextField()
    likes = models.PositiveIntegerField()
    organised_by = models.CharField(max_length=50, choices=ORGANIZERS, default = ('college', 'college'))
    subtype = models.CharField(max_length=20, choices=EVENT_TYPES, default = ('hackathon', 'hackathon'))
    # type = models.CharField(max_length=10, choices=POST_TYPES)
    is_interested = models.BooleanField(default=False)
    date_updated = models.DateField(auto_now=True)
    date_uploaded = models.DateField(auto_now_add=True)
    image=models.ImageField(upload_to='images/',  storage=RawMediaCloudinaryStorage())

class JobBoardModel(models.Model):
    job_id = models.AutoField(primary_key=True)
    JOB_SUBTYPES = [
        ('internship', 'internship'),
        ('Job', 'job')
    ]
    STATUS_CHOICES = [
        ('Offline', 'offline'),
        ('Online', 'online'),
        ('Hybrid', 'hybrid'),
        ('Remote', 'remote')
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    company = models.CharField(max_length=50)
    JOB_TITLES = [
        ('Software Engineer', 'Software Engineer'),
        ('Data Analyst', 'Data Analyst'),
        ('Web Developer', 'Web Developer'),
        ('UI/UX Designer', 'UI/UX Designer'),
        ('Project Manager', 'Project Manager'),
        ('Business Analyst', 'Business Analyst'),
        ('Backend Developer', 'Backend Developer'),
        ('Frontend Developer', 'Frontend Developer'),
        ('Fullstack Developer', 'Fullstack Developer'),
        ('Machine Learning Engineer', 'Machine Learning Engineer'),
    ]
    job_title = models.CharField(max_length=50, choices=JOB_TITLES)
    subtype = models.CharField(max_length=10, choices=JOB_SUBTYPES)
    mode = models.CharField(max_length=10, choices=STATUS_CHOICES)
    location = models.CharField(max_length=50,default='Remote')
    contact_no = models.CharField(max_length=10)
    requirements = models.TextField()
    duration_in_months = models.IntegerField()  # new field
    description = models.TextField(default='')  # new field
    upload_time = models.DateTimeField(auto_now_add=True)


# class EventModel(models.Model):
#     event_id = models.AutoField(primary_key=True)
#     ORGANIZERS = [
#         ('college', 'college'),
#         ('commitee', 'commitee')
#     ]
#     EVENT_TYPES = [
#         ('hackathon', 'hackathon'),
#         ('cultural', 'cultural'),
#         ('datathon', 'datathon'),
#         ('startup', 'startup')
#     ]
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     organised_by = models.CharField(max_length=50, choices=ORGANIZERS)
#     subtype = models.CharField(max_length=20, choices=EVENT_TYPES)

class NotesModel(models.Model):
    note_id = models.AutoField(primary_key=True)
    RATING_CHOICES = [
        (1, 'One Star'),
        (2, 'Two Stars'),
        (3, 'Three Stars'),
        (4, 'Four Stars'),
        (5, 'Five Stars'),
    ]
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    note_title = models.TextField()
    note_description = models.TextField()
    subject = models.TextField()
    department = models.CharField(max_length=100)
    # rating = models.IntegerField(choices=RATING_CHOICES)
    document = models.FileField(upload_to='raw/',  storage=RawMediaCloudinaryStorage())

class NoteRating(models.Model):
    note = models.ForeignKey(NotesModel, related_name='ratings', on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    rating = models.IntegerField(choices=NotesModel.RATING_CHOICES)

    class Meta:
        unique_together = ('note', 'user')

class CalendarModel(models.Model):
    calendar_id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()
    title = models.CharField(max_length=100)
    description = models.TextField()
    note = models.TextField()

class MentorshipModel(models.Model):
    mentorship_id = models.AutoField(primary_key=True)
    mentor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentorships_mentor')
    mentee = models.ForeignKey(User, on_delete=models.CASCADE, related_name='mentorships_mentee')
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    expertise = models.CharField(max_length=50, blank=True)

    def save(self, *args, **kwargs):
        if not self.pk:  # If this is a new MentorshipModel instance
            self.expertise = self.mentor.expertise
        super().save(*args, **kwargs)