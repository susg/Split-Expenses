from django.contrib.auth.models import User, Group
from django.db import models
from datetime import  datetime
 
class UserProfile(models.Model):
    user = models.OneToOneField(User, related_name='users')
    total_balance = models.IntegerField(default=0)

    def __str__(self):
    	return self.user.username

    def get_absolute_url(self):
        return reverse('userProfile-detail', args=[str(self.id)])    
    
class GroupProfile(models.Model):
    name = models.CharField(max_length=20)
    description = models.CharField(max_length=100, blank=True, default='')
    date_created = models.DateField(default=datetime.now, blank=True)
    user_created = models.ForeignKey(UserProfile, related_name='owners')
    members = models.ManyToManyField(UserProfile, related_name='members')

    def __str__(self):
    	return self.name

    def get_absolute_url(self):
        return reverse('groupProfile-detail', args=[str(self.id)])    
    
class ExpenseDetail(models.Model):
	spender = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
	group_spent = models.ForeignKey(GroupProfile, on_delete=models.CASCADE)
	details = models.CharField(max_length=20, blank=True, default='')
	amount = models.IntegerField(default=0)
	date_spent = models.DateField(default=datetime.now, blank=True)

	def __str__(self):
		return "%s %s" % (self.spender.user.username, self.group_spent.name)    