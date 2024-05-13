from django.shortcuts import render
from django.http import Http404

DATA = {
    'omlet': {
        'яйца, шт': 2,
        'молоко, л': 0.1,
        'соль, ч.л.': 0.5,
    },
    'pasta': {
        'макароны, г': 0.3,
        'сыр, г': 0.05,
    },
    'buter': {
        'хлеб, ломтик': 1,
        'колбаса, ломтик': 1,
        'сыр, ломтик': 1,
        'помидор, ломтик': 1,
    },
    # можете добавить свои рецепты ;)
}


def recipe_view(request, dish):
    servings = request.GET.get('servings')
    ingredients = DATA.get(dish)

    if ingredients is not None:
        # Если указано количество порций, умножаем количество ингредиентов
        if servings:
            try:
                servings = int(servings)
                ingredients = {ingredient: quantity * servings for ingredient, quantity in ingredients.items()}
            except ValueError:
                # Если количество порций не может быть преобразовано в число, возвращаем исходные данные
                raise Http404("Количество порций должно быть целым числом.")

        context = {
            'recipe': ingredients
        }
        return render(request, 'calculator/recipe.html', context)
    else:
        # Если блюдо не найдено, вызываем исключение 404
        raise Http404(f"Блюдо '{dish}' не найдено.")

def index(request):
    return render(request, 'calculator/index.html')