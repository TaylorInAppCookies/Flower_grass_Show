from wechatpy import WeChatComponent
from wechatpy.utils import check_signature
from wechatpy.exceptions import InvalidSignatureException

app_id = ""
app_secret = ""
component_token = ""
encoding_aes_key = ""
component = WeChatComponent(app_id, app_secret, component_token, encoding_aes_key)


