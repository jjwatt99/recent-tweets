from django.test import TestCase
from django.contrib.staticfiles.testing import StaticLiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

class ViewTests(TestCase):
	def test_index(self):
		res = self.client.get('/')
		self.assertEqual(res.status_code, 200)

	def test_get_data(self):
		ajax = {'HTTP_X_REQUESTED_WITH': 'XMLHttpRequest'}
		res = self.client.get('/api/data/', {'query': '#tapingo'}, **ajax)
		data = json.loads(res.content.decode('utf-8'))
		self.assertEqual(res.status_code, 200)
		self.assertTrue(type(data['info']) is list)

class FrontEndTests(StaticLiveServerTestCase):
	def setUp(self):
		self.selenium = webdriver.Chrome()
		self.selenium.implicitly_wait(5)
		super(FrontEndTests, self).setUp()

	def tearDown(self):
		self.selenium.quit()
		super(FrontEndTests, self).tearDown()

	def test_initial(self):
		selenium = self.selenium
		selenium.get(self.live_server_url)
		title = selenium.find_element_by_class_name('nav-title')
		assert title.text == 'Tapingo Twitter Assignment'
		items = selenium.find_elements_by_class_name('list-item')
		assert len(items) > 1

	def test_pagination(self):
		selenium = self.selenium
		selenium.get(self.live_server_url)
		search_bar = selenium.find_element_by_class_name('search-bar')
		button = selenium.find_element_by_class_name('search-button')
		search_bar.send_keys('#yolo')
		button.click()

		loaded = WebDriverWait(selenium, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'bottom-text'), '1 / 5'))
		next_arrow = selenium.find_element_by_id('next')
		next_arrow.click()

		found = WebDriverWait(selenium, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'bottom-text'), '2 / 5'))
		page = selenium.find_element_by_class_name('bottom-text')
		assert page.text == '2 / 5'
		
		prev_arrow = selenium.find_element_by_id('prev')
		prev_arrow.click()

		found = WebDriverWait(selenium, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'bottom-text'), '1 / 5'))
		page = selenium.find_element_by_class_name('bottom-text')
		assert page.text == '1 / 5'

	def test_search(self):
		selenium = self.selenium
		selenium.get(self.live_server_url)
		search_bar = selenium.find_element_by_class_name('search-bar')
		button = selenium.find_element_by_class_name('search-button')
		search_bar.send_keys('#yolo')
		button.click()

		loaded = WebDriverWait(selenium, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'bottom-text'), '1 / 5'))
		items = selenium.find_elements_by_class_name('list-item')
		assert len(items) > 1

	def test_x(self):
		selenium = self.selenium
		selenium.get(self.live_server_url)
		items = selenium.find_elements_by_class_name('list-item')
		x = selenium.find_element_by_id('x')
		x.click()

		loaded = WebDriverWait(selenium, 10).until(EC.text_to_be_present_in_element((By.CLASS_NAME, 'bottom-text'), '1 / 1'))
		page = selenium.find_element_by_class_name('bottom-text')
		assert page.text == '1 / 1'


