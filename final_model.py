


class GetCountriesResponseModel extends GetCountriesResponseEntity {
  GetCountriesResponseModel({
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

  factory GetCountriesResponseModel.fromMap(Map<String, dynamic> json) =>
      GetCountriesResponseModel(
        success: json['success'],
        message: json['message'],

      );
  factory GetCountriesResponseModel.fromJson(String str) =>
      GetCountriesResponseModel.fromMap(json.decode(str));

String toJson() => json.encode(toMap());

  Map<String, dynamic> toMap() => {
        'success' : success,
        'message' : message,

      };

}
