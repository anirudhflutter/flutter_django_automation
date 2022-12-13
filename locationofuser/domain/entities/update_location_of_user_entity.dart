
import 'package:equatable/equatable.dart';

class UpdateLocationOfUserResponseEntity extends Equatable{
  UpdateLocationOfUserResponseEntity({
    required this.success,
    required this.message,
  });

  final bool success;
  final String message;

  @override
  // TODO: implement props
  List<Object?> get props => [success,message];
}
                  