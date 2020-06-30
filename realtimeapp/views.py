from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

import json


'''
	API for handling POST requests from the client

	`request`: request agrument with JSON body from the client

	returns: `405 method not allowed` if request.method == GET
	returns: `JSON` if request.method == POST

'''
@csrf_exempt
def alert(request):

	if request.method == 'GET':
		return HttpResponse(status=405)

	elif request.method == 'POST':
		# parse the request
		data = json.loads(request.body)
		server_id = data['SERVER_ID']
		cpu_utilization = data['CPU_UTILIZATION']
		memory_utilization = data['MEMORY_UTILIZATION']
		disk_utilization = data['DISK_UTILIZATION']

		rules_violated = []
		error_cpu_utilization = "CPU_UTILIZATION " + str(cpu_utilization) + "% Expected <=85%"
		error_memory_utilization = "MEMORY_UTILIZATION " + str(memory_utilization) + "% Expected <=75%"
		error_disk_utilization = "DISK_UTILIZATION " + str(disk_utilization) + "% Expected <=60%"

		# check for voilation of rules specified
		if int(cpu_utilization) > 85:
			rules_violated.append(error_cpu_utilization)
		if int(memory_utilization) > 75:
			rules_violated.append(error_memory_utilization)
		if int(disk_utilization) > 60:
			rules_violated.append(error_disk_utilization)

		result = {}
		if len(rules_violated) > 0:
			# response if any rule is voilated
			result['ALERT'] = "True"
			result['SERVER_ID'] = server_id
			result['RULES_VIOLATED'] = rules_violated
		else:
			# response if no rule is voilated
			result['ALERT'] = "False"
			result['SERVER_ID'] = server_id

		return JsonResponse(result)
