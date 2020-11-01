# from django.test import TestCase
import json
from graphene_django.utils.testing import GraphQLTestCase


class MyTestCase(GraphQLTestCase):
	def test_create_user(self):
		response = self.query(
			'''
			userByUsername(
			username: "n_d_tai"
			){
				username
				joinDate
			}
			''',
			op_name='any'
		)

		content = json.load(response.content)

		self.assertResponseNoErrors(response)
