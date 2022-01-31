from django.shortcuts import render
from .models import FeedBack
from .forms import FeedBackForm
import joblib


def index(request):
    text = ''
    if request.method == 'POST':
        form = FeedBackForm(request.POST)
        if form.is_valid():
            filename_model = 'log_model'
            filename_cv = 'cv_model'

            loaded_model = joblib.load(filename_model)
            loaded_cv = joblib.load(filename_cv)

            text = [form.cleaned_data.get("data")] 
            form_for_cv = loaded_cv.transform(text)

            result = loaded_model.predict(form_for_cv)[0]
            print(result)
            form.save()

    if(text) :
        if result == 0:
            result = 'This is a negative review'
        else:
            result = 'This is a positive review'
        form = FeedBackForm()
        context = {'form': form, 'text': text[0], 'result': result}
        return render(request, 'main/index.html',context)

    form = FeedBackForm()
    context = {'form': form}
    return render(request, 'main/index.html',context)


def all_fb(request):
    fbs = FeedBack.objects.all()
    return render(request, 'main/all_fbs.html', {'fbs': fbs})  