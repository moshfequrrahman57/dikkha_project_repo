# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models
from django import forms


class OtpserviceTrainees(models.Model):
    id = models.BigAutoField(primary_key=True)
    year = models.IntegerField()
    course = models.CharField(max_length=100)
    batch = models.CharField(max_length=100)
    roll_number = models.IntegerField(unique=True)
    name = models.CharField(max_length=100)
    mobile_number = models.CharField(unique=True, max_length=15)
    # new field added for email
    email = models.EmailField(unique=False, null=True, blank=True, max_length=254)

    class Meta:
        managed = True
        db_table = 'otpService_trainees'


class CertificateAuthority(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=100) # নাম
    designation = models.CharField(max_length=100) # পদবী
    signature_image = models.ImageField(upload_to='signatures/') # ছবি (স্বাক্ষর বা প্রোফাইল)

    def __str__(self):
        return f"{self.name} - {self.designation}"

    class Meta:
        managed = True
        db_table = 'certificate_authorities'



class CertificateAuthorityForm(forms.ModelForm):
    class Meta:
        model = CertificateAuthority
        fields = ['name', 'designation', 'signature_image']
