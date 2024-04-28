def user_status(request):
    is_logged_in = request.session.get('logged_in', False)
    return {
        'is_logged_in': is_logged_in
    }