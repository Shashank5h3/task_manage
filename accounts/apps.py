from django.apps import AppConfig # app config is used to configure the our app

class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField" # it generates id's  automatically and it controls the default primary key
    name = "accounts"

    def ready(self): # This method is called when the app is ready
        import accounts.signals