from django.shortcuts import render

def show_main(request):
    context = {
        'npm' : '2306215923',
        'name': 'Shaney Zoya Fiandi',
        'class': 'PBP A'
    }

    return render(request, "main.html", context)