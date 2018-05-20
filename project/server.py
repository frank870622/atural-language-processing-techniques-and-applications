import  graphing
if isinstance(event.message, TextMessage):
    if "師生數量" in event.message.text:
        im = graphing.drawing("師生數量")
        image_message = ImageSendMessage(
            original_content_url=im,
            preview_image_url=im
        )
        line_bot_api.reply_message( event.reply_token, image_message)
        return 0
    elif "註冊率" in event.message.text:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text= graphing.drawing("註冊率")))
        return 0
    elif "就業比例" in event.message.text:
        im = graphing.drawing("就業比例")
        image_message = ImageSendMessage(
            original_content_url=im,
            preview_image_url=im
        )
        line_bot_api.reply_message(event.reply_token, image_message)
        return 0
    elif "學測分數" in event.message.text:
        im = graphing.drawing("學測分數")
        image_message = ImageSendMessage(
            original_content_url=im,
            preview_image_url=im
        )
        line_bot_api.reply_message(event.reply_token, image_message)
        return 0
    elif "指考分數" in event.message.text:
        line_bot_api.reply_message(event.reply_token, TextSendMessage(text=graphing.drawing("指考分數")))
        return 0
