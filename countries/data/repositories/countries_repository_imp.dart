import 'package:commdem_warriors/core/failure/failures.dart';
import 'package:dartz/dartz.dart';
import 'package:flutter/foundation.dart';
import '../datasource/network_source_imp.dart';
import '../../domain/repositories/countries_repository.dart';
import '../../domain/entities/add_countries_entity.dart';
import '../../domain/entities/add_countries_params_entity.dart';
import '../../domain/entities/get_countries_entity.dart';
import '../../domain/entities/get_countries_params_entity.dart';
import '../../domain/entities/update_countries_entity.dart';
import '../../domain/entities/update_countries_params_entity.dart';
import '../../domain/entities/delete_countries_entity.dart';
import '../../domain/entities/delete_countries_params_entity.dart';


class CountriesRepositoryImp extends CountriesRepository {
  final CountriesNetworkSourceImp _countriesNetworkSourceImp;
  CountriesRepositoryImp(this._countriesNetworkSourceImp);

  @override
  Stream<Either<Failure, GetCountriesResponseEntity>> getCountries(
      GetCountriesParamsEntity countriesParamsEntity) async* {
    try {
      GetCountriesResponseEntity responseFromNetwork =
          await _countriesNetworkSourceImp.getCountries(countriesParamsEntity);
      if (kDebugMode) {
        print("_responseFromNetwork");
      }
      yield Right(responseFromNetwork);
    } on Failure catch (failure) {
      if (kDebugMode) {
        print("failure $failure");
      }
      yield Left(failure);
    } catch (e) {
      if (kDebugMode) {
        print("e $e");
      }
      yield Left(FailureMessage());
    }
  }
                        
  @override
  Stream<Either<Failure, AddCountriesResponseEntity>> addCountries(
      AddCountriesParamsEntity countriesParamsEntity) async* {
    try {
      AddCountriesResponseEntity responseFromNetwork =
          await _countriesNetworkSourceImp.addCountries(countriesParamsEntity);
      if (kDebugMode) {
        print("_responseFromNetwork");
      }
      yield Right(responseFromNetwork);
    } on Failure catch (failure) {
      if (kDebugMode) {
        print("failure $failure");
      }
      yield Left(failure);
    } catch (e) {
      if (kDebugMode) {
        print("e $e");
      }
      yield Left(FailureMessage());
    }
  }
                        
  @override
  Stream<Either<Failure, UpdateCountriesResponseEntity>> updateCountries(
      UpdateCountriesParamsEntity countriesParamsEntity) async* {
    try {
      UpdateCountriesResponseEntity responseFromNetwork =
          await _countriesNetworkSourceImp.updateCountries(countriesParamsEntity);
      if (kDebugMode) {
        print("_responseFromNetwork");
      }
      yield Right(responseFromNetwork);
    } on Failure catch (failure) {
      if (kDebugMode) {
        print("failure $failure");
      }
      yield Left(failure);
    } catch (e) {
      if (kDebugMode) {
        print("e $e");
      }
      yield Left(FailureMessage());
    }
  }
                        
  @override
  Stream<Either<Failure, DeleteCountriesResponseEntity>> deleteCountries(
      DeleteCountriesParamsEntity countriesParamsEntity) async* {
    try {
      DeleteCountriesResponseEntity responseFromNetwork =
          await _countriesNetworkSourceImp.deleteCountries(countriesParamsEntity);
      if (kDebugMode) {
        print("_responseFromNetwork");
      }
      yield Right(responseFromNetwork);
    } on Failure catch (failure) {
      if (kDebugMode) {
        print("failure $failure");
      }
      yield Left(failure);
    } catch (e) {
      if (kDebugMode) {
        print("e $e");
      }
      yield Left(FailureMessage());
    }
  }
                        
}