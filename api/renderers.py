import vobject

from django.conf import settings

from rest_framework import renderers


class vCardRenderer(renderers.BaseRenderer):
    media_type = "text/x-vcard"
    format = "vcf"

    def render(self, data, accepted_media_type=None, renderer_context=None):
        vCard = vobject.vCard()
        vCard.add("FN").value = "Firefox Relay"
        # TODO: fix static urls
        photo_url = settings.SITE_ORIGIN + "/static/images/relay-logo.svg"
        vCard.add("PHOTO").value = photo_url
        vCard.add("LOGO").value = photo_url
        vCard.add("EMAIL").value = "support@relay.firefox.com"
        vCard.add("tel")
        vCard.tel.value = data.get("number", "")
        return vCard.serialize().encode()