from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse, JsonResponse

import json

@csrf_exempt
def alert(request):

	if request.method == 'GET':
		return HttpResponse(status=405)

	elif request.method == 'POST':
		data = json.loads(request.body)
		server_id = data['SERVER_ID']
		cpu_utilization = data['CPU_UTILIZATION']
		memory_utilization = data['MEMORY_UTILIZATION']
		disk_utilization = data['DISK_UTILIZATION']

		rules_violated = []
		error_cpu_utilization = "CPU_UTILIZATION " + str(cpu_utilization) + "% Expected <=85%"
		error_memory_utilization = "MEMORY_UTILIZATION " + str(memory_utilization) + "% Expected <=75%"
		error_disk_utilization = "DISK_UTILIZATION " + str(disk_utilization) + "% Expected <=60%"

		if cpu_utilization > 85:
			rules_violated.append(error_cpu_utilization)
		if memory_utilization > 75:
			rules_violated.append(error_memory_utilization)
		if disk_utilization > 60:
			rules_violated.append(error_disk_utilization)

		result = {}
		if len(rules_violated) > 0:
			result['ALERT'] = True
			result['SERVER_ID'] = server_id
			result['RULES_VIOLATED'] = rules_violated
		else:
			result['ALERT'] = False
			result['SERVER_ID'] = server_id

		return JsonResponse(result)
