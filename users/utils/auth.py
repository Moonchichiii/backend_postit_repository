from rest_framework_simplejwt.tokens import RefreshToken


def jwt_token_generation(user):
    refresh = RefreshToken.for_user(user)
    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'user_id': user.id,
        'profile_id': user.profile.id if hasattr(user, 'profile') else None
    }
