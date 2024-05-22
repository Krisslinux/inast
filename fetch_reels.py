def fetch_reels(cl, target_username):
    user_id = cl.user_id_from_username(target_username)
    reels = cl.user_clips(user_id)
    return reels