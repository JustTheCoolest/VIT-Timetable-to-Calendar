"""
This module interfaces with Discord to create:
1) A set of cosmetic roles in the bot's server based on the course list given (the course list has to be copy-pasted
from VTop),
2) Empty private channels for the corresponding subject roles, and
3) A message that we can copy-paste as the rolemenu message.
This bot is only intended to work as a complement of other rolemenu creation bots like Carl bot, by automating the part
of the process where we create the channel, while allowing the other bot to handle the menu operations by itself.
"""
import discord
from Backend import calendar_generator
import discord_tokens

"""discord_tokens is a file that contains the following variables:
bot_token, active_server_id, courses_text, category_id, all_channel_role"""

client = discord.Client(intents=discord.Intents.default())


def get_role_names():
    courses_text = discord_tokens.courses_text
    courses = calendar_generator.get_courses(courses_text)
    course_codes = list(courses.keys())
    course_codes.sort()
    return course_codes


async def get_roles(guild, role_names):
    roles = []
    for role_name in role_names:
        role = discord.utils.get(guild.roles, name=role_name)
        if not role:
            role = await guild.create_role(name=role_name)
        roles.append(role)
    return roles


async def create_channels(guild, roles):
    all_channel_role = None
    if discord_tokens.all_channel_role:
        all_channel_role = guild.get_role(discord_tokens.all_channel_role)
    category = guild.get_channel(discord_tokens.category_id)
    channels = category.channels
    text_channels, announcement_channels, forum_channels = [], [], []
    for channel_type, channel_list in zip([discord.ChannelType.text, discord.ChannelType.news,
                                           discord.ChannelType.forum],
                                          [text_channels, announcement_channels, forum_channels]):
        for channel in channels:
            if channel.type == channel_type:
                channel_list.append(channel.name)

    async def create_channel(role, channel_list_and_creation_method_iterable):
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            role: discord.PermissionOverwrite(read_messages=True)
        }
        if all_channel_role:
            overwrites[all_channel_role] = discord.PermissionOverwrite(read_messages=True)
        role_name = role.name.lower()
        for channel_list, creation_method in channel_list_and_creation_method_iterable:
            if role_name not in channel_list:
                await creation_method(role_name, overwrites=overwrites, category=category)
            else:
                print(f"{creation_method.__name__} channel {role_name} already exists.")

    channel_list_and_creation_method_iterable = [(announcement_channels, guild.create_news_channel),
                                                 (forum_channels, guild.create_category_channel)]
    for role in roles:  # Gathering create channels got rate limited
        await create_channel(role, channel_list_and_creation_method_iterable)


@client.event
async def on_ready():
    guild = client.get_guild(discord_tokens.active_server_id)
    roles = await get_roles(guild, get_role_names())
    await create_channels(guild, roles, )
    await client.close()


def main():
    client.run(discord_tokens.bot_token)


if __name__ == "__main__":
    main()
