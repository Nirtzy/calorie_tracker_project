from django.contrib.auth import logout
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm # Import the form
from django.contrib import messages
from .models import FoodItem
from django.http import JsonResponse

# Create your views here.

# This is a view function. It will be responsible for the homepage.
def home(request):
    from .models import FoodItem
    query = request.GET.get('q')
    results = None
    meal_result = None
    food_items = FoodItem.objects.all()
    if query:
        results = FoodItem.objects.filter(name__icontains=query)
        if not results.exists():
            messages.info(request, f'No food items found for "{query}".')
    if request.method == 'POST' and 'food_ids' in request.POST:
        total_calories = total_protein = total_fat = total_carbs = total_fiber = 0
        food_ids = request.POST.getlist('food_ids')
        for food_id in food_ids:
            qty = request.POST.get(f'qty_{food_id}')
            if food_id and qty and int(qty) > 0:
                try:
                    item = FoodItem.objects.get(id=food_id)
                    grams = int(qty)
                    factor = grams / 100.0
                    total_calories += item.calories * factor
                    total_protein += float(item.protein) * factor
                    total_fat += float(item.fat) * factor
                    total_carbs += float(item.carbs) * factor
                    total_fiber += float(item.fiber) * factor
                except FoodItem.DoesNotExist:
                    continue
        meal_result = {
            'calories': round(total_calories, 2),
            'protein': round(total_protein, 2),
            'fat': round(total_fat, 2),
            'carbs': round(total_carbs, 2),
            'fiber': round(total_fiber, 2),
        }
    return render(request, 'foods/home.html', {
        'results': results,
        'query': query,
        'food_items': food_items,
        'meal_result': meal_result
    })

def register(request):
    if request.method == 'POST':
        # If the form has been submitted, process the data
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save() # Save the new user to the database
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username}! You can now log in.')
            return redirect('login') # Redirect to the login page
    else:
        # If it's a GET request, just display a blank registration form
        form = UserCreationForm()
    return render(request, 'foods/register.html', {'form': form})

def logout_view(request):
    logout(request)
    messages.info(request, "You have been successfully logged out.")
    return redirect('home') # Redirect to the homepage

def food_search(request):
    q = request.GET.get('q', '')
    results = []
    if q:
        items = FoodItem.objects.filter(name__icontains=q)[:10]
        results = [{'id': item.id, 'name': item.name} for item in items]
    return JsonResponse(results, safe=False)
