import 'package:equatable/equatable.dart';
import '../../domain/entities/get_location_of_user_entity.dart';





class GetLocationOfUserResponseEntity extends Equatable {
  GetLocationOfUserResponseEntity({
    required this.data,
    required this.success,
    required this.message,
  });
  final GetDataResponseEntity data;
  final bool success;
  final String message;

  @override
// TODO: implement props
  List<Object?> get props => [data,success,message,];
}

