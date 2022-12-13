import '../../domain/entities/add_countries_entity.dart';
import '../../domain/entities/add_countries_params_entity.dart';
import '../../domain/entities/get_countries_entity.dart';
import '../../domain/entities/get_countries_params_entity.dart';
import '../../domain/entities/update_countries_entity.dart';
import '../../domain/entities/update_countries_params_entity.dart';
import '../../domain/entities/delete_countries_entity.dart';
import '../../domain/entities/delete_countries_params_entity.dart';


abstract class CountriesNetworkSource {
Future<GetCountriesResponseEntity> getCountries(GetCountriesParamsEntity getCountriesParamsEntity);
Future<AddCountriesResponseEntity> addCountries(AddCountriesParamsEntity addCountriesParamsEntity);
Future<UpdateCountriesResponseEntity> updateCountries(UpdateCountriesParamsEntity updateCountriesParamsEntity);
Future<DeleteCountriesResponseEntity> deleteCountries(DeleteCountriesParamsEntity deleteCountriesParamsEntity);
}
