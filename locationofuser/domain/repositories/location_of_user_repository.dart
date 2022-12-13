import '../../../../core/failure/failures.dart';
import '../../domain/entities/add_location_of_user_entity.dart';
import '../../domain/entities/add_location_of_user_params_entity.dart';
import '../../domain/entities/get_location_of_user_entity.dart';
import '../../domain/entities/get_location_of_user_params_entity.dart';
import '../../domain/entities/update_location_of_user_entity.dart';
import '../../domain/entities/update_location_of_user_params_entity.dart';
import '../../domain/entities/delete_location_of_user_entity.dart';
import '../../domain/entities/delete_location_of_user_params_entity.dart';
import 'package:dartz/dartz.dart';


abstract class LocationOfUserRepository {
Stream<Either<Failure, GetLocationOfUserResponseEntity>> getLocationOfUser(GetLocationOfUserParamsEntity getLocationOfUserParamsEntity);
Stream<Either<Failure, AddLocationOfUserResponseEntity>> addLocationOfUser(AddLocationOfUserParamsEntity addLocationOfUserParamsEntity);
Stream<Either<Failure, UpdateLocationOfUserResponseEntity>> updateLocationOfUser(UpdateLocationOfUserParamsEntity updateLocationOfUserParamsEntity);
Stream<Either<Failure, DeleteLocationOfUserResponseEntity>> deleteLocationOfUser(DeleteLocationOfUserParamsEntity deleteLocationOfUserParamsEntity);
}
