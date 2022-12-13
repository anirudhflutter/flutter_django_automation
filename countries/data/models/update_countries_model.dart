import 'dart:convert';
import '../../domain/entities/update_countries_entity.dart';


class UpdateCountriesResponseModel extends UpdateCountriesResponseEntity {
  UpdateCountriesResponseModel({
    required this.success,
    required this.message,
  }) : super(success: success, message: message);

  bool success;
  String message;
  factory UpdateCountriesResponseModel.fromJson(String str) =>
      UpdateCountriesResponseModel.fromMap(json.decode(str));

  String toJson() => json.encode(toMap());  factory UpdateCountriesResponseModel.fromMap(Map<String, dynamic> json) =>
      UpdateCountriesResponseModel(
        success: json['success'],
        message: json['message'],
        );
  Map<String, dynamic> toMap() => {
    'success': success,
    'message': message,
  };

}
