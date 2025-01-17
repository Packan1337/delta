import os

# Embed color for messages (#ffffff -> 0xffffff)
bot_color = 0x17c6ff # General color
bot_color2 = 0x2F3136 # Color for image commands

bot_time = "%d/%b/%Y %H:%M:%S" # Time structure for logs
code_link = "https://github.com/tibor309/delta" # Source code link

# Environment variables
# Set these in your env file!
bot_token = os.environ["TOKEN"]  # Your bot token -- NEVER SHARE YOUR TOKEN WITH ANYONE!
err_channel = os.environ["ERR_CHANNEL"] # Channel id for error logging (for bot admin)


# Icons for embeds
user_icon = "https://images.tibor309.repl.co/icons/user.png" # for member specific commnds
guild_icon = "https://images.tibor309.repl.co/icons/folder_cpu.png" # icon for guild specific commands

# Emojis for commands
# The bot needs access to the server to use custom emojs,
# so if you plan to fork the bot, change these to your own!
yes_emoji = "<:ye:935798200621760533>" # emoji for upvote
no_emoji = "<:nah:935798200869208074>" # emoji for downvote 
invite_emoji = "<:love:1027605898593579118>" # emoji for invite button
code_emoji = "<:github:1102166658589655080>" # emoji for source code link 



# Messages
# One message is randomly selected to be sent
no_perm = ["nope", "you don't have perms for this!", "access denied", "You don't have enough perms for this", "skill issue", "https://image.tibor309.repl.co/memes/no_perms.png", "you don't have perms", "https://tenor.com/view/nuh-uh-beocord-no-lol-gif-24435520", "nuh uh!"]
bot_no_perm = ["I don't have perms!", "i don't have enough perms for this", "i can't help you with that. i don't have perms"]
cmd_dms = ["You can't use this command here.", "No", "You can only use these commands in servers.", "Nope", "you can't use this command in dms!"]
bot_join_msg = ["Hi everyone!", "Hi", "hi everyone", "hi", "Hello everyone!", "https://tenor.com/view/hi-gif-25925938"]
err_msg = ["something went wrong", "well that didn't work", "uh.. i got an error", "got an error", "something didn't work"]
img_fail = ["I couldn't get the image", "Failed to get the image :(", "i couldn't download the image"]
on_cooldown = ["You're on cooldown!", "hey slow down", "not yet!"]