
import 'package:commdem_warriors/core/failure/failures.dart';
import 'package:commdem_warriors/core/usecases/usecase.dart';
import 'package:dartz/dartz.dart';
import '../../data/repositories/countries_repository_imp.dart';
import '../entities/get_countries_entity.dart';
import '../entities/get_countries_params_entity.dart';

class GetCountriesCase extends UseCase<GetCountriesResponseEntity, GetCountriesParamsEntity> {
  CountriesRepositoryImp? countriesRepositoryImp;
  GetCountriesCase(this.countriesRepositoryImp);
  @override
  Stream<Either<Failure, GetCountriesResponseEntity>> call(
      GetCountriesParamsEntity countriesParamsEntity) {
    return countriesRepositoryImp!.getCountries(countriesParamsEntity);
  }
}
                  