import 'dart:convert';
import '../../domain/entities/add_countries_entity.dart';


class AddCountriesResponseModel extends AddCountriesResponseEntity {
  AddCountriesResponseModel({
    required this.success,
    required this.message,
  }) : super(success: success, message: message);

  bool success;
  String message;
  factory AddCountriesResponseModel.fromJson(String str) =>
      AddCountriesResponseModel.fromMap(json.decode(str));

  String toJson() => json.encode(toMap());  factory AddCountriesResponseModel.fromMap(Map<String, dynamic> json) =>
      AddCountriesResponseModel(
        success: json['success'],
        message: json['message'],
        );
  Map<String, dynamic> toMap() => {
    'success': success,
    'message': message,
  };

}
