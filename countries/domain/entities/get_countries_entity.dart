import 'package:equatable/equatable.dart';
import '../../domain/entities/get_countries_entity.dart';





class GetCountriesResponseEntity extends Equatable {
  GetCountriesResponseEntity({
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

