import re
from models import mainClassNameWithModel
eval(f'exec("from models import {mainClassNameWithModel}")')

allObjects = ""
filterForAdding = ""
filterForUpdating = ""

mainClassName = str(mainClassNameWithModel).replace("Model","")

classnameinsmall = str(mainClassName).lower()
my_list = re.findall('[a-zA-Z][^A-Z]*', mainClassName)
name2 = ""
for i in range(0,len(my_list)):
    if(i != len(my_list) - 1):
       name2+=f"{str(my_list[i]).lower()}_"
    else:
      name2+=f"{str(my_list[i]).lower()}"
classnameinsmall = name2
allObjectsForUpdate = f"            {classnameinsmall}_id = serializer.data['id']\n"

for key in vars(eval(mainClassNameWithModel)):
    if(not str(key).__contains__("__") and not str(key).__contains__("objects") and not str(key).__contains__("updated_at") and not str(key).__contains__("created_at") and not str(key).__contains__("id")):
        allObjects+=f'            {key} = serializer.data["{key}"]\n'
        allObjectsForUpdate+=f'            {key} = serializer.data["{key}"]\n'
        filterForAdding += f'                {key} = {key},\n'
        filterForUpdating+= f'            {classnameinsmall}_data.{key}={key}\n'


with open("/Users/apple/Downloads/flutter_tdd_automation/django_automation/serializers.py", 'r+') as f:
    f.truncate(0)

with open('/Users/apple/Downloads/flutter_tdd_automation/django_automation/serializers.py', 'w') as fp:
                  fp.write('''
"""Serializer for %s module"""

from rest_framework import serializers

from %s.models import %sModel


class Add%sSerializer(serializers.ModelSerializer):
    """Serializer for adding new %s details"""
    class Meta:
        """Meta class to change behaviour of model fields"""
        model = %sModel
        exclude = ["created_at","updated_at"]


class Get%sSerializer(serializers.ModelSerializer):
    """Serializer for get %s details"""
    id = serializers.IntegerField(default=None)
    class Meta:
        """Meta class to change behaviour of model fields"""
        model = %sModel
        fields = ["id"]

                  ''' %(classnameinsmall,classnameinsmall,mainClassName,
                        mainClassName,classnameinsmall,mainClassName,
                        mainClassName,classnameinsmall,mainClassName))


with open("/Users/apple/Downloads/flutter_tdd_automation/django_automation/urls.py", 'r+') as f:
    f.truncate(0)

with open('/Users/apple/Downloads/flutter_tdd_automation/django_automation/urls.py', 'w') as fp:
                  fp.write('''
"""
Api end points for %s module
"""

from django.urls import path
from %s import views


urlpatterns = [
    path('add_%s/', views.add_%s, name="add_%s"),
    path('get_%s/', views.get_%s, name="get_%s"),
    path('get_%s_by_id/', views.get_%s_by_id, name="get_%s_by_id"),
    path('delete_all_%s/', views.delete_%s, name="delete_%s"),
    path('delete_%s_by_id/', views.delete_%s_by_id, name="delete_%s_by_id"),
    path('update_%s/', views.update_%s, name="update_%s"),
]


                  ''' %(classnameinsmall,classnameinsmall,classnameinsmall,classnameinsmall,classnameinsmall,
                       classnameinsmall,classnameinsmall,classnameinsmall,classnameinsmall,classnameinsmall,classnameinsmall,
                       classnameinsmall,classnameinsmall,classnameinsmall,classnameinsmall,classnameinsmall,classnameinsmall,
                       classnameinsmall,classnameinsmall,classnameinsmall
                       ))

with open("/Users/apple/Downloads/flutter_tdd_automation/django_automation/views.py", 'r+') as f:
    f.truncate(0)

with open('/Users/apple/Downloads/flutter_tdd_automation/django_automation/views.py', 'w') as fp:
                  fp.write('''
from rest_framework.decorators import api_view
from rest_framework.response import Response
from response import Response as ResponseData
from rest_framework import status
from %s.models import %sModel
from %s.serializers import Add%sSerializer, Get%sSerializer

# Create your views here.

@api_view(["POST"])
def add_%s(request):
    """Function to add new %s details"""
    try:
        data = request.data
        serializer = Add%sSerializer(data=data)
        if serializer.is_valid():
%s
            data_exists = %sModel.objects.filter(
%s
                ).first()
            if data_exists:
                   return Response(
                       ResponseData.error("%s with these details already exists"),
                       status=status.HTTP_200_OK,
                   )
            new_%s = %sModel.objects.create(
%s
            )
            new_%s.save()
            return Response(
                ResponseData.success_without_data(
                    "%s added successfully"),
                status=status.HTTP_201_CREATED,
            )
        for error in serializer.errors:
            print(serializer.errors[error][0])
        return Response(
            ResponseData.error(serializer.errors[error][0]),
            status=status.HTTP_400_BAD_REQUEST,
        )
    except Exception as exception:
        return Response(
            ResponseData.error(str(exception)), status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(["POST"])
def get_%s_by_id(request):
    """Function to get a %s based on id"""
    try:
        data = request.data
        serializer = Get%sSerializer(data=data)
        if serializer.is_valid():
            %s_id = serializer.data["id"]
            is_id_valid = %sModel.objects.filter(id=%s_id).first()
            if not is_id_valid:
                   return Response(
                       ResponseData.error("%s id is invalid"),
                       status=status.HTTP_200_OK,
                   )
            %s_data = %sModel.objects.values().filter(id = %s_id).all()
            for i in range(0,len(%s_data)):
                %s_data[i].pop('created_at')
                %s_data[i].pop('updated_at')
            return Response(
                ResponseData.success(
                    %s_data, "%s details fetched successfully"),
                status=status.HTTP_201_CREATED)
        return Response(
                    ResponseData.error(serializer.errors),
                    status=status.HTTP_400_BAD_REQUEST,
                )
    except Exception as exception:
        return Response(
            ResponseData.error(str(exception)), status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(["POST"])
def get_all_%s(request):
    """Function to get all %s"""
    try:
        data = request.data
        serializer = Get%sSerializer(data=data)
        if serializer.is_valid():
                %s_details = list(
                %sModel.objects.values().filter())
                for i in range(0,len(%s_details)):
                    %s_details[i].pop('created_at')
                    %s_details[i].pop('updated_at')
                return Response(
                    ResponseData.success(
                        %s_details, "%s details fetched successfully"),
                    status=status.HTTP_201_CREATED)
        return Response(
                    ResponseData.error(serializer.errors),
                    status=status.HTTP_400_BAD_REQUEST,
                )
    except Exception as exception:
        return Response(
            ResponseData.error(str(exception)), status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(["POST"])
def delete_%s_by_id(request):
    """Function to delete a %s based on id"""
    try:
        data = request.data
        serializer = Get%sSerializer(data=data)
        if serializer.is_valid():
            %s_id = serializer.data["id"]
            is_id_valid = %sModel.objects.filter(id=%s_id).first()
            if not is_id_valid:
                   return Response(
                       ResponseData.error("%s id is invalid"),
                       status=status.HTTP_200_OK,
                   )
            %s_data = %sModel.objects.values().filter(id = %s_id).delete()
            return Response(
                ResponseData.success_without_data(
                    "%s of this id deleted successfully"),
                status=status.HTTP_201_CREATED)
        return Response(
                    ResponseData.error(serializer.errors),
                    status=status.HTTP_400_BAD_REQUEST,
                )
    except Exception as exception:
        return Response(
            ResponseData.error(str(exception)), status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(["POST"])
def delete_all_%s(request):
    """Function to delete all %s"""
    try:
        data = request.data
        serializer = Get%sSerializer(data=data)
        if serializer.is_valid():
            %s_data = %sModel.objects.values().filter().delete()
            return Response(
                ResponseData.success_without_data(
                    "All %s deleted successfully"),
                status=status.HTTP_201_CREATED)
        return Response(
                    ResponseData.error(serializer.errors),
                    status=status.HTTP_400_BAD_REQUEST,
                )
    except Exception as exception:
        return Response(
            ResponseData.error(str(exception)), status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(["POST"])
def update_%s(request):
    """Function to update %s details"""
    try:
        data = request.data
        serializer = Add%sSerializer(data=data)
        if serializer.is_valid():
%s
            %s_data = %sModel.objects.filter(
                id=%s_id
            ).first()
            if not %s_data:
                return Response(
                    ResponseData.error("%s id is invalid."),
                    status=status.HTTP_200_OK,
                )
            if 'image' in request.FILES:
                fs = FileSystemStorage(location='static/')
                fs.save(request.FILES['image'].name, request.FILES['image'])
%s
            #if 'image' in request.FILES:
            #   userdata.profile_pic = f"static/{request.FILES['image']}"
            %s_data.save()
            updated_data = list(
                %sModel.objects.values().filter(
                    id=%s_id)
            )
            return Response(
                ResponseData.success(
                    updated_data[0]['id'], "%s details updated successfully"),
                status=status.HTTP_201_CREATED,
            )
        return Response(
            ResponseData.error(serializer.errors),
            status=status.HTTP_400_BAD_REQUEST,
        )
    except KeyError as exception:
        return Response(
            ResponseData.error(str(exception)),
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

                  ''' %(classnameinsmall,mainClassName,classnameinsmall,mainClassName,mainClassName,
                  classnameinsmall,classnameinsmall,mainClassName,allObjects,mainClassName,filterForAdding,
                  mainClassName,classnameinsmall,mainClassName,filterForAdding,classnameinsmall,
                  mainClassName,classnameinsmall,classnameinsmall,mainClassName,classnameinsmall,
                  mainClassName,classnameinsmall,mainClassName,classnameinsmall,mainClassName,classnameinsmall,
                  classnameinsmall,classnameinsmall,classnameinsmall,classnameinsmall,mainClassName,
                  classnameinsmall,classnameinsmall,mainClassName,classnameinsmall,mainClassName,
                  classnameinsmall,classnameinsmall,classnameinsmall,classnameinsmall,mainClassName,
                  classnameinsmall,classnameinsmall,mainClassName,classnameinsmall,mainClassName,classnameinsmall,
                  classnameinsmall,classnameinsmall,mainClassName,classnameinsmall,mainClassName,
                  classnameinsmall,classnameinsmall,mainClassName,classnameinsmall,mainClassName,classnameinsmall,
                  classnameinsmall,classnameinsmall,mainClassName,allObjectsForUpdate,classnameinsmall,
                  mainClassName,classnameinsmall,classnameinsmall,mainClassName,filterForUpdating,classnameinsmall,
                  mainClassName,classnameinsmall,mainClassName
                  ))