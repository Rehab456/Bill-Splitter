from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

@csrf_exempt
def split_evenly(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        total = data.get('total', 0)
        persons = data.get('persons', 0)

        if persons == 0:
            return JsonResponse({'error': 'Number of persons must be greater than 0'}, status=400)

        split_evenly = total / persons
        return JsonResponse({'split_per_person': split_evenly})
#{
#    "total": 100, 
#    "persons": 4
#}
    
@csrf_exempt
def split_unevenly(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        total = data.get('total', 0)
        persons = data.get('persons', [])

        if not persons:
            return JsonResponse({'error': 'No persons data provided'}, status=400)

        split_unevenly = total / len(persons)
        split = {}
        for person in persons:
            split[person["name"]] = split_unevenly - person.get("contribution", 0)

        return JsonResponse({'split': split})
#{
#    "total": 1000,
#    "persons": [
#        {"name": "Rehab", "contribution": 50},
#        {"name": "Taha", "contribution": 100},
#        {"name": "Fahad"}
#    ]
#}


@csrf_exempt
def split_evenly_with_tax_tip(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        total = data.get('total', 0)
        persons = data.get('persons', 0)  # Ensure this is the number of persons
        tax = data.get('tax', 0)
        tip = data.get('tip', 0)

        if persons == 0:
            return JsonResponse({'error': 'Number of persons must be greater than 0'}, status=400)

        total += tax + tip
        split_evenly_with_tax_tip = total / persons
        return JsonResponse({'split_per_person': split_evenly_with_tax_tip})
#{
#    "total": 200,
#    "persons": 4,
#    "tax": 20,
#    "tip": 30
#}


@csrf_exempt
def split_evenly_with_discount(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        total = data.get('total', 0)
        persons = data.get('persons', 0)
        discount = data.get('discount', 0)

        if persons == 0:
            return JsonResponse({'error': 'Number of persons must be greater than 0'}, status=400)

        total -= discount
        split_evenly_with_discount = total / persons
        return JsonResponse({'split_per_person': split_evenly_with_discount})
#{
#   "total": 100, 
#    "discount": 20, 
#    "persons": 5
#}

@csrf_exempt
def split_with_shared_items(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        user_ids = data.get('user_ids', [])
        items_name = data.get('items_name', [])
        shared_items = data.get('shared_items', [])

        if not user_ids or not items_name:
            return JsonResponse({'error': 'Missing user IDs or items'}, status=400)

        user_costs_rate = {user_id: 0 for user_id in user_ids}

        def add_costs(item_list):
            for item in item_list:
                price = float(item.get('price', 0))
                users = set(item.get('user_ids', []))
                if users:
                    cost = price / len(users)
                    for user in users:
                        if user in user_costs_rate:
                            user_costs_rate[user] += cost

        add_costs(items_name)
        add_costs(shared_items)

        return JsonResponse({user: round(cost, 2) for user, cost in user_costs_rate.items()})
    
    return JsonResponse({'error': 'Invalid method'}, status=405)
#{
#    "user_ids": ["user1", "user2", "user3"],
#    "items_name": [
#        {"price": 30, "user_ids": ["user1", "user2"]},
#        {"price": 20, "user_ids": ["user2", "user3"]}
#    ],
#    "shared_items": [
#        {"price": 40}
#    ]
#}
