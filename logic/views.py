from django.http import HttpResponse
from django.template.loader import get_template
from django.template import Template, Context, TemplateSyntaxError
from django.shortcuts import render, render_to_response
from django.utils.safestring import mark_safe

from .models import Dropdown
from .forms import FilterNameForm
from .utilities import parse_filters

def main(request):
    origin = 'Request here'
    if request.method == 'POST':
    # create a form instance and populate it with data from the request:
        form = FilterNameForm(request.POST)
        # check whether it's valid (not so useful in this case):
        if form.is_valid():
            try:
                searched_name = form.cleaned_data["filter_name"]
                origin = Dropdown.objects.get(name=searched_name).philter
            except Dropdown.DoesNotExist:
                origin = "isn't in the database yet."
    # if a GET method
    else:
        if 'user_input' in request.GET:
            origin = request.GET['user_input']
        else:
            origin = 'Nothing is filtered'
    template = get_template("bs_template.html")
    names_in_dropdown =  [item.name for item in Dropdown.objects.all()]
    parsed_message = parse_filters(origin)
    if len(parsed_message["filters"]) > 0:
        # mark_safe to prevent escaping of quotes in filters
        result = mark_safe("{{ subject%s }}"% "".join(parsed_message["filters"]))
    else: result = "No filters were provided yet."
    context_without_subject = Context(
        {'result': result,
        'names_list': names_in_dropdown,
        'origin':origin
        },
        )
    # compose html with one variable left and provided filters
    html_without_subject = template.render(context_without_subject)
    try:
        template = Template(html_without_subject)
    except TemplateSyntaxError:
        return HttpResponse(render_to_response(
            'bs_template.html',
            {
            'names_list': names_in_dropdown,
            'result': "Not a filter",
            'origin':origin,
            }
            ))
    context = Context({'subject': parsed_message["subject"]})
    http = template.render(context)
    return HttpResponse(http)
