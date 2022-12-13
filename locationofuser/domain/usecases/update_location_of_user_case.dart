
import 'package:commdem_warriors/core/failure/failures.dart';
import 'package:commdem_warriors/core/usecases/usecase.dart';
import 'package:dartz/dartz.dart';
import '../../data/repositories/location_of_user_repository_imp.dart';
import '../entities/update_location_of_user_entity.dart';
import '../entities/update_location_of_user_params_entity.dart';

class UpdateLocationOfUserCase extends UseCase<UpdateLocationOfUserResponseEntity, UpdateLocationOfUserParamsEntity> {
  LocationOfUserRepositoryImp? locationofuserRepositoryImp;
  UpdateLocationOfUserCase(this.locationofuserRepositoryImp);
  @override
  Stream<Either<Failure, UpdateLocationOfUserResponseEntity>> call(
      UpdateLocationOfUserParamsEntity locationofuserParamsEntity) {
    return locationofuserRepositoryImp!.updateLocationOfUser(locationofuserParamsEntity);
  }
}
                  