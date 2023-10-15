from django.contrib import admin
from.models import *

# Register your models here.



class profileAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'age', 'gender', 'occupation', 'date_of_birth', 'is_married')
    list_display_links=('name', 'email')
    list_filter=('gender', 'is_married')
    search_fields=('occupation',)
    


admin.site.register(profile, profileAdmin)


admin.site.register(FatherProfile)
admin.site.register(Religion)
admin.site.register(Sect)
admin.site.register(Caste)


class HobbyAdmin(admin.ModelAdmin):
    list_display=('name','get_profiles')

    def get_profiles(self, obj):
        hobby_followers=", ".join([profile.name for profile in obj.profiles.all()])
        return hobby_followers
    
    get_profiles.short_description="Followers"

admin.site.register(Hobby, HobbyAdmin)





