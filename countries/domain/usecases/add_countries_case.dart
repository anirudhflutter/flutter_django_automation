
import 'package:commdem_warriors/core/failure/failures.dart';
import 'package:commdem_warriors/core/usecases/usecase.dart';
import 'package:dartz/dartz.dart';
import '../../data/repositories/countries_repository_imp.dart';
import '../entities/add_countries_entity.dart';
import '../entities/add_countries_params_entity.dart';

class AddCountriesCase extends UseCase<AddCountriesResponseEntity, AddCountriesParamsEntity> {
  CountriesRepositoryImp? countriesRepositoryImp;
  AddCountriesCase(this.countriesRepositoryImp);
  @override
  Stream<Either<Failure, AddCountriesResponseEntity>> call(
      AddCountriesParamsEntity countriesParamsEntity) {
    return countriesRepositoryImp!.addCountries(countriesParamsEntity);
  }
}
                  