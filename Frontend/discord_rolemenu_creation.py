"""
This module interfaces with Discord to create:
1) A set of cosmetic roles in the bot's server based on the course list given,
2) Empty private channels for the corresponding subject roles, and
3) A message that we can copy-paste as the rolemenu message.
This bot is only intended to work as a complement of other rolemenu creation bots like Carl bot, by automating the part
of the process where we create the channel, while allowing the other bot to handle the menu operations by itself.
"""
import asyncio

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


def filter_role_names(role_names, guild):
    existing_roles = [role.name for role in guild.roles]
    return [role_name for role_name in role_names if role_name not in existing_roles]


def create_roles(guild, role_names):
    return asyncio.gather(*[guild.create_role(name=role_name) for role_name in role_names])


def create_channels(guild, roles):
    all_channel_role = None
    if discord_tokens.all_channel_role:
        all_channel_role = guild.get_role(discord_tokens.all_channel_role)
    category = guild.get_channel(discord_tokens.category_id)

    async def create_channel(role):
        overwrites = {
            guild.default_role: discord.PermissionOverwrite(read_messages=False),
            role: discord.PermissionOverwrite(read_messages=True)
        }
        if all_channel_role:
            overwrites[all_channel_role] = discord.PermissionOverwrite(read_messages=True)
        try:
            await guild.create_text_channel(role.name, overwrites=overwrites, category=category)
        except discord.errors.HTTPException:
            print(f"Failed to create channel for role {role.name}")
    asyncio.gather(*[create_channel(role) for role in roles])


@client.event
async def on_ready():
    role_names = get_role_names()
    guild = client.get_guild(discord_tokens.active_server_id)
    role_names = filter_role_names(role_names, guild)
    roles = create_roles(guild, role_names)
    create_channels(guild, roles)
    await client.close()


def main():
    client.run(discord_tokens.bot_token)


if __name__ == "__main__":
    main()
