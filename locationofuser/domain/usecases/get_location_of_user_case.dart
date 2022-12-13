
import 'package:commdem_warriors/core/failure/failures.dart';
import 'package:commdem_warriors/core/usecases/usecase.dart';
import 'package:dartz/dartz.dart';
import '../../data/repositories/location_of_user_repository_imp.dart';
import '../entities/get_location_of_user_entity.dart';
import '../entities/get_location_of_user_params_entity.dart';

class GetLocationOfUserCase extends UseCase<GetLocationOfUserResponseEntity, GetLocationOfUserParamsEntity> {
  LocationOfUserRepositoryImp? locationofuserRepositoryImp;
  GetLocationOfUserCase(this.locationofuserRepositoryImp);
  @override
  Stream<Either<Failure, GetLocationOfUserResponseEntity>> call(
      GetLocationOfUserParamsEntity locationofuserParamsEntity) {
    return locationofuserRepositoryImp!.getLocationOfUser(locationofuserParamsEntity);
  }
}
                  