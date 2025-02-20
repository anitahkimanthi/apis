from admin import serializers


class UsersSerializer (serializers.ModelSerializers):
    class meta: 
        model = Users
        fields = "__all__"
    