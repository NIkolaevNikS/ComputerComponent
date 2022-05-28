from django.test import TestCase
from django.contrib.auth import get_user_model
from django.contrib.auth import authenticate
from .models import Manufacturer, M_Mouse


# Create your tests here.

class SigninTest(TestCase):
    """Тест на создание пользователя и проверка его авторизации"""
    def setUp(self):
        self.user = get_user_model().objects.create_user(username='test', password='12345', email='test@example.com')
        self.user.save()

    def test_correct(self):
        """Тест на успешную авторизацию пользователя
        TRUE если пользователь авторизирован
        FALSE если пользователь не авторизован
        """
        user = authenticate(username='test', password='12345')
        self.assertTrue((user is not None) and user.is_authenticated)

    def test_wrong_username(self):
        """
        Тест на ошибку авторизации пользователя
        TRUE если пользователь не авторизован
        FALSE если пользователь авторизирован
        """
        user = authenticate(username='wrong', password='12345')
        self.assertFalse(user is not None and user.is_authenticated)


class M_Mouse_ModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        M_Mouse.objects.create(M_Mouse_name='G PRO')

    def test_get_absolute_url(self):
        """Тест на совпадение адресов ссылок"""
        mouse = M_Mouse.objects.get(M_Mouse_id=1)
        self.assertEquals(mouse.get_absolute_url(), '/mouse/1/')


class ManufacturerModelTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.Manufacturer = Manufacturer.objects.create(
            Manufacturer_name="Hyperx"
        )

    def test_it_has_information_fields(self):
        """Тест на совпадение типов данных"""
        self.assertIsInstance(self.Manufacturer.Manufacturer_name, str)
