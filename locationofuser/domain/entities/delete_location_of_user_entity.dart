
import 'package:equatable/equatable.dart';

class DeleteLocationOfUserResponseEntity extends Equatable{
  DeleteLocationOfUserResponseEntity({
    required this.success,
    required this.message,
  });

  final bool success;
  final String message;

  @override
  // TODO: implement props
  List<Object?> get props => [success,message];
}
                  