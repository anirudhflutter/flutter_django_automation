
import 'package:commdem_warriors/core/failure/failures.dart';
import 'package:commdem_warriors/core/usecases/usecase.dart';
import 'package:dartz/dartz.dart';
import '../../data/repositories/location_of_user_repository_imp.dart';
import '../entities/add_location_of_user_entity.dart';
import '../entities/add_location_of_user_params_entity.dart';

class AddLocationOfUserCase extends UseCase<AddLocationOfUserResponseEntity, AddLocationOfUserParamsEntity> {
  LocationOfUserRepositoryImp? locationofuserRepositoryImp;
  AddLocationOfUserCase(this.locationofuserRepositoryImp);
  @override
  Stream<Either<Failure, AddLocationOfUserResponseEntity>> call(
      AddLocationOfUserParamsEntity locationofuserParamsEntity) {
    return locationofuserRepositoryImp!.addLocationOfUser(locationofuserParamsEntity);
  }
}
                  