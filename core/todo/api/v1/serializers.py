from rest_framework import serializers
from todo.models import Task
from accounts.models import Profile


class TaskSerializer(serializers.ModelSerializer):
    absolute_url = serializers.SerializerMethodField(method_name='get_absolute_url')
    class Meta:
        model = Task
        fields = ['id', 'user', 'content', 'created_date', 'updated_date', 'isDone', 'absolute_url']

    def get_absolute_url(self, obj=None):
        request = self.context.get('request')
        url = request.build_absolute_uri()
        try:
            int(url[-2])
            return url
        except ValueError:
            return request.build_absolute_uri(obj.pk)

    def to_representation(self, instance):
        request = self.context.get('request')
        rep = super().to_representation(instance)
        rep['user'] = Profile.objects.get(pk=rep['user']).user.email
        if not request.parser_context.get('kwargs').get('pk', False):
            rep.pop('content', None)
        return rep
