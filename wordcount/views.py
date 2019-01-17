from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'wordcount/home.html')

def about(request):
    return render(request, 'wordcount/about.html')

def count(request):
    full_text = request.GET['fulltext']

    word_list = full_text.split()

    word_dic = {}

    for word in word_list:
        if word in word_dic:
            word_dic[word] += 1
        else:
            word_dic[word] = 1


    return render(request, 'wordcount/count.html', {'fulltext': full_text, 'dictionary': word_dic.items(), 'total': len(word_list)})