from django.db import models

class Question(models.Model):
    question_text = models.CharField(max_length=200)
    pub_date = models.DateTimeField('date published')


class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)



class Blog(models.Model):
	# title 변수는 최대 길이 200인 짧은 문자열 형식으로 정의
	title = models.CharField(max_length=200)
	# writer 변수는 100
	writer = models.CharField(max_length=100)
	# pub_date 는 날짜-시간 형식으로 정의
	pub_date = models.DateTimeField()
	body = models.TextField()