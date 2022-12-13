
import 'package:commdem_warriors/core/failure/failures.dart';
import 'package:commdem_warriors/core/usecases/usecase.dart';
import 'package:dartz/dartz.dart';
import '../../data/repositories/countries_repository_imp.dart';
import '../entities/update_countries_entity.dart';
import '../entities/update_countries_params_entity.dart';

class UpdateCountriesCase extends UseCase<UpdateCountriesResponseEntity, UpdateCountriesParamsEntity> {
  CountriesRepositoryImp? countriesRepositoryImp;
  UpdateCountriesCase(this.countriesRepositoryImp);
  @override
  Stream<Either<Failure, UpdateCountriesResponseEntity>> call(
      UpdateCountriesParamsEntity countriesParamsEntity) {
    return countriesRepositoryImp!.updateCountries(countriesParamsEntity);
  }
}
                  