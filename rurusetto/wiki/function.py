from django.contrib.auth.models import User


def make_listing_view(model_list):
    export_list = []
    for item in model_list:
        ruleset_owner = User.objects.filter(id=item.owner).first()
        export_list.append([item, ruleset_owner])
    return export_list