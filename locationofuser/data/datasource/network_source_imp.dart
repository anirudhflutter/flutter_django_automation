import 'package:commdem_warriors/core/utils/api_service/api_helper_dio.dart';
import '../../domain/entities/add_location_of_user_entity.dart';
import '../../domain/entities/add_location_of_user_params_entity.dart';
import '../../domain/entities/get_location_of_user_entity.dart';
import '../../domain/entities/get_location_of_user_params_entity.dart';
import '../../domain/entities/update_location_of_user_entity.dart';
import '../../domain/entities/update_location_of_user_params_entity.dart';
import '../../domain/entities/delete_location_of_user_entity.dart';
import '../../domain/entities/delete_location_of_user_params_entity.dart';
import '../models/add_location_of_user_model.dart';
import '../models/get_location_of_user_model.dart';
import '../models/delete_location_of_user_model.dart';
import '../models/update_location_of_user_model.dart';
import 'network_source.dart';


class LocationOfUserNetworkSourceImp extends LocationOfUserNetworkSource {

  @override
  Future<GetLocationOfUserResponseEntity> getLocationOfUser(GetLocationOfUserParamsEntity getLocationOfUserParamsEntity) async {
    var params = {
      'id' : getLocationOfUserParamsEntity.id,
    };
    var _responseFromApi;
    _responseFromApi = await ApiHelperDio().postDioMethod(
        endpoint:
        '/orders_app/get_order_details/',
        params: params,isInFormData: false);
    GetLocationOfUserResponseEntity _response = GetLocationOfUserResponseModel.fromMap(_responseFromApi);
    return _response;
  }
                        
  @override
  Future<AddLocationOfUserResponseEntity> addLocationOfUser(AddLocationOfUserParamsEntity addLocationOfUserParamsEntity) async {
    var params = {
      'id' : addLocationOfUserParamsEntity.id,
    };
    var _responseFromApi;
    _responseFromApi = await ApiHelperDio().postDioMethod(
        endpoint:
        '/orders_app/add_order_details/',
        params: params,isInFormData: false);
    AddLocationOfUserResponseEntity _response = AddLocationOfUserResponseModel.fromMap(_responseFromApi);
    return _response;
  }
                        
  @override
  Future<UpdateLocationOfUserResponseEntity> updateLocationOfUser(UpdateLocationOfUserParamsEntity updateLocationOfUserParamsEntity) async {
    var params = {
      'id' : updateLocationOfUserParamsEntity.id,
    };
    var _responseFromApi;
    _responseFromApi = await ApiHelperDio().postDioMethod(
        endpoint:
        '/orders_app/update_order_details/',
        params: params,isInFormData: false);
    UpdateLocationOfUserResponseEntity _response = UpdateLocationOfUserResponseModel.fromMap(_responseFromApi);
    return _response;
  }
                        
  @override
  Future<DeleteLocationOfUserResponseEntity> deleteLocationOfUser(DeleteLocationOfUserParamsEntity deleteLocationOfUserParamsEntity) async {
    var params = {
      'id' : deleteLocationOfUserParamsEntity.id,
    };
    var _responseFromApi;
    _responseFromApi = await ApiHelperDio().postDioMethod(
        endpoint:
        '/orders_app/delete_order_details/',
        params: params,isInFormData: false);
    DeleteLocationOfUserResponseEntity _response = DeleteLocationOfUserResponseModel.fromMap(_responseFromApi);
    return _response;
  }
                        
}