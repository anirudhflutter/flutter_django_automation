import os
import re


jsonData =  {
    "data": [{
            "id": 452134,
            "country_id": 6,
            "country_code": "AD",
            "country_name": "Andorra"
        }],
    "success": True,
    "message": "Hospital created successfully"
}


mainlist = []
mainjsonkeyslist = []
mainClassName = 'Countries'
getApiEndPoint = '/orders_app/get_order_details/'
addApiEndPoint = '/orders_app/add_order_details/'
updateApiEndPoint = '/orders_app/update_order_details/'
deleteApiEndPoint = '/orders_app/delete_order_details/'

# Create folder directory first 
mainclassnameinsmall = str(mainClassName).lower()

# Directory
directory = mainclassnameinsmall
  
# Parent Directory path
path = os.path.join(mainclassnameinsmall)
os.mkdir(path)

my_list = re.findall('[a-zA-Z][^A-Z]*', mainClassName)
name = ""
for i in my_list:
    name+=f"_{str(i).lower()}"
name1 = ""
for i in my_list:
    name1+=f"{str(i).lower()}_"
name2 = ""
for i in range(0,len(my_list)):
    if(i != len(my_list) - 1):
       name2+=f"{str(my_list[i]).lower()}_"
    else:
      name2+=f"{str(my_list[i]).lower()}"

with open("/Users/apple/Downloads/flutter_tdd_automation/final_model.py", 'r+') as f:
    f.truncate(0)
with open("/Users/apple/Downloads/flutter_tdd_automation/entity.py", 'r+') as f:
    f.truncate(0)

def main(data):
    for key, value in dict(data).items():
       dictdata = {}
       dictdata[key] = type(value)
       mainlist.append(dictdata)
       mainjsonkeyslist.append(dictdata)

main(jsonData) 

def changevalueinflutterformat(listdata):
  for i in range(0,len(listdata)):
        if listdata[i] != "<class 'str'>":
         for key,value in dict(listdata[i]).items():
            if str(value) == "<class 'list'>":
              listdata[i][key] = 'List'
            if str(value) == "<class 'str'>":
              listdata[i][key] = 'String'
            if str(value) == "<class 'dict'>":
              listdata[i][key] = 'Map'
            if str(value) == "<class 'bool'>":
              listdata[i][key] = 'bool'
            if str(value) == "<class 'int'>":
              listdata[i][key] = 'int'
  return listdata

def classFunction(mainClassName,keys,keys1,json2,definevar,definevarEntity,jsons,entityname):
    with open('/Users/apple/Downloads/flutter_tdd_automation/final_model.py', 'a') as f:
           l1 = [
               "\n\n\nclass Get%sResponseModel extends Get%sResponseEntity {\n" % (mainClassName,mainClassName)
           ]
           l2 = [
               "  Get%sResponseModel({\n" % mainClassName
           ]
           l3 = [keys]
           l4 = [
               "  }) : super(\n"
           ]
           l5 = [keys1]
           l6 = [
               ');\n\n'
           ]
           l7 = [definevar + "\n"]
           l8 = [
               '  factory Get%sResponseModel.fromMap(Map<String, dynamic> json) =>\n' % (mainClassName),
               '      Get%sResponseModel(\n' % (mainClassName),
               jsons + "\n",
               '      );\n'
           ]
           l11 = [
            f"  factory Get{mainClassName}ResponseModel.fromJson(String str) =>\n",
            f"      Get{mainClassName}ResponseModel.fromMap(json.decode(str));\n\n"
           ]
           l10 = [
            "String toJson() => json.encode(toMap());\n\n",
           ]
           l9 = [
               '  Map<String, dynamic> toMap() => {\n',
               json2 + "\n",
               '      };\n\n',
               '}\n'
           ]
           f.writelines(l1)
           f.writelines(l2)
           f.writelines(l3)
           f.writelines(l4)
           f.writelines(l5)
           f.writelines(l6)
           f.writelines(l7)
           f.writelines(l8)
           f.writelines(l11)
           f.writelines(l10)
           f.writelines(l9)
    with open('/Users/apple/Downloads/flutter_tdd_automation/entity.py', 'a') as f:
           l1 = [
               "\n\n\nclass Get%sResponseEntity extends Equatable {\n" % (mainClassName)
           ]
           l2 = [
               "  Get%sResponseEntity({\n" % mainClassName
           ]
           l3 = [keys]
           l4 = [
               "  });\n"
           ]
           l7 = [definevarEntity + "\n"]
           l8 = [
            "  @override\n",
            "// TODO: implement props\n",
            f"  List<Object?> get props => [{entityname}];\n",
            "}\n\n"
           ]
           f.writelines(l1)
           f.writelines(l2)
           f.writelines(l3)
           f.writelines(l4)
           f.writelines(l7)
           f.writelines(l8)
    return mainClassName


def forNewClass(mainData,mainClassName):
  jsons = ""
  jsons1 = ""
  json2 = ""
  definevar = ""
  definevarEntity = ""
  entityname = ""
  keys = ''
  pastclassname = ''
  # mainData = changevalueinflutterformat(mainData)
  for i in range(0,len(mainData)):
   for key,value in mainData[i].items():  
      keys+= "    required this.%s,\n" %key
      entityname+=key + ","
      if str(value) == "<class 'list'>":
          definevar+= "  final Get%sResponseModel %s;\n" % (str(key).capitalize(),key)
          definevarEntity+= "  final Get%sResponseEntity %s;\n" % (str(key).capitalize(),key)
          pastclassname = key
      elif str(value) == "<class 'dict'>":
          jsons1+= "        %s : %s,\n" % (key,key)
          json2+= "        '%s' : %s.toMap(),\n" % (key,key)
          jsons+= "        %s: Get%sResponseModel.fromMap(json['%s']),\n" % (key,str(key).capitalize(),key)
          definevar+= "  final Get%sResponseModel %s;\n" % (str(key).capitalize(),key)
          definevarEntity+= "  final Get%sResponseEntity %s;\n" % (str(key).capitalize(),key)
          pastclassname = key
      elif str(value) == "<class 'bool'>":
          definevar+= "  final bool %s;\n" % (key)
          definevarEntity+= "  final bool %s;\n" % (key)
          jsons+= "        %s: json['%s'],\n" % (key,key)
          jsons1+= "        %s : %s,\n" % (key,key)
          json2+= "        '%s' : %s,\n" % (key,key)
      elif str(value) == "<class 'str'>":
          definevar+= "  final String %s;\n" % (key)
          definevarEntity+= "  final String %s;\n" % (key)
          jsons+= "        %s: json['%s'],\n" % (key,key)
          jsons1+= "        %s : %s,\n" % (key,key)
          json2+= "        '%s' : %s,\n" % (key,key)
      elif str(value) == "<class 'int'>":
          definevar+= "  final int %s;\n" % (key)
          definevarEntity+= "  final int %s;\n" % (key)
          jsons+= "        %s: json['%s'],\n" % (key,key)
          jsons1+= "        %s : %s,\n" % (key,key)
          json2+= "        '%s' : %s,\n" % (key,key)
      else:
          definevar+= "  final %s %s;\n" % (value,key)
          definevarEntity+= "  final %s %s;\n" % (value,key)
          jsons+= "        %s: json['%s'],\n" % (key,key)
          jsons1+= "        %s : %s,\n" % (key,key)
          json2+= "        '%s' : %s,\n" % (key,key)
  
  subclassname = classFunction(mainClassName,keys,jsons1,json2,definevar,definevarEntity,jsons,entityname)
  subclassname = pastclassname.capitalize()
  return subclassname

def add_data_to_main_list(inputdata,inputdatacopy): 
    for key, value in dict(inputdata).items():
        dictdata = {}
        dictdata[key] = type(value)
        for key1, value1 in dict(inputdatacopy).items():
          dictdata1 = {}
          dictdata1[key1] = type(value1)
          if str(type(value1)) == "<class 'str'>" or str(type(value1)) == "<class 'int'>":
              if not mainlist.__contains__(dictdata1):
               mainlist.append(dictdata1)       
        if str(type(value)) == "<class 'dict'>":
           mainlist.append(dictdata)
        if str(type(value)) == "<class 'list'>":
           mainlist.append(dictdata)
    
    return mainlist,inputdata      
               
def sub_function(inputdata,data):
     parentdata = {}
     for key,value in inputdata.items():
            if str(type(data[key])) == "<class 'dict'>":
               mainlist,parentdata = add_data_to_main_list(data[key],data[key])
            elif str(type(data[key])) == "<class 'list'>":
               if len(data[key]) > 0:
                     if str(type(data[key][0])) == "<class 'str'>":
                          mainlist.append("<class 'str'>")
                     else:
                          add_data_to_main_list(data[key][0])
            else:
              mainlist.append(data[key])
     return mainlist,parentdata

def verymainfunction(maindatatypelist,actualdatalist,classname):
  for i in range(0,len(maindatatypelist)):
    for key,value in dict(maindatatypelist[i]).items():
       if str(value) == "<class 'dict'>":
          print(f"sdvdvvdvsv {maindatatypelist}")
          finalMainList,parentdata = sub_function(maindatatypelist[i],actualdatalist)
          print("-----------------maindatatypelist-------------------\n")
          print(maindatatypelist)
          print("-----------------parentdata-----------------\n")
          print(parentdata)
          print("-----------------finalMainListbefore remove-----------------\n")
          print(finalMainList)
          if len(finalMainList) == len(maindatatypelist):
            for j in range(0,len(finalMainList)):
                dictpresent = False
                for key1,value1 in finalMainList[j].items():
                  if str(value1) == "<class 'dict'>":
                     dictpresent = True
                     x = []
                     for k in range(j+1,len(finalMainList)):
                        x.append(maindatatypelist[k])
                     finalMainList = x
                     break
                if dictpresent:
                  break
                  # finalMainList.remove(maindatatypelist[j])
          else:
              for j in range(0,len(maindatatypelist)):
                for key1,value1 in maindatatypelist[j].items():
                   if str(value1) == "<class 'dict'>" and j!=0:
                      break
                   if finalMainList.__contains__(maindatatypelist[j]):
                      finalMainList.remove(maindatatypelist[j])
          #         maindatatypelist.remove(maindatatypelist[j])
          # for k in range(0,len(finalMainList)):
          #   for key,value in dict(finalMainList[k]).items():
          #     if str(value) == "<class 'str'>":
          #       finalMainList.remove(finalMainList[k])
          #     else:
          #       break
          # finaldata = changevalueinflutterformat(finalMainList)
          print("finalMainList after")
          print(finalMainList)
          subclassname = forNewClass(finalMainList,classname)
          mapexists = False
          for key1,value1 in parentdata.items():
            if str(type(value1)) == "<class 'dict'>":
              mapexists = True
              break
          if mapexists:
             print("functiom called again")
             print("finalMainList")
             print(finalMainList)
             maindatatypelist = finalMainList
             verymainfunction(maindatatypelist,parentdata,subclassname)


subclassname = forNewClass(mainjsonkeyslist,mainClassName)          
verymainfunction(mainjsonkeyslist,jsonData,subclassname)

list = ['data', 'domain', 'presentation']
index = 0  
for items in list:
    path1 = os.path.join(path, items)
    os.mkdir(path1)
    if index == 0:
        sublist1 = ['datasource','models','repositories']
        for subitems in sublist1:
          path2 = os.path.join(path1, subitems)
          os.mkdir(path2)
          if(subitems == 'datasource'):
                file_name = '/network_source.dart'
                file_name1 = '/network_source_imp.dart'
                with open(path2+file_name, 'w') as f:
                      l1 = [
                          f"import '../../domain/entities/add{name}_entity.dart';\n",
                          f"import '../../domain/entities/add{name}_params_entity.dart';\n",
                          f"import '../../domain/entities/get{name}_entity.dart';\n",
                          f"import '../../domain/entities/get{name}_params_entity.dart';\n",
                          f"import '../../domain/entities/update{name}_entity.dart';\n",
                          f"import '../../domain/entities/update{name}_params_entity.dart';\n",
                          f"import '../../domain/entities/delete{name}_entity.dart';\n",
                          f"import '../../domain/entities/delete{name}_params_entity.dart';\n\n\n",
                      ]
                      l2 = [
                          "abstract class %sNetworkSource {\n" % (mainClassName),
                          "Future<Get%sResponseEntity> get%s(Get%sParamsEntity get%sParamsEntity);\n" % (mainClassName,mainClassName,mainClassName,mainClassName),
                          "Future<Add%sResponseEntity> add%s(Add%sParamsEntity add%sParamsEntity);\n" % (mainClassName,mainClassName,mainClassName,mainClassName),
                          "Future<Update%sResponseEntity> update%s(Update%sParamsEntity update%sParamsEntity);\n" % (mainClassName,mainClassName,mainClassName,mainClassName),
                          "Future<Delete%sResponseEntity> delete%s(Delete%sParamsEntity delete%sParamsEntity);\n" % (mainClassName,mainClassName,mainClassName,mainClassName),
                          "}\n"
                      ]
                      f.writelines(l1)
                      f.writelines(l2)
                with open(path2+file_name1, 'w') as fp:
                      l1 = [
                         "import 'package:commdem_warriors/core/utils/api_service/api_helper_dio.dart';\n",
                          f"import '../../domain/entities/add{name}_entity.dart';\n",
                          f"import '../../domain/entities/add{name}_params_entity.dart';\n",
                          f"import '../../domain/entities/get{name}_entity.dart';\n",
                          f"import '../../domain/entities/get{name}_params_entity.dart';\n",
                          f"import '../../domain/entities/update{name}_entity.dart';\n",
                          f"import '../../domain/entities/update{name}_params_entity.dart';\n",
                          f"import '../../domain/entities/delete{name}_entity.dart';\n",
                          f"import '../../domain/entities/delete{name}_params_entity.dart';\n",
                          f"import '../models/add{name}_model.dart';\n",
                          f"import '../models/get{name}_model.dart';\n",
                          f"import '../models/delete{name}_model.dart';\n",
                          f"import '../models/update{name}_model.dart';\n",
                          "import 'network_source.dart';\n\n\n"
                      ]
                      l2 = [
                        "class %sNetworkSourceImp extends %sNetworkSource {\n" %(mainClassName,mainClassName)
                      ]
                      for i in range(0,4):
                        sub_name = ""
                        api=""
                        if i==0:
                          sub_name = 'get'
                          api = getApiEndPoint
                        if i==1:
                          sub_name = 'add'
                          api = addApiEndPoint
                        if i==2:
                          sub_name = 'update'
                          api = updateApiEndPoint
                        if i==3:
                          sub_name = 'delete'
                          api = deleteApiEndPoint
                        l2.append("""
  @override
  Future<%s%sResponseEntity> %s%s(%s%sParamsEntity %s%sParamsEntity) async {
    var params = {
      'id' : %s%sParamsEntity.id,
    };
    var _responseFromApi;
    _responseFromApi = await ApiHelperDio().postDioMethod(
        endpoint:
        '%s',
        params: params,isInFormData: false);
    %s%sResponseEntity _response = %s%sResponseModel.fromMap(_responseFromApi);
    return _response;
  }
                        """ %(str(sub_name).capitalize(),mainClassName,sub_name,mainClassName,str(sub_name).capitalize(),mainClassName,sub_name,mainClassName,sub_name,mainClassName,api,str(sub_name).capitalize(),mainClassName,str(sub_name).capitalize(),mainClassName)
                        )
                      fp.writelines(l1)
                      l2.append(
                        "\n}"
                      )
                      fp.writelines(l2)
          if(subitems == 'models'):
                file_name = f"/add{name}_model.dart"
                file_name1 = f"/get{name}_model.dart"
                with open(path2+file_name, 'w') as fp:
                      l1 = [
                          "import 'dart:convert';\n",
                          f"import '../../domain/entities/add{name}_entity.dart';\n\n\n",
                      ]
                      l2 = [
                          "class Add%sResponseModel extends Add%sResponseEntity {\n" %(mainClassName,mainClassName),
                          "  Add%sResponseModel({\n" %(mainClassName),
                          "    required this.success,\n",
                          "    required this.message,\n",
                          "  }) : super(success: success, message: message);\n\n",
                          "  bool success;\n",
                          "  String message;\n",
                          f"  factory Add{mainClassName}ResponseModel.fromJson(String str) =>\n",
                          f"      Add{mainClassName}ResponseModel.fromMap(json.decode(str));\n\n",
                          "  String toJson() => json.encode(toMap());",
                          f"  factory Add{mainClassName}ResponseModel.fromMap(Map<String, dynamic> json) =>\n",
                          f"      Add{mainClassName}ResponseModel(\n",
                          f"        success: json['success'],\n",
                          f"        message: json['message'],\n",
                          "        );\n",
                          "  Map<String, dynamic> toMap() => {\n",
                          "    'success': success,\n",
                          "    'message': message,\n",
                          "  };\n\n",
                          "}\n"

                      ]
                      fp.writelines(l1)
                      fp.writelines(l2)
                with open("/Users/apple/Downloads/flutter_tdd_automation/final_model.py") as f1:
                      l1 = [
                          "import 'dart:convert';\n",
                          f"import '../../domain/entities/get{name}_entity.dart';\n\n\n",
                      ]
                      with open(path2+file_name1, 'w') as fp1:
                          fp1.writelines(l1)
                          for line in f1:
                              fp1.write(line)
                file_name = f"/update{name}_model.dart"
                file_name1 = f"/delete{name}_model.dart"
                with open(path2+file_name, 'w') as fp:
                      l1 = [
                          "import 'dart:convert';\n",
                          f"import '../../domain/entities/update{name}_entity.dart';\n\n\n",
                      ]
                      l2 = [
                          "class Update%sResponseModel extends Update%sResponseEntity {\n" %(mainClassName,mainClassName),
                          "  Update%sResponseModel({\n" %(mainClassName),
                          "    required this.success,\n",
                          "    required this.message,\n",
                          "  }) : super(success: success, message: message);\n\n",
                          "  bool success;\n",
                          "  String message;\n",
                          f"  factory Update{mainClassName}ResponseModel.fromJson(String str) =>\n",
                          f"      Update{mainClassName}ResponseModel.fromMap(json.decode(str));\n\n",
                          "  String toJson() => json.encode(toMap());",
                          f"  factory Update{mainClassName}ResponseModel.fromMap(Map<String, dynamic> json) =>\n",
                          f"      Update{mainClassName}ResponseModel(\n",
                          f"        success: json['success'],\n",
                          f"        message: json['message'],\n",
                          "        );\n",
                          "  Map<String, dynamic> toMap() => {\n",
                          "    'success': success,\n",
                          "    'message': message,\n",
                          "  };\n\n",
                          "}\n"
                      ]
                      fp.writelines(l1)
                      fp.writelines(l2)
                with open(path2+file_name1, 'w') as fp:
                      l1 = [
                          "import 'dart:convert';\n",
                          f"import '../../domain/entities/delete{name}_entity.dart';\n\n\n",
                      ]
                      l2 = [
                          "class Delete%sResponseModel extends Delete%sResponseEntity {\n" %(mainClassName,mainClassName),
                          "  Delete%sResponseModel({\n" %(mainClassName),
                          "    required this.success,\n",
                          "    required this.message,\n",
                          "  }) : super(success: success, message: message);\n\n",
                          "  bool success;\n",
                          "  String message;\n",
                          f"  factory Delete{mainClassName}ResponseModel.fromJson(String str) =>\n",
                          f"      Delete{mainClassName}ResponseModel.fromMap(json.decode(str));\n\n",
                          "  String toJson() => json.encode(toMap());",
                          f"  factory Delete{mainClassName}ResponseModel.fromMap(Map<String, dynamic> json) =>\n",
                          f"      Delete{mainClassName}ResponseModel(\n",
                          f"        success: json['success'],\n",
                          f"        message: json['message'],\n",
                          "        );\n",
                          "  Map<String, dynamic> toMap() => {\n",
                          "    'success': success,\n",
                          "    'message': message,\n",
                          "  };\n\n",
                          "}\n"
                      ]
                      fp.writelines(l1)
                      fp.writelines(l2)
          if(subitems == 'repositories'):
                file_name = f"/{name1}repository_imp.dart"
                with open(path2+file_name, 'w') as fp:
                      l1 = [
                         "import 'package:commdem_warriors/core/failure/failures.dart';\n",
                         "import 'package:dartz/dartz.dart';\n",
                         "import 'package:flutter/foundation.dart';\n",
                         "import '../datasource/network_source_imp.dart';\n"
                         f"import '../../domain/repositories/{name1}repository.dart';\n",
                          f"import '../../domain/entities/add{name}_entity.dart';\n",
                          f"import '../../domain/entities/add{name}_params_entity.dart';\n",
                          f"import '../../domain/entities/get{name}_entity.dart';\n",
                          f"import '../../domain/entities/get{name}_params_entity.dart';\n",
                          f"import '../../domain/entities/update{name}_entity.dart';\n",
                          f"import '../../domain/entities/update{name}_params_entity.dart';\n",
                          f"import '../../domain/entities/delete{name}_entity.dart';\n",
                          f"import '../../domain/entities/delete{name}_params_entity.dart';\n\n\n",
                      ]
                      l2 = [
                        "class %sRepositoryImp extends %sRepository {\n" %(mainClassName,mainClassName),
                        f"  final {mainClassName}NetworkSourceImp _{str(mainClassName).lower()}NetworkSourceImp;\n",
                        f"  {mainClassName}RepositoryImp(this._{str(mainClassName).lower()}NetworkSourceImp);\n"
                      ]
                      for i in range(0,4):
                        sub_name = ""
                        api=""
                        if i==0:
                          sub_name = 'get'
                          api = getApiEndPoint
                        if i==1:
                          sub_name = 'add'
                          api = addApiEndPoint
                        if i==2:
                          sub_name = 'update'
                          api = updateApiEndPoint
                        if i==3:
                          sub_name = 'delete'
                          api = deleteApiEndPoint
                        l2.append("""
  @override
  Stream<Either<Failure, %s%sResponseEntity>> %s%s(
      %s%sParamsEntity %sParamsEntity) async* {
    try {
      %s%sResponseEntity responseFromNetwork =
          await _%sNetworkSourceImp.%s%s(%sParamsEntity);
      if (kDebugMode) {
        print("_responseFromNetwork");
      }
      yield Right(responseFromNetwork);
    } on Failure catch (failure) {
      if (kDebugMode) {
        print("failure $failure");
      }
      yield Left(failure);
    } catch (e) {
      if (kDebugMode) {
        print("e $e");
      }
      yield Left(FailureMessage());
    }
  }
                        """ %(str(sub_name).capitalize(),mainClassName,sub_name,mainClassName,str(sub_name).capitalize(),mainClassName,str(mainClassName).lower(),str(sub_name).capitalize(),mainClassName,str(mainClassName).lower(),sub_name,mainClassName,str(mainClassName).lower())
                        )
                      fp.writelines(l1)
                      l2.append(
                        "\n}"
                      )
                      fp.writelines(l2)
    if index == 1:
        sublist2 = ['entities','repositories','usecases']
        for subitems in sublist2:
          path3 = os.path.join(path1, subitems)
          os.mkdir(path3)
          if(subitems == 'entities'):
                file_name = f"/add{name}_entity.dart"
                file_name1 = f"/add{name}_params_entity.dart"
                with open(path3+file_name, 'w') as fp:
                  fp.write("""
import 'package:equatable/equatable.dart';

class Add%sResponseEntity extends Equatable{
  Add%sResponseEntity({
    required this.success,
    required this.message,
  });

  final bool success;
  final String message;

  @override
  // TODO: implement props
  List<Object?> get props => [success,message];
}
                  """ %(mainClassName,mainClassName))
                with open(path3+file_name1, 'w') as fp:
                  fp.write("""
import 'dart:io';

class Add%sParamsEntity {
  Add%sParamsEntity({
    required this.id,
  });

  final String id;
}

                  """ %(mainClassName,mainClassName))
                file_name = f"/get{name}_entity.dart"
                file_name1 = f"/get{name}_params_entity.dart"
                with open("/Users/apple/Downloads/flutter_tdd_automation/entity.py") as f1:
                      l1 = [
                          "import 'package:equatable/equatable.dart';\n",
                          f"import '../../domain/entities/get{name}_entity.dart';\n\n\n",

                      ]
                      with open(path3+file_name, 'w') as fp1:
                          fp1.writelines(l1)
                          for line in f1:
                              fp1.write(line)
                with open(path3+file_name1, 'w') as fp:
                  fp.write("""
import 'dart:io';

class Get%sParamsEntity {
  Get%sParamsEntity({ 
    required this.id,
  });

  final String id;
}

                  """ %(mainClassName,mainClassName))
                file_name = f"/update{name}_entity.dart"
                file_name1 = f"/update{name}_params_entity.dart"
                with open(path3+file_name, 'w') as fp:
                  fp.write("""
import 'package:equatable/equatable.dart';

class Update%sResponseEntity extends Equatable{
  Update%sResponseEntity({
    required this.success,
    required this.message,
  });

  final bool success;
  final String message;

  @override
  // TODO: implement props
  List<Object?> get props => [success,message];
}
                  """ %(mainClassName,mainClassName))
                with open(path3+file_name1, 'w') as fp:
                  fp.write("""
import 'dart:io';

class Update%sParamsEntity {
  Update%sParamsEntity({
    required this.id,
  });

  final String id;
}

                  """ %(mainClassName,mainClassName))
                file_name = f"/delete{name}_entity.dart"
                file_name1 = f"/delete{name}_params_entity.dart"
                with open(path3+file_name, 'w') as fp:
                  fp.write("""
import 'package:equatable/equatable.dart';

class Delete%sResponseEntity extends Equatable{
  Delete%sResponseEntity({
    required this.success,
    required this.message,
  });

  final bool success;
  final String message;

  @override
  // TODO: implement props
  List<Object?> get props => [success,message];
}
                  """ %(mainClassName,mainClassName))
                with open(path3+file_name1, 'w') as fp:
                  fp.write("""
import 'dart:io';

class Delete%sParamsEntity {
  Delete%sParamsEntity({
    required this.id,
  });

  final String id;
}

                  """ %(mainClassName,mainClassName))
          if(subitems == 'repositories'):
                file_name = f"/{name1}repository.dart"
                with open(path3+file_name, 'w') as fp:
                      l1 = [
                        f"import '../../../../core/failure/failures.dart';\n",
                          f"import '../../domain/entities/add{name}_entity.dart';\n",
                          f"import '../../domain/entities/add{name}_params_entity.dart';\n",
                          f"import '../../domain/entities/get{name}_entity.dart';\n",
                          f"import '../../domain/entities/get{name}_params_entity.dart';\n",
                          f"import '../../domain/entities/update{name}_entity.dart';\n",
                          f"import '../../domain/entities/update{name}_params_entity.dart';\n",
                          f"import '../../domain/entities/delete{name}_entity.dart';\n",
                          f"import '../../domain/entities/delete{name}_params_entity.dart';\n",
                          "import 'package:dartz/dartz.dart';\n\n\n",
                      ]
                      l2 = [
                          "abstract class %sRepository {\n" % (mainClassName),
                          "Stream<Either<Failure, Get%sResponseEntity>> get%s(Get%sParamsEntity get%sParamsEntity);\n" % (mainClassName,mainClassName,mainClassName,mainClassName),
                          "Stream<Either<Failure, Add%sResponseEntity>> add%s(Add%sParamsEntity add%sParamsEntity);\n" % (mainClassName,mainClassName,mainClassName,mainClassName),
                          "Stream<Either<Failure, Update%sResponseEntity>> update%s(Update%sParamsEntity update%sParamsEntity);\n" % (mainClassName,mainClassName,mainClassName,mainClassName),
                          "Stream<Either<Failure, Delete%sResponseEntity>> delete%s(Delete%sParamsEntity delete%sParamsEntity);\n" % (mainClassName,mainClassName,mainClassName,mainClassName),
                          "}\n"
                      ]
                      fp.writelines(l1)
                      fp.writelines(l2)
          if(subitems == 'usecases'):
                file_name = f"/add{name}_case.dart"
                file_name1 = f"/get{name}_case.dart"
                with open(path3+file_name, 'w') as fp:
                  fp.write("""
import 'package:commdem_warriors/core/failure/failures.dart';
import 'package:commdem_warriors/core/usecases/usecase.dart';
import 'package:dartz/dartz.dart';
import '../../data/repositories/%s_repository_imp.dart';
import '../entities/add%s_entity.dart';
import '../entities/add%s_params_entity.dart';

class Add%sCase extends UseCase<Add%sResponseEntity, Add%sParamsEntity> {
  %sRepositoryImp? %sRepositoryImp;
  Add%sCase(this.%sRepositoryImp);
  @override
  Stream<Either<Failure, Add%sResponseEntity>> call(
      Add%sParamsEntity %sParamsEntity) {
    return %sRepositoryImp!.add%s(%sParamsEntity);
  }
}
                  """ %(name2,name,name,mainClassName,mainClassName,mainClassName,mainClassName,str(mainClassName).lower(),mainClassName,str(mainClassName).lower(),mainClassName,mainClassName,str(mainClassName).lower(),str(mainClassName).lower(),mainClassName,str(mainClassName).lower()))
                with open(path3+file_name1, 'w') as fp:
                  fp.write("""
import 'package:commdem_warriors/core/failure/failures.dart';
import 'package:commdem_warriors/core/usecases/usecase.dart';
import 'package:dartz/dartz.dart';
import '../../data/repositories/%s_repository_imp.dart';
import '../entities/get%s_entity.dart';
import '../entities/get%s_params_entity.dart';

class Get%sCase extends UseCase<Get%sResponseEntity, Get%sParamsEntity> {
  %sRepositoryImp? %sRepositoryImp;
  Get%sCase(this.%sRepositoryImp);
  @override
  Stream<Either<Failure, Get%sResponseEntity>> call(
      Get%sParamsEntity %sParamsEntity) {
    return %sRepositoryImp!.get%s(%sParamsEntity);
  }
}
                  """ %(name2,name,name,mainClassName,mainClassName,mainClassName,mainClassName,str(mainClassName).lower(),mainClassName,str(mainClassName).lower(),mainClassName,mainClassName,str(mainClassName).lower(),str(mainClassName).lower(),mainClassName,str(mainClassName).lower()))
                file_name = f"/update{name}_case.dart"
                file_name1 = f"/delete{name}_case.dart"
                with open(path3+file_name, 'w') as fp:
                  fp.write("""
import 'package:commdem_warriors/core/failure/failures.dart';
import 'package:commdem_warriors/core/usecases/usecase.dart';
import 'package:dartz/dartz.dart';
import '../../data/repositories/%s_repository_imp.dart';
import '../entities/update%s_entity.dart';
import '../entities/update%s_params_entity.dart';

class Update%sCase extends UseCase<Update%sResponseEntity, Update%sParamsEntity> {
  %sRepositoryImp? %sRepositoryImp;
  Update%sCase(this.%sRepositoryImp);
  @override
  Stream<Either<Failure, Update%sResponseEntity>> call(
      Update%sParamsEntity %sParamsEntity) {
    return %sRepositoryImp!.update%s(%sParamsEntity);
  }
}
                  """ %(name2,name,name,mainClassName,mainClassName,mainClassName,mainClassName,str(mainClassName).lower(),mainClassName,str(mainClassName).lower(),mainClassName,mainClassName,str(mainClassName).lower(),str(mainClassName).lower(),mainClassName,str(mainClassName).lower()))
                with open(path3+file_name1, 'w') as fp:
                  fp.write("""
import 'package:commdem_warriors/core/failure/failures.dart';
import 'package:commdem_warriors/core/usecases/usecase.dart';
import 'package:dartz/dartz.dart';
import '../../data/repositories/%s_repository_imp.dart';
import '../entities/delete%s_entity.dart';
import '../entities/delete%s_params_entity.dart';

class Delete%sCase extends UseCase<Delete%sResponseEntity, Delete%sParamsEntity> {
  %sRepositoryImp? %sRepositoryImp;
  Delete%sCase(this.%sRepositoryImp);
  @override
  Stream<Either<Failure, Delete%sResponseEntity>> call(
      Delete%sParamsEntity %sParamsEntity) {
    return %sRepositoryImp!.delete%s(%sParamsEntity);
  }
}
                  """ %(name2,name,name,mainClassName,mainClassName,mainClassName,mainClassName,str(mainClassName).lower(),mainClassName,str(mainClassName).lower(),mainClassName,mainClassName,str(mainClassName).lower(),str(mainClassName).lower(),mainClassName,str(mainClassName).lower()))
    if index == 2:
        sublist3 = ['cubit','pages']
        for subitems in sublist3:
          path4 = os.path.join(path1, subitems)
          os.mkdir(path4)
          if(subitems == 'cubit'):
                file_name = f"/{name1}cubit.dart"
                file_name1 = f"/{name1}state.dart"
                with open(path4+file_name, 'w') as fp:
                  l1 = [
                          "import 'package:flutter/material.dart';\n",
                          "import 'package:flutter_bloc/flutter_bloc.dart';\n",
                          "import '../../../../core/helpers/base/base_state.dart';\n",
                          f"import '../../domain/entities/add{name}_params_entity.dart';\n",
                          f"import '../../domain/entities/get{name}_params_entity.dart';\n",
                          f"import '../../domain/entities/update{name}_params_entity.dart';\n",
                          f"import '../../domain/entities/delete{name}_params_entity.dart';\n",
                          f"import '../../domain/usecases/add{name}_case.dart';\n",
                          f"import '../../domain/usecases/get{name}_case.dart';\n",
                          f"import '../../domain/usecases/update{name}_case.dart';\n",
                          f"import '../../domain/usecases/delete{name}_case.dart';\n",
                          f"import '{name1}state.dart';\n\n",
                      ]
                  fp.writelines(l1)
                  fp.write("""

class %sCubit extends Cubit<BaseState> {

  Get%sCase get%sCase;
  Add%sCase add%sCase;
  Update%sCase update%sCase;
  Delete%sCase delete%sCase;
  
  %sCubit(this.get%sCase,this.add%sCase,this.update%sCase,this.delete%sCase) : super(StateLoading());

    Future add%s({required Add%sParamsEntity add%sParamsEntity,required BuildContext context}) async {
    add%sCase.call(add%sParamsEntity).listen((event) {
      event.fold((fail) {
        print('add%s fail in cubit ${fail.toString()}');
        emit(%sFailState(errorMessage: fail.toString()));
      }, (success) {
        print('add%s success in cubit  $success');
        emit(Add%sSuccessState(successResponse: success));
      });
    });
  }

  Future get%s({required Get%sParamsEntity get%sParamsEntity,required BuildContext context}) async {
    get%sCase.call(get%sParamsEntity).listen((event) {
      event.fold((fail) {
        print('get%s fail in cubit ${fail.toString()}');
        emit(%sFailState(errorMessage: fail.toString()));
      }, (success) {
        print('get%s success in cubit  $success');
        emit(Get%sSuccessState(successResponse: success));
      });
    });
  }

  Future update%s({required Update%sParamsEntity update%sParamsEntity,required BuildContext context}) async {
    update%sCase.call(update%sParamsEntity).listen((event) {
      event.fold((fail) {
        print('update%s fail in cubit ${fail.toString()}');
        emit(%sFailState(errorMessage: fail.toString()));
      }, (success) {
        print('update%s success in cubit  $success');
        emit(Update%sSuccessState(successResponse: success));
      });
    });
  }

    Future delete%s({required Delete%sParamsEntity delete%sParamsEntity,required BuildContext context}) async {
    delete%sCase.call(delete%sParamsEntity).listen((event) {
      event.fold((fail) {
        print('delete%s fail in cubit ${fail.toString()}');
        emit(%sFailState(errorMessage: fail.toString()));
      }, (success) {
        print('delete%s success in cubit  $success');
        emit(Delete%sSuccessState(successResponse: success));
      });
    });
  }

}  

                  """ %(mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName))
                with open(path4+file_name1, 'w') as fp:
                  l1 = [
                          "import '../../../../core/helpers/base/base_state.dart';\n",
                          f"import '../../domain/entities/add{name}_entity.dart';\n",
                          f"import '../../domain/entities/get{name}_entity.dart';\n",
                          f"import '../../domain/entities/update{name}_entity.dart';\n",
                          f"import '../../domain/entities/delete{name}_entity.dart';\n",
                      ]
                  fp.writelines(l1)
                  fp.write("""

class %sFailState extends BaseState {
  String errorMessage;

  %sFailState({required this.errorMessage});

  @override
  // TODO: implement props
  List<Object?> get props => [errorMessage];
}


class Get%sSuccessState extends BaseState {
  Get%sResponseEntity successResponse;

  Get%sSuccessState({required this.successResponse});

  @override
  // TODO: implement props
  List<Object?> get props => [successResponse];
}

class Add%sSuccessState extends BaseState {
  Add%sResponseEntity successResponse;

  Add%sSuccessState({required this.successResponse});

  @override
  // TODO: implement props
  List<Object?> get props => [successResponse];
}

class Update%sSuccessState extends BaseState {
  Update%sResponseEntity successResponse;

  Update%sSuccessState({required this.successResponse});

  @override
  // TODO: implement props
  List<Object?> get props => [successResponse];
}

class Delete%sSuccessState extends BaseState {
  Delete%sResponseEntity successResponse;

  Delete%sSuccessState({required this.successResponse});

  @override
  // TODO: implement props
  List<Object?> get props => [successResponse];
}


                  """ %(mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,mainClassName,))
    index+=1
    


