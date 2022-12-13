import 'package:flutter/material.dart';
import 'package:flutter_bloc/flutter_bloc.dart';
import '../../../../core/helpers/base/base_state.dart';
import '../../domain/entities/add_countries_params_entity.dart';
import '../../domain/entities/get_countries_params_entity.dart';
import '../../domain/entities/update_countries_params_entity.dart';
import '../../domain/entities/delete_countries_params_entity.dart';
import '../../domain/usecases/add_countries_case.dart';
import '../../domain/usecases/get_countries_case.dart';
import '../../domain/usecases/update_countries_case.dart';
import '../../domain/usecases/delete_countries_case.dart';
import 'countries_state.dart';



class CountriesCubit extends Cubit<BaseState> {

  GetCountriesCase getCountriesCase;
  AddCountriesCase addCountriesCase;
  UpdateCountriesCase updateCountriesCase;
  DeleteCountriesCase deleteCountriesCase;
  
  CountriesCubit(this.getCountriesCase,this.addCountriesCase,this.updateCountriesCase,this.deleteCountriesCase) : super(StateLoading());

    Future addCountries({required AddCountriesParamsEntity addCountriesParamsEntity,required BuildContext context}) async {
    addCountriesCase.call(addCountriesParamsEntity).listen((event) {
      event.fold((fail) {
        print('addCountries fail in cubit ${fail.toString()}');
        emit(CountriesFailState(errorMessage: fail.toString()));
      }, (success) {
        print('addCountries success in cubit  $success');
        emit(AddCountriesSuccessState(successResponse: success));
      });
    });
  }

  Future getCountries({required GetCountriesParamsEntity getCountriesParamsEntity,required BuildContext context}) async {
    getCountriesCase.call(getCountriesParamsEntity).listen((event) {
      event.fold((fail) {
        print('getCountries fail in cubit ${fail.toString()}');
        emit(CountriesFailState(errorMessage: fail.toString()));
      }, (success) {
        print('getCountries success in cubit  $success');
        emit(GetCountriesSuccessState(successResponse: success));
      });
    });
  }

  Future updateCountries({required UpdateCountriesParamsEntity updateCountriesParamsEntity,required BuildContext context}) async {
    updateCountriesCase.call(updateCountriesParamsEntity).listen((event) {
      event.fold((fail) {
        print('updateCountries fail in cubit ${fail.toString()}');
        emit(CountriesFailState(errorMessage: fail.toString()));
      }, (success) {
        print('updateCountries success in cubit  $success');
        emit(UpdateCountriesSuccessState(successResponse: success));
      });
    });
  }

    Future deleteCountries({required DeleteCountriesParamsEntity deleteCountriesParamsEntity,required BuildContext context}) async {
    deleteCountriesCase.call(deleteCountriesParamsEntity).listen((event) {
      event.fold((fail) {
        print('deleteCountries fail in cubit ${fail.toString()}');
        emit(CountriesFailState(errorMessage: fail.toString()));
      }, (success) {
        print('deleteCountries success in cubit  $success');
        emit(DeleteCountriesSuccessState(successResponse: success));
      });
    });
  }

}  

                  