def topup_balance(user_id, amount):
    user = User.objects.get(id=user_id)
    user.balance += amount
    user.save()
    return user.balance