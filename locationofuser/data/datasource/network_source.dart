import '../../domain/entities/add_location_of_user_entity.dart';
import '../../domain/entities/add_location_of_user_params_entity.dart';
import '../../domain/entities/get_location_of_user_entity.dart';
import '../../domain/entities/get_location_of_user_params_entity.dart';
import '../../domain/entities/update_location_of_user_entity.dart';
import '../../domain/entities/update_location_of_user_params_entity.dart';
import '../../domain/entities/delete_location_of_user_entity.dart';
import '../../domain/entities/delete_location_of_user_params_entity.dart';


abstract class LocationOfUserNetworkSource {
Future<GetLocationOfUserResponseEntity> getLocationOfUser(GetLocationOfUserParamsEntity getLocationOfUserParamsEntity);
Future<AddLocationOfUserResponseEntity> addLocationOfUser(AddLocationOfUserParamsEntity addLocationOfUserParamsEntity);
Future<UpdateLocationOfUserResponseEntity> updateLocationOfUser(UpdateLocationOfUserParamsEntity updateLocationOfUserParamsEntity);
Future<DeleteLocationOfUserResponseEntity> deleteLocationOfUser(DeleteLocationOfUserParamsEntity deleteLocationOfUserParamsEntity);
}
