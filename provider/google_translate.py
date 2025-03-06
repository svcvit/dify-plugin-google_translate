from typing import Any

from dify_plugin import ToolProvider
from dify_plugin.errors.tool import ToolProviderCredentialValidationError
from tools.google_translate import GoogleTranslateTool

class GoogleTranslateProvider(ToolProvider):
    def _validate_credentials(self, credentials: dict[str, Any]) -> None:
        try:
            for _ in GoogleTranslateTool.from_credentials(credentials).invoke(
                tool_parameters={"content": "这是一段测试文本","dest": "en"}):
                pass
        except Exception as e:
            raise ToolProviderCredentialValidationError(str(e))
