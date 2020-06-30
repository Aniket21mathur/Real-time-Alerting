from django.test import TestCase, Client


class alertViewTest(TestCase):

	# test for methof not allowed for GET request
	def test_get_method_not_allowed(self):
		c = Client()
		response = c.get('/realtimeapp/')
		self.assertEquals(response.status_code, 405)

	# test for no rule voilation condition
	def test_no_alert_condition(self):
		c = Client()
		response = c.post('/realtimeapp/', \
			{"SERVER_ID":1220, "CPU_UTILIZATION":50, "MEMORY_UTILIZATION":10, "DISK_UTILIZATION": 40}, \
			content_type = "application/json")
		self.assertEquals(response.json()["ALERT"], False)
		self.assertEquals(response.json()["SERVER_ID"], 1220)

	# test when CPU_UTILIZATION rule is voilated
	def test_cpu_alert(self):
		c = Client()
		response = c.post('/realtimeapp/', \
			{"SERVER_ID":1220, "CPU_UTILIZATION":87, "MEMORY_UTILIZATION":10, "DISK_UTILIZATION": 40}, \
			content_type = "application/json")
		self.assertEquals(response.json()["ALERT"], True)
		self.assertEquals(response.json()["SERVER_ID"], 1220)
		self.assertEquals(response.json()["RULES_VIOLATED"][0], "CPU_UTILIZATION 87% Expected <=85%")

	# test when MEMORY_UTILIZATION rule is voilated
	def test_memory_alert(self):
		c = Client()
		response = c.post('/realtimeapp/', \
			{"SERVER_ID":1220, "CPU_UTILIZATION":50, "MEMORY_UTILIZATION":80, "DISK_UTILIZATION": 40}, \
			content_type = "application/json")
		self.assertEquals(response.json()["ALERT"], True)
		self.assertEquals(response.json()["SERVER_ID"], 1220)
		self.assertEquals(response.json()["RULES_VIOLATED"][0], "MEMORY_UTILIZATION 80% Expected <=75%")

	# test when DISK_UTILIZATION rule is voilated
	def test_disk_alert(self):
		c = Client()
		response = c.post('/realtimeapp/', \
			{"SERVER_ID":1220, "CPU_UTILIZATION":50, "MEMORY_UTILIZATION":10, "DISK_UTILIZATION": 74}, \
			content_type = "application/json")
		self.assertEquals(response.json()["ALERT"], True)
		self.assertEquals(response.json()["SERVER_ID"], 1220)
		self.assertEquals(response.json()["RULES_VIOLATED"][0], "DISK_UTILIZATION 74% Expected <=60%")

	# test when CPU_UTILIZATION and MEMORY_UTILIZATION rules are voilated
	def test_cpu_memory_alert(self):
		c = Client()
		response = c.post('/realtimeapp/', \
			{"SERVER_ID":1220, "CPU_UTILIZATION":87, "MEMORY_UTILIZATION":80, "DISK_UTILIZATION": 40}, \
			content_type = "application/json")
		self.assertEquals(response.json()["ALERT"], True)
		self.assertEquals(response.json()["SERVER_ID"], 1220)
		self.assertEquals(response.json()["RULES_VIOLATED"][0], "CPU_UTILIZATION 87% Expected <=85%")
		self.assertEquals(response.json()["RULES_VIOLATED"][1], "MEMORY_UTILIZATION 80% Expected <=75%")

	# test when CPU_UTILIZATION and DISK_UTILIZATION rules are voilated
	def test_cpu_disk_alert(self):
		c = Client()
		response = c.post('/realtimeapp/', \
			{"SERVER_ID":1220, "CPU_UTILIZATION":87, "MEMORY_UTILIZATION":10, "DISK_UTILIZATION": 74}, \
			content_type = "application/json")
		self.assertEquals(response.json()["ALERT"], True)
		self.assertEquals(response.json()["SERVER_ID"], 1220)
		self.assertEquals(response.json()["RULES_VIOLATED"][0], "CPU_UTILIZATION 87% Expected <=85%")
		self.assertEquals(response.json()["RULES_VIOLATED"][1], "DISK_UTILIZATION 74% Expected <=60%")

	# test when MEMORY_UTILIZATION and DISK_UTILIZATION rules are voilated
	def test_memory_disk_alert(self):
		c = Client()
		response = c.post('/realtimeapp/', \
			{"SERVER_ID":1220, "CPU_UTILIZATION":50, "MEMORY_UTILIZATION":80, "DISK_UTILIZATION": 74}, \
			content_type = "application/json")
		self.assertEquals(response.json()["ALERT"], True)
		self.assertEquals(response.json()["SERVER_ID"], 1220)
		self.assertEquals(response.json()["RULES_VIOLATED"][0], "MEMORY_UTILIZATION 80% Expected <=75%")
		self.assertEquals(response.json()["RULES_VIOLATED"][1], "DISK_UTILIZATION 74% Expected <=60%")


	# test when CPU_UTILIZATION, MEMORY_UTILIZATION and DISK_UTILIZATION rules are voilated
	def test_cpu_memory_disk_alert(self):
		c = Client()
		response = c.post('/realtimeapp/', \
			{"SERVER_ID":1220, "CPU_UTILIZATION":87, "MEMORY_UTILIZATION":80, "DISK_UTILIZATION": 74}, \
			content_type = "application/json")
		self.assertEquals(response.json()["ALERT"], True)
		self.assertEquals(response.json()["SERVER_ID"], 1220)
		self.assertEquals(response.json()["RULES_VIOLATED"][0], "CPU_UTILIZATION 87% Expected <=85%")
		self.assertEquals(response.json()["RULES_VIOLATED"][1], "MEMORY_UTILIZATION 80% Expected <=75%")
		self.assertEquals(response.json()["RULES_VIOLATED"][2], "DISK_UTILIZATION 74% Expected <=60%")
