from django.contrib.auth.decorators import login_required
from models import *
from datetime import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django import template
from django.template.loader import get_template 
from django.shortcuts import render, redirect

@login_required(login_url='/split/login/')
def profile(request):

	user = request.user
	#print user.username
	#print UserProfile.objects.all()

	groups = user.users.members.all()
	owner = user.users.owners.all()

	return render(request, 'split/home.html',
		{
			'groups' : groups,
			'owner' : owner,
		})			
	
def group_profile(request, group_id):

	print "I am here"
	group = Group.objects.get(pk = group_id).groups
	#print group.members.all()
	record = group.expensedetail_set.all()
	#print record
	pers_exp = {}
	tot_sum = 0
	for r in record:
		tot_sum += r.amount
		try:
			pers_exp[r.spender.user.username] += r.amount
		except KeyError:
			pers_exp[r.spender.user.username] = r.amount

	pps = tot_sum/3

	print pers_exp

	return render(request, 'split/group.html',
		{
			'group' : group,
			'members' : group.members.all(),
			'record' : record,
			'sum' : tot_sum,
			'pps' : tot_sum/3,
			'pers_exp' : pers_exp,
		})			
	
def add_expense(request, group_id):

	return render(request, 'split/add_expense.html',
	{
		'group_id' : group_id,
	})
	#return HttpResponse("Hello, world. You're at group.")

def adding(request, group_id):

	spender = request.user.users
	group = Group.objects.get(pk = group_id).groups
	date_sp = request.POST['date']
	amount = request.POST['amount']
	details = request.POST['details']

	r = ExpenseDetail(spender = spender, group_spent = group, date_spent = date_sp,
		 				amount = amount, details = details)
	r.save()
	#group.add(r)

	return redirect('group_profile', group_id = group_id)

def delete_expense(request, group_id):

	return render(request, 'split/delete_expense.html',
	{
		'group_id' : group_id,
	})
	#return HttpResponse("Hello, world. You're at group.")

def deleting(request, group_id):

	spender = request.user.users
	group = Group.objects.get(pk = group_id).groups
	date_sp = request.POST['date']
	amount = request.POST['amount']
	details = request.POST['details']

	r = ExpenseDetail(spender = spender, group_spent = group, date_spent = date_sp,
		 				amount = amount, details = details)
	r.save()
	#group.add(r)

	return redirect('group_profile', group_id = group_id)



