










session_name
@app.on_message(filters.regex("تغيير الاسم"))
def change_name(client, message):
    input_name = message.text.split(" ")[1]
    current_first_name = app.session.first_name
    current_bot_name = client.get_me().first_name
    
    if not input_name:
        message.reply_text("الرجاء إدخال اسم صحيح.")
    elif input_name == current_first_name:
        message.reply_text("لا يمكن تحديث اسم الحساب الأول للمستخدم إلى نفس الاسم الحالي.")
    else:
        app.update_profile(first_name=input_name)
        client.update_profile(first_name=input_name)
        message.reply_text(f"تم تحديث اسم الحساب الأول للمستخدم إلى {input_name} واسم البوت إلى {input_name}.")