from django.test import TestCase, Client

# Create your tests here.

class alertViewTest(TestCase):

	def test_get_method_not_allowed(self):
		c = Client()
		response = c.get('/realtimeapp/')
		self.assertEquals(response.status_code, 405)


	def test_no_alert_condition(self):
		c = Client()
		response = c.post('/realtimeapp/', \
			{"SERVER_ID":1220, "CPU_UTILIZATION":50, "MEMORY_UTILIZATION":10, "DISK_UTILIZATION": 40}, \
			content_type = "application/json")
		self.assertEquals(response.json()["ALERT"], False)
		self.assertEquals(response.json()["SERVER_ID"], 1220)

	def test_cpu_alert(self):
		c = Client()
		response = c.post('/realtimeapp/', \
			{"SERVER_ID":1220, "CPU_UTILIZATION":87, "MEMORY_UTILIZATION":10, "DISK_UTILIZATION": 40}, \
			content_type = "application/json")
		self.assertEquals(response.json()["ALERT"], True)
		self.assertEquals(response.json()["SERVER_ID"], 1220)
		self.assertEquals(response.json()["RULES_VIOLATED"][0], "CPU_UTILIZATION 87% Expected <=85%")

	def test_memory_alert(self):
		c = Client()
		response = c.post('/realtimeapp/', \
			{"SERVER_ID":1220, "CPU_UTILIZATION":50, "MEMORY_UTILIZATION":80, "DISK_UTILIZATION": 40}, \
			content_type = "application/json")
		self.assertEquals(response.json()["ALERT"], True)
		self.assertEquals(response.json()["SERVER_ID"], 1220)
		self.assertEquals(response.json()["RULES_VIOLATED"][0], "MEMORY_UTILIZATION 80% Expected <=75%")

	def test_disk_alert(self):
		c = Client()
		response = c.post('/realtimeapp/', \
			{"SERVER_ID":1220, "CPU_UTILIZATION":50, "MEMORY_UTILIZATION":10, "DISK_UTILIZATION": 74}, \
			content_type = "application/json")
		self.assertEquals(response.json()["ALERT"], True)
		self.assertEquals(response.json()["SERVER_ID"], 1220)
		self.assertEquals(response.json()["RULES_VIOLATED"][0], "DISK_UTILIZATION 74% Expected <=60%")

	def test_cpu_memory_alert(self):
		c = Client()
		response = c.post('/realtimeapp/', \
			{"SERVER_ID":1220, "CPU_UTILIZATION":87, "MEMORY_UTILIZATION":80, "DISK_UTILIZATION": 40}, \
			content_type = "application/json")
		self.assertEquals(response.json()["ALERT"], True)
		self.assertEquals(response.json()["SERVER_ID"], 1220)
		self.assertEquals(response.json()["RULES_VIOLATED"][0], "CPU_UTILIZATION 87% Expected <=85%")
		self.assertEquals(response.json()["RULES_VIOLATED"][1], "MEMORY_UTILIZATION 80% Expected <=75%")

	def test_cpu_disk_alert(self):
		c = Client()
		response = c.post('/realtimeapp/', \
			{"SERVER_ID":1220, "CPU_UTILIZATION":87, "MEMORY_UTILIZATION":10, "DISK_UTILIZATION": 74}, \
			content_type = "application/json")
		self.assertEquals(response.json()["ALERT"], True)
		self.assertEquals(response.json()["SERVER_ID"], 1220)
		self.assertEquals(response.json()["RULES_VIOLATED"][0], "CPU_UTILIZATION 87% Expected <=85%")
		self.assertEquals(response.json()["RULES_VIOLATED"][1], "DISK_UTILIZATION 74% Expected <=60%")

	def test_memory_disk_alert(self):
		c = Client()
		response = c.post('/realtimeapp/', \
			{"SERVER_ID":1220, "CPU_UTILIZATION":50, "MEMORY_UTILIZATION":80, "DISK_UTILIZATION": 74}, \
			content_type = "application/json")
		self.assertEquals(response.json()["ALERT"], True)
		self.assertEquals(response.json()["SERVER_ID"], 1220)
		self.assertEquals(response.json()["RULES_VIOLATED"][0], "MEMORY_UTILIZATION 80% Expected <=75%")
		self.assertEquals(response.json()["RULES_VIOLATED"][1], "DISK_UTILIZATION 74% Expected <=60%")


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
