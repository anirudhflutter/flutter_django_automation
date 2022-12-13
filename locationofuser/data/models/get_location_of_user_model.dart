import 'dart:convert';
import '../../domain/entities/get_location_of_user_entity.dart';





class GetLocationOfUserResponseModel extends GetLocationOfUserResponseEntity {
  GetLocationOfUserResponseModel({
    required this.data,
    required this.success,
    required this.message,
  }) : super(
        success : success,
        message : message,
);

  final GetDataResponseModel data;
  final bool success;
  final String message;

  factory GetLocationOfUserResponseModel.fromMap(Map<String, dynamic> json) =>
      GetLocationOfUserResponseModel(
        success: json['success'],
        message: json['message'],

      );
  factory GetLocationOfUserResponseModel.fromJson(String str) =>
      GetLocationOfUserResponseModel.fromMap(json.decode(str));

String toJson() => json.encode(toMap());

  Map<String, dynamic> toMap() => {
        'success' : success,
        'message' : message,

      };

}
