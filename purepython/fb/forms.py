from django.forms import Form, CharField, Textarea

class UserPostForm():
	text = CharField(widget=Textarea(
		attrs={'rows': '5', cols': '100'}))
