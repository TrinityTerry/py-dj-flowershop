from django.shortcuts import render

def add_bouquets(request):
    """
    This view handles all request to the add bouquets page
    url_ex: bouquet/form
    """
    if request.method == "GET":
        template = "bouquets/bouquets_form.html"
        context = {}
        return render(request, template, context)

def edit_bouquets(request, bouquet_id):
    """
    This view handles all request to the edit bouquet page
    url_ex: bouquet/1/form
    """
    if request.method == "GET":
        template = "bouquets/bouquets_form.html"
        context = {}
        return render(request, template, context)
