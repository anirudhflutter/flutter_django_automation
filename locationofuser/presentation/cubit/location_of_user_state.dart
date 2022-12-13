import '../../../../core/helpers/base/base_state.dart';
import '../../domain/entities/add_location_of_user_entity.dart';
import '../../domain/entities/get_location_of_user_entity.dart';
import '../../domain/entities/update_location_of_user_entity.dart';
import '../../domain/entities/delete_location_of_user_entity.dart';


class LocationOfUserFailState extends BaseState {
  String errorMessage;

  LocationOfUserFailState({required this.errorMessage});

  @override
  // TODO: implement props
  List<Object?> get props => [errorMessage];
}


class GetLocationOfUserSuccessState extends BaseState {
  GetLocationOfUserResponseEntity successResponse;

  GetLocationOfUserSuccessState({required this.successResponse});

  @override
  // TODO: implement props
  List<Object?> get props => [successResponse];
}

class AddLocationOfUserSuccessState extends BaseState {
  AddLocationOfUserResponseEntity successResponse;

  AddLocationOfUserSuccessState({required this.successResponse});

  @override
  // TODO: implement props
  List<Object?> get props => [successResponse];
}

class UpdateLocationOfUserSuccessState extends BaseState {
  UpdateLocationOfUserResponseEntity successResponse;

  UpdateLocationOfUserSuccessState({required this.successResponse});

  @override
  // TODO: implement props
  List<Object?> get props => [successResponse];
}

class DeleteLocationOfUserSuccessState extends BaseState {
  DeleteLocationOfUserResponseEntity successResponse;

  DeleteLocationOfUserSuccessState({required this.successResponse});

  @override
  // TODO: implement props
  List<Object?> get props => [successResponse];
}


                  