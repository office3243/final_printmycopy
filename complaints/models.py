from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.urls import reverse_lazy, reverse


# User_Model = get_user_model()
User_Model = settings.AUTH_USER_MODEL


class ComplaintCategory(models.Model):
    name = models.CharField(max_length=128)
    email_to_send = models.EmailField()
    order = models.SmallIntegerField(unique=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Complaint Category"
        verbose_name_plural = "Complaint Categories"


class Complaint(models.Model):

    STATUS_CHOICES = (("IN", "Inititated"), ("PR", "Processing"), ("SL", "Solved"))

    user = models.ForeignKey(User_Model, on_delete=models.CASCADE)
    category = models.ForeignKey(ComplaintCategory, on_delete=models.CASCADE)
    description = models.TextField()
    attachment = models.ImageField(upload_to="complaints/attachments/", blank=True, null=True)

    status = models.CharField(max_length=2, choices=STATUS_CHOICES, default="IN")

    created_on = models.DateTimeField(auto_now_add=True)
    solved_on = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return self.user.get_display_text

    @property
    def get_absolute_url(self):
        return reverse_lazy("complaints:update", kwargs={"pk": self.id})

    @property
    def get_delete_url(self):
        return reverse_lazy("complaints:delete", kwargs={"pk": self.id})

    @property
    def get_status(self):
        return self.get_status_display

    @property
    def get_display_text(self):
        return self.details[:25]

    @property
    def get_date(self):
        return self.created_on.date

    @property
    def get_description_display(self):
        if len(self.description) < 25:
            return self.description
        return "{}...".format(self.description[:25])
