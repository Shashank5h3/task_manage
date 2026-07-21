from django.contrib.auth.models import User, Group
from rest_framework import serializers


class RegisterSerializer(serializers.ModelSerializer): # this serializer is used to register a new user,
    password = serializers.CharField(                  # whenever POST /api/auth/register/ is called, it will be added to the User group by default
        write_only=True,
        min_length=8,
        style={"input_type": "password"}
    )

    confirm_password = serializers.CharField(
        write_only=True,
        style={"input_type": "password"}
    )

    class Meta: # this meta tells which model to use and which fields to include in the serializer
        model = User
        fields = (
            "id",
            "username",
            "email",
            "password",
            "confirm_password",
            "first_name",
            "last_name",
        )

    def validate(self, attrs):
        if attrs["password"] != attrs["confirm_password"]: # here it will validate if the pswd and confirm pswd is same or not.
            raise serializers.ValidationError(             # if the pswd doesnt match it will raise an error and return the msg
                {"confirm_password": "Passwords do not match."}
            )
        return attrs

    def create(self, validated_data):
        validated_data.pop("confirm_password")

        user = User.objects.create_user(
            username=validated_data["username"],
            email=validated_data.get("email"), # here we can use vadilated_data["email"] but we are using data.get("email") becoz if we wont enter the email id it will return none instead of throwing error
            password=validated_data["password"],
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
        )

        user_group, _ = Group.objects.get_or_create(name="User")
        user.groups.add(user_group)

        return user


class UserSerializer(serializers.ModelSerializer): #it is used to serialize the user data and return it in the response
    role = serializers.SerializerMethodField()

    class Meta:
        model = User
        fields = (
            "id",
            "username",
            "email",
            "first_name",
            "last_name",
            "role",
        )

    def get_role(self, obj):
        if obj.is_superuser:
            return "Admin"

        group = obj.groups.first()
        return group.name if group else "User"