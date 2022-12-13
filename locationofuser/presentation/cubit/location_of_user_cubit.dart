import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import '../../../../core/helpers/base/base_state.dart';
import '../../domain/entities/add_location_of_user_params_entity.dart';
import '../../domain/entities/get_location_of_user_params_entity.dart';
import '../../domain/entities/update_location_of_user_params_entity.dart';
import '../../domain/entities/delete_location_of_user_params_entity.dart';
import '../../domain/usecases/add_location_of_user_case.dart';
import '../../domain/usecases/get_location_of_user_case.dart';
import '../../domain/usecases/update_location_of_user_case.dart';
import '../../domain/usecases/delete_location_of_user_case.dart';
import 'location_of_user_state.dart';



class LocationOfUserCubit extends Cubit<BaseState> {

  GetLocationOfUserCase getLocationOfUserCase;
  AddLocationOfUserCase addLocationOfUserCase;
  UpdateLocationOfUserCase updateLocationOfUserCase;
  DeleteLocationOfUserCase deleteLocationOfUserCase;
  
  LocationOfUserCubit(this.getLocationOfUserCase,this.addLocationOfUserCase,this.updateLocationOfUserCase,this.deleteLocationOfUserCase) : super(StateLoading());

    Future addLocationOfUser({required AddLocationOfUserParamsEntity addLocationOfUserParamsEntity,required BuildContext context}) async {
    addLocationOfUserCase.call(addLocationOfUserParamsEntity).listen((event) {
      event.fold((fail) {
        print('addLocationOfUser fail in cubit ${fail.toString()}');
        emit(LocationOfUserFailState(errorMessage: fail.toString()));
      }, (success) {
        print('addLocationOfUser success in cubit  $success');
        emit(AddLocationOfUserSuccessState(successResponse: success));
      });
    });
  }

  Future getLocationOfUser({required GetLocationOfUserParamsEntity getLocationOfUserParamsEntity,required BuildContext context}) async {
    getLocationOfUserCase.call(getLocationOfUserParamsEntity).listen((event) {
      event.fold((fail) {
        print('getLocationOfUser fail in cubit ${fail.toString()}');
        emit(LocationOfUserFailState(errorMessage: fail.toString()));
      }, (success) {
        print('getLocationOfUser success in cubit  $success');
        emit(GetLocationOfUserSuccessState(successResponse: success));
      });
    });
  }

  Future updateLocationOfUser({required UpdateLocationOfUserParamsEntity updateLocationOfUserParamsEntity,required BuildContext context}) async {
    updateLocationOfUserCase.call(updateLocationOfUserParamsEntity).listen((event) {
      event.fold((fail) {
        print('updateLocationOfUser fail in cubit ${fail.toString()}');
        emit(LocationOfUserFailState(errorMessage: fail.toString()));
      }, (success) {
        print('updateLocationOfUser success in cubit  $success');
        emit(UpdateLocationOfUserSuccessState(successResponse: success));
      });
    });
  }

    Future deleteLocationOfUser({required DeleteLocationOfUserParamsEntity deleteLocationOfUserParamsEntity,required BuildContext context}) async {
    deleteLocationOfUserCase.call(deleteLocationOfUserParamsEntity).listen((event) {
      event.fold((fail) {
        print('deleteLocationOfUser fail in cubit ${fail.toString()}');
        emit(LocationOfUserFailState(errorMessage: fail.toString()));
      }, (success) {
        print('deleteLocationOfUser success in cubit  $success');
        emit(DeleteLocationOfUserSuccessState(successResponse: success));
      });
    });
  }

}  

                  