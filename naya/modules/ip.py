"""
CREDITS XTSEA RENDAY
"""

import base64
from base64 import b64decode as kc

import aiohttp
import requests
from pyrogram import filters

from . import *


@bots.on_message(filters.command("ip", cmd) & filters.me)
async def hacker_lacak_target(client, message):
    apikey = kc("M0QwN0UyRUFBRjU1OTQwQUY0NDczNEMzRjJBQzdDMUE=").decode("utf-8")
    ran = await eor(message, "<code>Processing...</code>")
    ipddres = message.text.split(None, 1)[1] if len(message.command) != 1 else None
    if not ipddres:
        await ran.edit("Example: <code>+ip your ip address here : 1592.401.xxx</code>")
        return

    if not apikey:
        await ran.edit("Missing APIKEY.")
        return

    location_link = "https"
    location_api = "api.ip2location.io"
    location_key = f"key={apikey}"
    location_search = f"ip={ipddres}"
    location_param = (
        f"{location_link}://{location_api}/?{location_key}&{location_search}"
    )
    response = requests.get(location_param)
    if response.status_code == 200:
        data_location = response.json()
        try:
            location_ip = data_location["ip"]
            location_code = data_location["country_code"]
            location_name = data_location["country_name"]
            location_region = data_location["region_name"]
            location_city = data_location["city_name"]
            location_zip = data_location["zip_code"]
            location_zone = data_location["time_zone"]
            location_card = data_location["as"]
        except Exception as e:
            await ran.edit_text(f"Error request {e}")
            return
        if (
            location_ip
            and location_code
            and location_name
            and location_region
            and location_city
            and location_zip
            and location_zone
            and location_card
        ):
            location_target = ""
            location_target += f"<b>IP Address:</b> {location_ip}\n"
            location_target += f"<b>Country code:</b> {location_code}\n"
            location_target += f"<b>Country name:</b> {location_name}\n"
            location_target += f"<b>Region name:</b> {location_region}\n"
            location_target += f"<b>City name:</b> {location_city}\n"
            location_target += f"<b>Zip code:</b> {location_zip}\n"
            location_target += f"<b>Time Zone:</b> {location_zone}\n"
            location_target += f"<b>Data card:</b> {location_card}\n"
            await ran.edit(location_target)
        else:
            await ran.edit("Not data ip address")
    else:
        await ran.edit(
            "Sorry, there was an error processing your request. Please try again later"
        )


@bots.on_message(filters.command("ipd", cmd) & filters.me)
async def whois_domain_target(client, message):
    apikey = base64.b64decode("M0QwN0UyRUFBRjU1OTQwQUY0NDczNEMzRjJBQzdDMUE=").decode(
        "utf-8"
    )
    ran = await eor(message, "<code>Processing...</code>")
    domain_text = message.text.split(None, 1)[1] if len(message.command) != 1 else None
    if not domain_text:
        await ran.edit("Example: <code>+ip your ip address here : 1592.401.xxx</code>")
        return

    if not apikey:
        await ran.edit("Missing apikey ip domain")
        return

    url_api_domain = f"https://api.ip2whois.com/v2?key={apikey}&domain={domain_text}"
    whois_domain = ""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url_api_domain) as response:
                if response.status == 200:
                    data_domain = await response.json()
                    domain_domain = data_domain.get("domain")
                    domain_domainid = data_domain.get("domain_id")
                    domain_status = data_domain.get("status")
                    domain_create_date = data_domain.get("create_date")
                    domain_update_date = data_domain.get("update_date")
                    domain_expire_date = data_domain.get("expire_date")
                    domain_ages = data_domain.get("domain_age")
                    domain_server = data_domain.get("whois_server")
                    domain_name = data_domain.get("name")
                    domain_organization = data_domain.get("organization")
                    domain_addres = data_domain.get("street_address")
                    domain_city = data_domain.get("city")
                    domain_region = data_domain.get("region")
                    domain_country = data_domain.get("country")
                    domain_email = data_domain.get("email")
                    domain_zip = data_domain.get("zip_code")
                    domain_phone = data_domain.get("phone")
                    domain_nameservers = data_domain.get("nameservers")

                    if (
                        domain_domain
                        and domain_domainid
                        and domain_status
                        and domain_create_date
                        and domain_update_date
                        and domain_expire_date
                        and domain_ages
                        and domain_server
                        and domain_name
                        and domain_organization
                        and domain_addres
                        and domain_city
                        and domain_region
                        and domain_country
                        and domain_email
                        and domain_zip
                        and domain_phone
                        and domain_nameservers
                    ):
                        whois_domain += f"<b>Domain:</b> {domain_domain}\n"
                        whois_domain += f"<b>Domain ID:</b> {domain_domainid}\n"
                        whois_domain += f"<b>Status:</b> {domain_status}\n"
                        whois_domain += f"<b>Create date:</b> {domain_create_date}\n"
                        whois_domain += f"<b>Update date:</b> {domain_update_date}\n"
                        whois_domain += f"<b>Expire date:</b> {domain_expire_date}\n"
                        whois_domain += f"<b>Age:</b> {domain_ages}\n"
                        whois_domain += f"<b>Whois_server:</b> {domain_server}\n"
                        whois_domain += f"<b>Name:</b> {domain_name}\n"
                        whois_domain += f"<b>Organization:</b> {domain_organization}\n"
                        whois_domain += f"<b>Street address:</b> {domain_addres}\n"
                        whois_domain += f"<b>City:</b> {domain_city}\n"
                        whois_domain += f"<b>Region:</b> {domain_region}\n"
                        await ran.edit(whois_domain)
                    else:
                        await ran.edit("No data for this domain.")
                else:
                    await ran.edit("Error: could not fetch WHOIS information.")
    except Exception as e:
        await ran.edit(f"Error: {str(e)}")


__MODULE__ = "ipsearch"
__HELP__ = f"""
✘ Bantuan Untuk IP Search

๏ Perintah: <code>{cmd}ip</code> [ip host]
◉ Penjelasan: Untuk mencari lokasi ip addres.

๏ Perintah: <code>{cmd}ipd</code> [ip domain]
◉ Penjelasan: Untuk mencari lokasi ip domain.
"""
