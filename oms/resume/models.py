# coding=utf-8
__author__ = 'Administrator'
from django.db import models


class CV(models.Model):
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'),
    )
    TITLE_CHOICES = (
        ('GS.', u'Giao Su'),
        ('PGS.', u'Pho Giao Su'),
        ('TS.', u'Tien Sy'),
        ('ThS.', u'Thac Sy'),
        ('CN.', u'Cu Nhan'),
        ('KS.', u'Ky Su'),
        (' ', u'Khac')
    )
    user_id = models.IntegerField()
    full_name = models.CharField(max_length=64)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    date_of_birth = models.DateField()
    title = models.CharField(max_length=5, choices=TITLE_CHOICES)
    major1 = models.CharField(max_length=64)
    major2 = models.CharField(max_length=64)
    major3 = models.CharField(max_length=64)

    position_vi = models.CharField(max_length=64)
    position_en = models.CharField(max_length=64)

    organization_vi = models.CharField(max_length=128)
    organization_en = models.CharField(max_length=128)

    department_vi = models.CharField(max_length=128)
    department_en = models.CharField(max_length=128)
    organization_address = models.CharField(max_length=256)
    organization_city = models.CharField(max_length=256)

    identification_number = models.CharField(max_length=12)

    email_main = models.CharField(max_length=64)
    email_backup = models.CharField(max_length=64)
    phone_work = models.CharField(max_length=16)
    phone_mobile = models.CharField(max_length=16)
    fax = models.CharField(max_length=16)
    other = models.TextField()


class Education(models.Model):
    cv = models.ForeignKey(CV)
    school_name_vi = models.CharField(max_length=128)
    school_name_en = models.CharField(max_length=128)
    school_address = models.CharField(max_length=512)
    school_start_year = models.CharField(max_length=4)
    school_end_year = models.CharField(max_length=4)
    major_vi = models.CharField(max_length=64)
    major_en = models.CharField(max_length=64)
    degree_vi = models.CharField(max_length=24)
    degree_en = models.CharField(max_length=24)
    # file PDF chứng chỉ, bằng cấp, < 5MB
    pdf_file = models.FileField(upload_to='degree/%Y/%m/%d')


class Job(models.Model):
    cv = models.ForeignKey(CV)
    organization_vi = models.CharField(max_length=128)
    organization_en = models.CharField(max_length=128)
    department_vi = models.CharField(max_length=128)
    department_en = models.CharField(max_length=128)
    organization_address = models.CharField(max_length=512)
    position_vi = models.CharField(max_length=64)
    position_en = models.CharField(max_length=64)
    organization_start_year = models.CharField(max_length=4)
    organization_end_year = models.CharField(max_length=4)
    organization_tel = models.CharField(max_length=16)
    note = models.TextField()


class Major(models.Model):
    cv = models.ForeignKey(CV)
    major_vi = models.CharField(max_length=64)
    major_en = models.CharField(max_length=64)


class Project(models.Model):
    cv = models.ForeignKey(CV)
    name = models.CharField(max_length=512)
    organisation = models.CharField(max_length=512)
    start_date = models.DateField()
    end_date = models.DateField()
    role = models.CharField(max_length=64)


class Publication(models.Model):
    cv = models.ForeignKey(CV)
    PUBLICATION_TYPES = (
        ('ISI', u'Bài báo ISI'),
        ('nonISI', u'Bài báo quốc tế khác'),
        ('Proceeding', u'Bài báo tại hội thảo/hội nghị trong và ngoài nước'),
        ('VN', u'Bài báo trên các tạp chí khoa học trong nước'),
        ('Other', u'Khác (Sách chuyên khảo, bằng sáng chế, giải thưởng khoa học, ...)')
    )
    type_pub = models.CharField(max_length=10, choices=PUBLICATION_TYPES)
    title = models.CharField(max_length=1024)
    authors = models.CharField(max_length=512)
    publisher = models.CharField(max_length=512)
    issn = models.CharField(max_length=64)
    publish_year = models.CharField(max_length=4)
    pdf_file = models.FileField(upload_to='publication/%Y/%m/%d')
    note = models.TextField()


class Language(models.Model):
    LANGUAGE_CHOICES = (
        ('EN', u'Tiếng Anh'),
        ('FR', u'Tiếng Pháp'),
        ('DE', u'Tiếng Đức'),
        ('JP', u'Tiếng Nhật'),
        ('KR', u'Tiếng Hàn'),
        ('CN', u'Tiếng Trung')
    )
    LEVEL_CHOICES = (
        ('Excellent', u'Thành thạo'),
        ('Good', u'Khá'),
        ('Fair', u'Trung bình'),
        ('Bad', u'Yếu')
    )
    cv = models.ForeignKey(CV)
    language = models.CharField(max_length=2, choices=LANGUAGE_CHOICES)
    level = models.CharField(max_length=10, choices=LEVEL_CHOICES)
