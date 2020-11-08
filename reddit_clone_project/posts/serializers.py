from rest_framework import serializers

from .models import Post, Vote

class PostSerializer(serializers.ModelSerializer): 

    # Read Only
    posted_by = serializers.ReadOnlyField(source='posted_by.username')
    posted_by_id = serializers.ReadOnlyField(source='posted_by.id')
    
    votes = serializers.SerializerMethodField()

    class Meta:
        model = Post
        fields = ['id', 'title', 'url', 'posted_by','posted_by_id', 'created_on', 'votes']
  
    def get_votes(self, post):
        return Vote.objects.filter(post=post).count()

class VoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vote
        fields = ['id'] 