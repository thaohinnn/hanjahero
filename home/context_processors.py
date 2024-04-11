def user_first_name(request):
    first_name = None
    if request.user.is_authenticated:
        first_name = request.user.first_name
    return {'user_first_name': first_name}