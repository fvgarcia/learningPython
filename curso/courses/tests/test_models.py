from django.core import mail
from django.test import TestCase
from django.test.client import Client
from django.urls import reverse
from django.conf import settings

from model_mommy import mommy

from curso.courses.models import Course

class CourseManagerTestCase(TestCase):

    def setUp(self):
        self.courses_django = mommy.make(
            'courses.Course', name='Python Web with Django',
            _quantity=5
        )
        self.courses_dev = mommy.make(
            'courses.Course', name='Python for Devs',
            _quantity=10
        )
        self.client = Client()

    def tearDown(self):
        Course.objects.all().delete()

    def test_course_search(self):
        search = Course.objects.search('django')
        self.assertEqual(len(search), 5)
        search = Course.objects.search('devs')
        self.assertEqual(len(search), 10)