from django.shortcuts import render
from .models import Record
from xml.etree.ElementTree import Element, SubElement, tostring
from xml.etree import ElementTree
from xml.dom import minidom
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse


# Create your views here.
@csrf_exempt
def record_list(request):
    records = Record.objects.order_by('score').reverse()[:10].values()

    root = Element("Records")
    root.set('version', '1.0')

    for record in records:
        element_record = SubElement(root, "record")
        element_record.set('player_name', record['player_name'])
        element_record.set('score', str(record['score']))
        element_record.set('joke_comment', record['joke_comment'])

    rough_string = ElementTree.tostring(root, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return HttpResponse(reparsed.toprettyxml(indent="  "))

@csrf_exempt
def send_record(request):
    player_name = request.POST["player_name"]
    score = request.POST["score"]

    record = Record.objects.get_new_record(player_name, score)
    record.save()

    return HttpResponse(200)