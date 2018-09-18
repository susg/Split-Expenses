# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase
from split.models import *
# Create your tests here.

class LoginTestCase(TestCase):

    def setUp(self):

        self.credentials = {'username' : 'test_user', 'password' : 'test_pass' }
        user = User.objects.create_user(**self.credentials)
        u = UserProfile(user = user, total_balance = 0)
        u.save()
        
    def test_logout(self):

        resp = self.client.get('/split/logout/')
        self.assertEqual(resp.status_code, 200)
        resp = self.client.get('/split/')
        self.assertEqual(resp.status_code, 302)

    def test_login(self):

        resp = self.client.get('/split/login/')
        self.assertEqual(resp.status_code, 200)
        self.client.post('/split/login/', {'username': 'test_user', 'password' : 'test_pass' } )
        resp = self.client.get('/split/')
        self.assertEqual(resp.status_code, 200)
        
class GroupTestCase(TestCase):

    def setUp(self):

        self.credentials = {'username' : 'test_user', 'password' : 'test_pass' }
        user = User.objects.create_user(**self.credentials)
        u = UserProfile(user = user, total_balance = 0)
        u.save()
        self.client.post('/split/login/', {'username': 'test_user', 'password' : 'test_pass' } )
        
        
    def test_create_group(self):

        resp = self.client.get('/split/create_group/')
        #print resp
        self.assertEqual(resp.status_code, 200)
        self.client.post('/split/creating/', {'name': 'test_group', 'description' : 'testing' } )
        resp = self.client.get('/split/group/1/')
        self.assertEqual(resp.status_code, 200)
        
