
import 'package:commdem_warriors/core/failure/failures.dart';
import 'package:commdem_warriors/core/usecases/usecase.dart';
import 'package:dartz/dartz.dart';
import '../../data/repositories/countries_repository_imp.dart';
import '../entities/delete_countries_entity.dart';
import '../entities/delete_countries_params_entity.dart';

class DeleteCountriesCase extends UseCase<DeleteCountriesResponseEntity, DeleteCountriesParamsEntity> {
  CountriesRepositoryImp? countriesRepositoryImp;
  DeleteCountriesCase(this.countriesRepositoryImp);
  @override
  Stream<Either<Failure, DeleteCountriesResponseEntity>> call(
      DeleteCountriesParamsEntity countriesParamsEntity) {
    return countriesRepositoryImp!.deleteCountries(countriesParamsEntity);
  }
}
                  