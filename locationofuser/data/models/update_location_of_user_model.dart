import 'dart:convert';
import '../../domain/entities/update_location_of_user_entity.dart';


class UpdateLocationOfUserResponseModel extends UpdateLocationOfUserResponseEntity {
  UpdateLocationOfUserResponseModel({
    required this.success,
    required this.message,
  }) : super(success: success, message: message);

  bool success;
  String message;
  factory UpdateLocationOfUserResponseModel.fromJson(String str) =>
      UpdateLocationOfUserResponseModel.fromMap(json.decode(str));

  String toJson() => json.encode(toMap());  factory UpdateLocationOfUserResponseModel.fromMap(Map<String, dynamic> json) =>
      UpdateLocationOfUserResponseModel(
        success: json['success'],
        message: json['message'],
        );
  Map<String, dynamic> toMap() => {
    'success': success,
    'message': message,
  };

}
