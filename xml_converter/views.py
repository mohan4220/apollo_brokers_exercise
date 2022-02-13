from django.http import JsonResponse
from django.shortcuts import render
from lib.Xml2JSON import Xml_to_json_converter

xml_to_json_converter = Xml_to_json_converter()

def upload_page(request):
    if request.method == 'POST':
        xml_file = request.FILES['document']
        xml_file_content = xml_file.read()
        converted_data = xml_to_json_converter.convert(xml_file_content)
        # TODO: Convert the submitted XML file into a JSON object and return to the user.
        return JsonResponse(converted_data)

    return render(request, "upload_page.html")
