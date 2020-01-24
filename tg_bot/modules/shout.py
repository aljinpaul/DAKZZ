from telegram import Update, Bot
from telegram.ext import run_async

from tg_bot.modules.disable import DisableAbleCommandHandler
from tg_bot import dispatcher

@run_async
def shout(bot: Bot, update: Update, args):
    if len(args) == 0:
        update.effective_message.reply_text("Where is text?")
        return

    msg = "```"
    text = " ".join(args)
    result = []
    result.append(' '.join([s for s in text]))
    for pos, symbol in enumerate(text[1:]):
        result.append(symbol + ' ' + '  ' * pos + symbol)
    result = list("\n".join(result))
    result[0] = text[0]
    result = "".join(result)
    msg = "```\n" + result + "```"
    return update.effective_message.reply_text(msg, parse_mode="MARKDOWN")
    
__help__ = """
 രസകരമായ പദങ്ങളുടെ ഒരു ചെറിയ ഭാഗം! ചാറ്റ് റൂമിൽ ഉച്ചത്തിലുള്ള ആരവം നൽകുക.
 
അതായത്  /shout HELP, സ്ക്വയറിനുള്ളിൽ വലിയ കോഡ് ചെയ്ത HELP അക്ഷരങ്ങൾ ഉപയോഗിച്ച് ബോട്ട് മറുപടി നൽകുന്നു. 
 
 - /shout <keyword>: നിങ്ങൾക്ക് ഉച്ചത്തിലുള്ള ശബ്ദമുണ്ടാക്കാൻ ആഗ്രഹിക്കുന്ന എന്തും എഴുതുക.
  
"""

__mod_name__ = "Shout Text"

SHOUT_HANDLER = DisableAbleCommandHandler("shout", shout, pass_args=True)

dispatcher.add_handler(SHOUT_HANDLER)
