from django.shortcuts import render


# Create your views here.
def home(request):
    context = {
        'blog_entries': [
            {
                'title': 'Hello, world!',
                'body': 'I have created my first template in Django!',
                'date': 'Sep 27 ,2015',
                'person': "Henri"

            },
            {
                'title': 'Something in here',
                'body': 'Something else in there',
                'date': 'Sep 27, 2023',
                'person': 'Anna'
            },
            {
                'title': 'Oh Bummer!',
                'body': 'Am i doing it right?',
                'date': 'Sep 27, 2018',
                'person': 'Zaid'
            }
        ]
    }
    return render(request, 'home.html', context)


def posts(request):
    return render(request, "posts.html")
