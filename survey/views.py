from django.shortcuts import render
from django.http import HttpResponseRedirect
from survey.settings import support_email
from survey.models import Survey, Category
from survey.forms import ResponseForm


def index(request):
    return render(request, 'index.html')


def survey_detail(request, p_id):
    survey = Survey.objects.get(id=p_id)
    category_items = Category.objects.filter(survey=survey)
    categories = [c.name for c in category_items]
    print 'categories for this survey:'
    print categories
    if request.method == 'POST':
        form = ResponseForm(request.POST, survey=survey)
        if form.is_valid():
            response = form.save()
            return HttpResponseRedirect("/confirm/%s" % response.interview_uuid)
    else:
        form = ResponseForm(survey=survey)
        print form
        # TODO sort by category
    return render(request, 'survey.html', {'response_form': form, 'survey': survey, 'categories': categories})


def confirm(request, uuid):
    email = support_email
    return render(request, 'confirm.html', {'uuid':uuid, "email": email})


def privacy(request):
    return render(request, 'privacy.html')


