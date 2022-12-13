import 'dart:convert';
import '../../domain/entities/add_location_of_user_entity.dart';


class AddLocationOfUserResponseModel extends AddLocationOfUserResponseEntity {
  AddLocationOfUserResponseModel({
    required this.success,
    required this.message,
  }) : super(success: success, message: message);

  bool success;
  String message;
  factory AddLocationOfUserResponseModel.fromJson(String str) =>
      AddLocationOfUserResponseModel.fromMap(json.decode(str));

  String toJson() => json.encode(toMap());  factory AddLocationOfUserResponseModel.fromMap(Map<String, dynamic> json) =>
      AddLocationOfUserResponseModel(
        success: json['success'],
        message: json['message'],
        );
  Map<String, dynamic> toMap() => {
    'success': success,
    'message': message,
  };

}
