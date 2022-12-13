import 'package:commdem_warriors/core/failure/failures.dart';
import 'package:dartz/dartz.dart';
import 'package:flutter/foundation.dart';
import '../datasource/network_source_imp.dart';
import '../../domain/repositories/location_of_user_repository.dart';
import '../../domain/entities/add_location_of_user_entity.dart';
import '../../domain/entities/add_location_of_user_params_entity.dart';
import '../../domain/entities/get_location_of_user_entity.dart';
import '../../domain/entities/get_location_of_user_params_entity.dart';
import '../../domain/entities/update_location_of_user_entity.dart';
import '../../domain/entities/update_location_of_user_params_entity.dart';
import '../../domain/entities/delete_location_of_user_entity.dart';
import '../../domain/entities/delete_location_of_user_params_entity.dart';


class LocationOfUserRepositoryImp extends LocationOfUserRepository {
  final LocationOfUserNetworkSourceImp _locationofuserNetworkSourceImp;
  LocationOfUserRepositoryImp(this._locationofuserNetworkSourceImp);

  @override
  Stream<Either<Failure, GetLocationOfUserResponseEntity>> getLocationOfUser(
      GetLocationOfUserParamsEntity locationofuserParamsEntity) async* {
    try {
      GetLocationOfUserResponseEntity responseFromNetwork =
          await _locationofuserNetworkSourceImp.getLocationOfUser(locationofuserParamsEntity);
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
  Stream<Either<Failure, AddLocationOfUserResponseEntity>> addLocationOfUser(
      AddLocationOfUserParamsEntity locationofuserParamsEntity) async* {
    try {
      AddLocationOfUserResponseEntity responseFromNetwork =
          await _locationofuserNetworkSourceImp.addLocationOfUser(locationofuserParamsEntity);
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
  Stream<Either<Failure, UpdateLocationOfUserResponseEntity>> updateLocationOfUser(
      UpdateLocationOfUserParamsEntity locationofuserParamsEntity) async* {
    try {
      UpdateLocationOfUserResponseEntity responseFromNetwork =
          await _locationofuserNetworkSourceImp.updateLocationOfUser(locationofuserParamsEntity);
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
  Stream<Either<Failure, DeleteLocationOfUserResponseEntity>> deleteLocationOfUser(
      DeleteLocationOfUserParamsEntity locationofuserParamsEntity) async* {
    try {
      DeleteLocationOfUserResponseEntity responseFromNetwork =
          await _locationofuserNetworkSourceImp.deleteLocationOfUser(locationofuserParamsEntity);
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