from rest_framework import serializers
from PharmaWeb.models.user import User
from PharmaWeb.models.account import Account
from PharmaWeb.serializers.accountSerializer import AccountSerializer

class UserSerializer(serializers.ModelSerializer):
    account = AccountSerializer()
    class Meta:
        model = User
        fields = ['id', 'username', 'password', 'Pname', 'sname', 'Papellido', 'Sapellido','Tipodoc','IdDocumento','email', 'account']

    def create(self, validated_data):
        accountData = validated_data.pop('account')
        userInstance = User.objects.create(**validated_data)
        Account.objects.create(user=userInstance, **accountData)
    
        return userInstance
# aca consulta
    def to_representation(self, obj):
        user = User.objects.get(id=obj.id)
        account = Account.objects.get(user=obj.id)       
        return {
                    'id': user.id, 
                    'username': user.username,
                    'Pname': user.Pname,
                    'email': user.email,
                    'account': {
                        'id': account.id,
                        'balance': account.balance,
                        'lastChangeDate': account.lastChangeDate,
                        'isActive': account.isActive
                    }
                }