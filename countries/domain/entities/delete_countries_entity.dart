
import 'package:equatable/equatable.dart';

class DeleteCountriesResponseEntity extends Equatable{
  DeleteCountriesResponseEntity({
    required this.success,
    required this.message,
  });

  final bool success;
  final String message;

  @override
  // TODO: implement props
  List<Object?> get props => [success,message];
}
                  