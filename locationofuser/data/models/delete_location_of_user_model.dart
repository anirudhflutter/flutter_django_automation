import 'dart:convert';
import '../../domain/entities/delete_location_of_user_entity.dart';


class DeleteLocationOfUserResponseModel extends DeleteLocationOfUserResponseEntity {
  DeleteLocationOfUserResponseModel({
    required this.success,
    required this.message,
  }) : super(success: success, message: message);

  bool success;
  String message;
  factory DeleteLocationOfUserResponseModel.fromJson(String str) =>
      DeleteLocationOfUserResponseModel.fromMap(json.decode(str));

  String toJson() => json.encode(toMap());  factory DeleteLocationOfUserResponseModel.fromMap(Map<String, dynamic> json) =>
      DeleteLocationOfUserResponseModel(
        success: json['success'],
        message: json['message'],
        );
  Map<String, dynamic> toMap() => {
    'success': success,
    'message': message,
  };

}
