from rest_framework import serializers
from wiki.models import Ruleset, Subpage
from users.models import Profile
from django.contrib.auth.models import User


class FullRulesetSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for Ruleset model for passing the value to the API view
    """
    class Meta:
        model = Ruleset
        fields = ['id', 'name', 'slug', 'description', 'icon', 'light_icon', 'logo', 'cover_image', 'cover_image_light',
                  'opengraph_image', 'recommend_beatmap_cover', 'custom_css', 'content', 'source', 'github_download_filename',
                  'creator', 'created_at', 'owner', 'last_edited_at', 'last_edited_by', 'verified', 'archive']


class MinimizeRulesetSerializer(serializers.HyperlinkedModelSerializer):
    """
    Serializer for Ruleset model for passing only main detail of the ruleset to the API view
    """
    class Meta:
        model = Ruleset
        fields = ['id', 'name', 'slug', 'description', 'icon', 'light_icon', 'source', 'github_download_filename',
                  'owner', 'verified', 'archive']


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class ProfileMiniSerializer(serializers.ModelSerializer):
    """
    Serializer that will only filter the profile of owner to use in RulesetListingSerializer.
    """
    user = UserSerializer()

    class Meta:
        model = Profile
        fields = ['id', 'user', 'image']
        depth = 1


# Serializer for listing page


class RulesetListingSerializer(serializers.ModelSerializer):
    """
    Serializer for essential information that is user in listing page.
    """
    owner_detail = serializers.SerializerMethodField()

    class Meta:
        model = Ruleset
        fields = ['id', 'name', 'slug', 'description', 'icon', 'light_icon', 'owner_detail', 'verified']

    def get_owner_detail(self, obj):
        owner = Profile.objects.get(id=obj.owner)
        return ProfileMiniSerializer(owner).data


# Serializer for rulesets detail


class RulesetsDetailSubpageSerializer(serializers.ModelSerializer):
    """
    Serializer for Subpage model that use in RulesetsDetailSerializer
    """
    class Meta:
        model = Subpage
        # fields = ['title', 'slug']
        fields = '__all__'


class RulesetsDetailSerializer(serializers.ModelSerializer):
    """
    Serializer for essential information in wiki view of each rulesets
    """
    # subpage = serializers.SerializerMethodField()
    creator_detail = serializers.SerializerMethodField()
    owner_detail = serializers.SerializerMethodField()
    last_edited_by_detail = serializers.SerializerMethodField()

    class Meta:
        model = Ruleset
        fields = ['id', 'name', 'slug', 'description', 'icon', 'light_icon', 'logo', 'cover_image', 'cover_image_light',
                  'opengraph_image', 'custom_css', 'content', 'source',
                  'github_download_filename', 'creator_detail', 'created_at', 'owner_detail',
                  'last_edited_at', 'last_edited_by_detail', 'verified', 'archive']

    def get_subpage(self, obj):
        all_subpage = Subpage.objects.filter(ruleset_id=obj.id, hidden=False)
        return RulesetsDetailSubpageSerializer(all_subpage).data

    def get_creator_detail(self, obj):
        creator = Profile.objects.get(id=obj.creator)
        return ProfileMiniSerializer(creator).data

    def get_owner_detail(self, obj):
        owner = Profile.objects.get(id=obj.owner)
        return ProfileMiniSerializer(owner).data

    def get_last_edited_by_detail(self, obj):
        last_edited_by = Profile.objects.get(id=obj.last_edited_by)
        return ProfileMiniSerializer(last_edited_by).data
