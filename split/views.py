from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from models import *
from datetime import datetime
from django.http import HttpResponseRedirect, HttpResponse
from django.urls import reverse
from django import template
from django.template.loader import get_template 
from django.shortcuts import render, redirect

def sign_up(request):

	return render(request, 'split/sign_up.html')

def signing_up(request):

	user = User.objects.create_user(
		username = request.POST['username'],
		email = request.POST['email'],
		password = request.POST['pwd'],
		first_name = request.POST['fname'],
		last_name = request.POST['lname']
	)
	u = UserProfile(user = user, total_balance = 0)
	u.save()
	user = authenticate(username = request.POST['username'],
			 password = request.POST['pwd'],)
	login(request, user)
	
	return redirect('profile')

@login_required(login_url='/split/login/')
def profile(request):

	user = request.user
	#print user.username
	#print UserProfile.objects.all()

	groups = user.users.members.all()
	owner = user.users.owners.all()
	
	return render(request, 'split/home.html',
		{
			'user' : user,
			'groups' : groups,
			'owner' : owner,
		})			
	
def group_profile(request, group_id):

	user = request.user
	group = GroupProfile.objects.get(pk = group_id)
	#print group.members.all()
	record = group.expensedetail_set.all()
	pers_exp = {}
	tot_sum = 0
	for r in record:
		tot_sum += r.amount
		try:
			pers_exp[r.spender.user.username][0] += r.amount
		except KeyError:
			pers_exp[r.spender.user.username] = []
			pers_exp[r.spender.user.username].append(r.amount)

	for key in pers_exp:
		pers_exp[key].append(
			(pers_exp[key][0]*100)/tot_sum
		)
		print pers_exp[key][1]
	#pps = tot_sum/len()

	#print pers_exp

	return render(request, 'split/group.html',
		{
			'group' : group,
			'members' : group.members.all(),
			'record' : record,
			'sum' : tot_sum,
			'pps' : tot_sum/(len(group.members.all()) + 1),
			'pers_exp' : pers_exp,
			'groups' : user.users.members.all(),
			'owner' : user.users.owners.all(),
	
		})			
	
def add_expense(request, group_id):

	return render(request, 'split/add_expense.html',
	{
		'group_id' : group_id,
	})
	#return HttpResponse("Hello, world. You're at group.")

def adding_expense(request, group_id):

	spender = request.user.users
	group = GroupProfile.objects.get(pk = group_id)
	date_sp = request.POST['date']
	amount = request.POST['amount']
	details = request.POST['details']

	r = ExpenseDetail(spender = spender, group_spent = group, date_spent = date_sp,
		 				amount = amount, details = details)
	r.save()
	#group.add(r)

	return redirect('group_profile', group_id = group_id)

def delete_expense(request, group_id):

	group = GroupProfile.objects.get(pk = group_id)
	record = group.expensedetail_set.all()
	
	return render(request, 'split/delete_expense.html',
	{
		'group_id' : group_id,
		'record' : record,
	})
	#return HttpResponse("Hello, world. You're at group.")

'''def deleting(request, group_id):

	for r in request.POST.getlist('record'):
		ExpenseDetail.objects.filter(id = r).delete()

	return redirect('group_profile', group_id = group_id)
	#return HttpResponse("Hello, world. You're at group.")
'''

def deleting(request, record_id):

	r = ExpenseDetail.objects.get(id = record_id)
	group_id = r.group_spent.id 
	r.delete()

	return redirect('group_profile', group_id = group_id)


def create_group(request):

	user = request.user
	#print user.username
	#print UserProfile.objects.all()

	groups = user.users.members.all()
	owner = user.users.owners.all()
	
	return render(request, 'split/create_group.html',
		{
			'user' : user,
			'groups' : groups,
			'owner' : owner,
		})			


def creating(request):

	owner = request.user.users
	name = request.POST['name']
	desc = request.POST['description']
	date_created = datetime.now().date()

	g = GroupProfile(name = name, description = desc, date_created = date_created,
						user_created = owner)
	g.save()
	#g.members.add(owner)
	return redirect('group_profile', group_id = g.id)

def add_member(request, group_id):

	return render(request, 'split/add_member.html',
		{
			'group_id' : group_id
		})

import json as simplejson
def autocompleteModel(request):
    search_qs = User.objects.filter(username__startswith=request.GET['search'])
    results = []
    for r in search_qs:
        results.append(r.username)
    resp = request.GET['callback'] + '(' + simplejson.dumps(results) + ');'
    return HttpResponse(resp, content_type='application/json')

def adding_member(request, group_id):

	user = User.objects.get(username = request.POST['username']).users
	group = GroupProfile.objects.get(pk = group_id)
	group.members.add(user)

	return redirect('group_profile', group_id = group_id)
	
	'''spender = request.user.users
	group = Group.objects.get(pk = group_id).groups
	date_sp = request.POST['date']
	amount = request.POST['amount']
	details = request.POST['details']

	r = ExpenseDetail(spender = spender, group_spent = group, date_spent = date_sp,
		 				amount = amount, details = details)
	r.save()
	#group.add(r)

	return redirect('group_profile', group_id = group_id)
'''



