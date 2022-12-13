
import 'package:commdem_warriors/core/failure/failures.dart';
import 'package:commdem_warriors/core/usecases/usecase.dart';
import 'package:dartz/dartz.dart';
import '../../data/repositories/location_of_user_repository_imp.dart';
import '../entities/delete_location_of_user_entity.dart';
import '../entities/delete_location_of_user_params_entity.dart';

class DeleteLocationOfUserCase extends UseCase<DeleteLocationOfUserResponseEntity, DeleteLocationOfUserParamsEntity> {
  LocationOfUserRepositoryImp? locationofuserRepositoryImp;
  DeleteLocationOfUserCase(this.locationofuserRepositoryImp);
  @override
  Stream<Either<Failure, DeleteLocationOfUserResponseEntity>> call(
      DeleteLocationOfUserParamsEntity locationofuserParamsEntity) {
    return locationofuserRepositoryImp!.deleteLocationOfUser(locationofuserParamsEntity);
  }
}
                  