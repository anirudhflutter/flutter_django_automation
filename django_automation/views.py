
from rest_framework.decorators import api_view
from rest_framework.response import Response
from response import Response as ResponseData
from rest_framework import status
from subscription.models import SubscriptionModel
from subscription.serializers import AddSubscriptionSerializer, GetSubscriptionSerializer

# Create your views here.

@api_view(["POST"])
def add_subscription(request):
    """Function to add new subscription details"""
    try:
        data = request.data
        serializer = AddSubscriptionSerializer(data=data)
        if serializer.is_valid():
            amount = serializer.data["amount"]
            is_free_trial = serializer.data["is_free_trial"]
            duration = serializer.data["duration"]

            data_exists = SubscriptionModel.objects.filter(
                amount = amount,
                is_free_trial = is_free_trial,
                duration = duration,

                ).first()
            if data_exists:
                   return Response(
                       ResponseData.error("Subscription with these details already exists"),
                       status=status.HTTP_200_OK,
                   )
            new_subscription = SubscriptionModel.objects.create(
                amount = amount,
                is_free_trial = is_free_trial,
                duration = duration,

            )
            new_subscription.save()
            return Response(
                ResponseData.success_without_data(
                    "Subscription added successfully"),
                status=status.HTTP_201_CREATED,
            )
        for error in serializer.errors:
            print(serializer.errors[error][0])
        return Response(
            ResponseData.error(serializer.errors[error][0]),
            status=status.HTTP_400_BAD_REQUEST,
        )
    except Exception as exception:
        return Response(
            ResponseData.error(str(exception)), status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(["POST"])
def get_subscription_by_id(request):
    """Function to get a subscription based on id"""
    try:
        data = request.data
        serializer = GetSubscriptionSerializer(data=data)
        if serializer.is_valid():
            subscription_id = serializer.data["id"]
            is_id_valid = SubscriptionModel.objects.filter(id=subscription_id).first()
            if not is_id_valid:
                   return Response(
                       ResponseData.error("Subscription id is invalid"),
                       status=status.HTTP_200_OK,
                   )
            subscription_data = SubscriptionModel.objects.values().filter(id = subscription_id).all()
            for i in range(0,len(subscription_data)):
                subscription_data[i].pop('created_at')
                subscription_data[i].pop('updated_at')
            return Response(
                ResponseData.success(
                    subscription_data, "Subscription details fetched successfully"),
                status=status.HTTP_201_CREATED)
        return Response(
                    ResponseData.error(serializer.errors),
                    status=status.HTTP_400_BAD_REQUEST,
                )
    except Exception as exception:
        return Response(
            ResponseData.error(str(exception)), status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(["POST"])
def get_all_subscription(request):
    """Function to get all subscription"""
    try:
        data = request.data
        serializer = GetSubscriptionSerializer(data=data)
        if serializer.is_valid():
                subscription_details = list(
                SubscriptionModel.objects.values().filter())
                for i in range(0,len(subscription_details)):
                    subscription_details[i].pop('created_at')
                    subscription_details[i].pop('updated_at')
                return Response(
                    ResponseData.success(
                        subscription_details, "Subscription details fetched successfully"),
                    status=status.HTTP_201_CREATED)
        return Response(
                    ResponseData.error(serializer.errors),
                    status=status.HTTP_400_BAD_REQUEST,
                )
    except Exception as exception:
        return Response(
            ResponseData.error(str(exception)), status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(["POST"])
def delete_subscription_by_id(request):
    """Function to delete a subscription based on id"""
    try:
        data = request.data
        serializer = GetSubscriptionSerializer(data=data)
        if serializer.is_valid():
            subscription_id = serializer.data["id"]
            is_id_valid = SubscriptionModel.objects.filter(id=subscription_id).first()
            if not is_id_valid:
                   return Response(
                       ResponseData.error("subscription id is invalid"),
                       status=status.HTTP_200_OK,
                   )
            subscription_data = SubscriptionModel.objects.values().filter(id = subscription_id).delete()
            return Response(
                ResponseData.success_without_data(
                    "Subscription of this id deleted successfully"),
                status=status.HTTP_201_CREATED)
        return Response(
                    ResponseData.error(serializer.errors),
                    status=status.HTTP_400_BAD_REQUEST,
                )
    except Exception as exception:
        return Response(
            ResponseData.error(str(exception)), status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )


@api_view(["POST"])
def delete_all_subscription(request):
    """Function to delete all subscription"""
    try:
        data = request.data
        serializer = GetSubscriptionSerializer(data=data)
        if serializer.is_valid():
            subscription_data = SubscriptionModel.objects.values().filter().delete()
            return Response(
                ResponseData.success_without_data(
                    "All subscription deleted successfully"),
                status=status.HTTP_201_CREATED)
        return Response(
                    ResponseData.error(serializer.errors),
                    status=status.HTTP_400_BAD_REQUEST,
                )
    except Exception as exception:
        return Response(
            ResponseData.error(str(exception)), status=status.HTTP_500_INTERNAL_SERVER_ERROR
        )

@api_view(["POST"])
def update_subscription(request):
    """Function to update subscription details"""
    try:
        data = request.data
        serializer = AddSubscriptionSerializer(data=data)
        if serializer.is_valid():
            subscription_id = serializer.data['id']
            amount = serializer.data["amount"]
            is_free_trial = serializer.data["is_free_trial"]
            duration = serializer.data["duration"]

            subscription_data = SubscriptionModel.objects.filter(
                id=subscription_id
            ).first()
            if not subscription_data:
                return Response(
                    ResponseData.error("Subscription id is invalid."),
                    status=status.HTTP_200_OK,
                )
            if 'image' in request.FILES:
                fs = FileSystemStorage(location='static/')
                fs.save(request.FILES['image'].name, request.FILES['image'])
            subscription_data.amount=amount
            subscription_data.is_free_trial=is_free_trial
            subscription_data.duration=duration

            #if 'image' in request.FILES:
            #   userdata.profile_pic = f"static/{request.FILES['image']}"
            subscription_data.save()
            updated_data = list(
                SubscriptionModel.objects.values().filter(
                    id=subscription_id)
            )
            return Response(
                ResponseData.success(
                    updated_data[0]['id'], "Subscription details updated successfully"),
                status=status.HTTP_201_CREATED,
            )
        return Response(
            ResponseData.error(serializer.errors),
            status=status.HTTP_400_BAD_REQUEST,
        )
    except KeyError as exception:
        return Response(
            ResponseData.error(str(exception)),
            status=status.HTTP_500_INTERNAL_SERVER_ERROR,
        )

                  