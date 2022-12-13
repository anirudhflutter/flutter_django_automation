import '../../../../core/failure/failures.dart';
import '../../domain/entities/add_countries_entity.dart';
import '../../domain/entities/add_countries_params_entity.dart';
import '../../domain/entities/get_countries_entity.dart';
import '../../domain/entities/get_countries_params_entity.dart';
import '../../domain/entities/update_countries_entity.dart';
import '../../domain/entities/update_countries_params_entity.dart';
import '../../domain/entities/delete_countries_entity.dart';
import '../../domain/entities/delete_countries_params_entity.dart';
import 'package:dartz/dartz.dart';


abstract class CountriesRepository {
Stream<Either<Failure, GetCountriesResponseEntity>> getCountries(GetCountriesParamsEntity getCountriesParamsEntity);
Stream<Either<Failure, AddCountriesResponseEntity>> addCountries(AddCountriesParamsEntity addCountriesParamsEntity);
Stream<Either<Failure, UpdateCountriesResponseEntity>> updateCountries(UpdateCountriesParamsEntity updateCountriesParamsEntity);
Stream<Either<Failure, DeleteCountriesResponseEntity>> deleteCountries(DeleteCountriesParamsEntity deleteCountriesParamsEntity);
}
