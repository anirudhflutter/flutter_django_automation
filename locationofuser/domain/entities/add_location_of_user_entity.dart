
import 'package:equatable/equatable.dart';

class AddLocationOfUserResponseEntity extends Equatable{
  AddLocationOfUserResponseEntity({
    required this.success,
    required this.message,
  });

  final bool success;
  final String message;

  @override
  // TODO: implement props
  List<Object?> get props => [success,message];
}
                  