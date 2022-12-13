import 'dart:convert';
import '../../domain/entities/delete_countries_entity.dart';


class DeleteCountriesResponseModel extends DeleteCountriesResponseEntity {
  DeleteCountriesResponseModel({
    required this.success,
    required this.message,
  }) : super(success: success, message: message);

  bool success;
  String message;
  factory DeleteCountriesResponseModel.fromJson(String str) =>
      DeleteCountriesResponseModel.fromMap(json.decode(str));

  String toJson() => json.encode(toMap());  factory DeleteCountriesResponseModel.fromMap(Map<String, dynamic> json) =>
      DeleteCountriesResponseModel(
        success: json['success'],
        message: json['message'],
        );
  Map<String, dynamic> toMap() => {
    'success': success,
    'message': message,
  };

}
