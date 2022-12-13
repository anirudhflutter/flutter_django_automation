import 'package:commdem_warriors/core/utils/api_service/api_helper_dio.dart';
import '../../domain/entities/add_countries_entity.dart';
import '../../domain/entities/add_countries_params_entity.dart';
import '../../domain/entities/get_countries_entity.dart';
import '../../domain/entities/get_countries_params_entity.dart';
import '../../domain/entities/update_countries_entity.dart';
import '../../domain/entities/update_countries_params_entity.dart';
import '../../domain/entities/delete_countries_entity.dart';
import '../../domain/entities/delete_countries_params_entity.dart';
import '../models/add_countries_model.dart';
import '../models/get_countries_model.dart';
import '../models/delete_countries_model.dart';
import '../models/update_countries_model.dart';
import 'network_source.dart';


class CountriesNetworkSourceImp extends CountriesNetworkSource {

  @override
  Future<GetCountriesResponseEntity> getCountries(GetCountriesParamsEntity getCountriesParamsEntity) async {
    var params = {
      'id' : getCountriesParamsEntity.id,
    };
    var _responseFromApi;
    _responseFromApi = await ApiHelperDio().postDioMethod(
        endpoint:
        '/orders_app/get_order_details/',
        params: params,isInFormData: false);
    GetCountriesResponseEntity _response = GetCountriesResponseModel.fromMap(_responseFromApi);
    return _response;
  }
                        
  @override
  Future<AddCountriesResponseEntity> addCountries(AddCountriesParamsEntity addCountriesParamsEntity) async {
    var params = {
      'id' : addCountriesParamsEntity.id,
    };
    var _responseFromApi;
    _responseFromApi = await ApiHelperDio().postDioMethod(
        endpoint:
        '/orders_app/add_order_details/',
        params: params,isInFormData: false);
    AddCountriesResponseEntity _response = AddCountriesResponseModel.fromMap(_responseFromApi);
    return _response;
  }
                        
  @override
  Future<UpdateCountriesResponseEntity> updateCountries(UpdateCountriesParamsEntity updateCountriesParamsEntity) async {
    var params = {
      'id' : updateCountriesParamsEntity.id,
    };
    var _responseFromApi;
    _responseFromApi = await ApiHelperDio().postDioMethod(
        endpoint:
        '/orders_app/update_order_details/',
        params: params,isInFormData: false);
    UpdateCountriesResponseEntity _response = UpdateCountriesResponseModel.fromMap(_responseFromApi);
    return _response;
  }
                        
  @override
  Future<DeleteCountriesResponseEntity> deleteCountries(DeleteCountriesParamsEntity deleteCountriesParamsEntity) async {
    var params = {
      'id' : deleteCountriesParamsEntity.id,
    };
    var _responseFromApi;
    _responseFromApi = await ApiHelperDio().postDioMethod(
        endpoint:
        '/orders_app/delete_order_details/',
        params: params,isInFormData: false);
    DeleteCountriesResponseEntity _response = DeleteCountriesResponseModel.fromMap(_responseFromApi);
    return _response;
  }
                        
}