from django.test import TestCase
from djangoapp.forms import *

# Create your tests here.

class MyTests(TestCase):
    def test_forms(self):
        form_data = {'password1': 'password1'}
        form = CreateUserForm(data=form_data)
        self.assertTrue(form.is_valid())

class MyTests(TestCase):
    def test_forms(self):
        form_data = {'password2': 'password2'}
        form = CreateUserForm(data=form_data)
        self.assertTrue(form.is_valid())

class MyTests(TestCase):
    def test_forms(self):
        form_data = {'email': 'email'}
        form = CreateUserForm(data=form_data)
        self.assertTrue(form.is_valid())

class MyTests(TestCase):
    def test_forms(self):
        form_data = {'username': 'username'}
        form = CreateUserForm(data=form_data)
        self.assertTrue(form.is_valid())


class MyTests(TestCase):
    def test_forms(self):
        form_data = {'username': 'username'}
        form = UpdateUserForm(data=form_data)
        self.assertTrue(form.is_valid())

class MyTests(TestCase):
    def test_forms(self):
        form_data = {'email': 'email'}
        form = UpdateUserForm(data=form_data)
        self.assertTrue(form.is_valid())
