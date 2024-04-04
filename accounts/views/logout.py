from django.contrib.auth.views import LogoutView


class CustomLogoutView(LogoutView):

    def dispatch(self, request, *args, **kwargs):
        # Customize logout behavior here if needed
        # For example, you can perform additional actions before logout

        # Call the parent class's dispatch method to handle logout logic
        response = super().dispatch(request, *args, **kwargs)

        # Additional logic after logout if needed

        return response
