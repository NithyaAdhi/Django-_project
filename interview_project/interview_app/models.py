from django.db import models

class School(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Class(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Student(models.Model):
    id = models.AutoField(primary_key=True)
    fullname = models.CharField(max_length=200)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)

    def __str__(self):
        return self.fullname

class Assessment_Areas(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Answers(models.Model):
    id = models.AutoField(primary_key=True)
    answer = models.TextField()
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)

    def __str__(self):
        return self.answer

class Awards(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Subject(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    score = models.IntegerField()

    def __str__(self):
        return self.name

class Summary(models.Model):
    id = models.AutoField(primary_key=True)
    school_id = models.ForeignKey(School, on_delete=models.CASCADE)
    answer_id = models.ForeignKey('Answers', on_delete=models.CASCADE, related_name='summary_answer_set')
    sydney_participants = models.IntegerField()
    sydney_percentile = models.FloatField()
    assessment_area_id = models.ForeignKey(Assessment_Areas, on_delete=models.CASCADE)
    award_id = models.ForeignKey(Awards, on_delete=models.CASCADE)
    class_id = models.ForeignKey(Class, on_delete=models.CASCADE)
    correct_answer_percentage_per_class = models.FloatField()
    correct_answer = models.TextField()
    student_id = models.ForeignKey(Student, on_delete=models.CASCADE)
    participant = models.BooleanField()
    student_score = models.IntegerField()
    subject_id = models.ForeignKey(Subject, on_delete=models.CASCADE)
    category_id = models.IntegerField()
    year_level_name = models.CharField(max_length=200)
    #answer_id = models.ForeignKey(Answers, on_delete=models.CASCADE)
    #correct_answer_id = models.ForeignKey(Answers, on_delete=models.CASCADE)
    correct_answer_id = models.ForeignKey('Answers', on_delete=models.CASCADE, related_name='summary_correct_answer_set')


    def __str__(self):
        return self.school_id.name