import '../../../../core/helpers/base/base_state.dart';
import '../../domain/entities/add_countries_entity.dart';
import '../../domain/entities/get_countries_entity.dart';
import '../../domain/entities/update_countries_entity.dart';
import '../../domain/entities/delete_countries_entity.dart';


class CountriesFailState extends BaseState {
  String errorMessage;

  CountriesFailState({required this.errorMessage});

  @override
  // TODO: implement props
  List<Object?> get props => [errorMessage];
}


class GetCountriesSuccessState extends BaseState {
  GetCountriesResponseEntity successResponse;

  GetCountriesSuccessState({required this.successResponse});

  @override
  // TODO: implement props
  List<Object?> get props => [successResponse];
}

class AddCountriesSuccessState extends BaseState {
  AddCountriesResponseEntity successResponse;

  AddCountriesSuccessState({required this.successResponse});

  @override
  // TODO: implement props
  List<Object?> get props => [successResponse];
}

class UpdateCountriesSuccessState extends BaseState {
  UpdateCountriesResponseEntity successResponse;

  UpdateCountriesSuccessState({required this.successResponse});

  @override
  // TODO: implement props
  List<Object?> get props => [successResponse];
}

class DeleteCountriesSuccessState extends BaseState {
  DeleteCountriesResponseEntity successResponse;

  DeleteCountriesSuccessState({required this.successResponse});

  @override
  // TODO: implement props
  List<Object?> get props => [successResponse];
}


                  