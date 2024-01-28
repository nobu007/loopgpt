import os
import sys
import time
from typing import *

import tiktoken
from loopgpt.logger import logger
from loopgpt.models.base import BaseModel
from loopgpt.utils.openai_key import get_openai_key

# commonモジュールをインポートする
COMMON_MOD_DIR = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "../../../../common")
)
print("COMMON_MOD_DIR=", COMMON_MOD_DIR)
sys.path.append(COMMON_MOD_DIR)


from yka_langchain import yka_langchain_raw


class YkaLlmModel(BaseModel):
    def __init__(self, model: str = "gpt-3.5-turbo", api_key: Optional[str] = None):
        self.model = model
        self.api_key = api_key

    def chat(
        self,
        messages: List[Dict[str, str]],
        max_tokens: Optional[int] = None,
        temperature: float = 0.8,
    ) -> str:
        api_key = get_openai_key(self.api_key)
        num_retries = 3
        for i in range(num_retries):
            try:
                resp = yka_langchain_raw(messages, is_chat=True)
                return resp

            except Exception as e:
                logger.warn("Rate limit exceeded. Retrying after 20 seconds.")
                time.sleep(20)
                if i == num_retries - 1:
                    raise

    def count_tokens(self, messages: List[Dict[str, str]]) -> int:
        tokens_per_message, tokens_per_name = (4, -1)
        enc = tiktoken.encoding_for_model(self.model)
        num_tokens = 0
        for message in messages:
            num_tokens += tokens_per_message
            for key, value in message.items():
                num_tokens += len(enc.encode(value))
                if key == "name":
                    num_tokens += tokens_per_name
        num_tokens += 3
        return num_tokens

    def get_token_limit(self) -> int:
        return 4000

    def config(self):
        cfg = super().config()
        cfg.update(
            {
                "model": self.model,
                "api_key": self.api_key,
            }
        )
        return cfg

    @classmethod
    def from_config(cls, config):
        return cls(config["model"], config.get("api_key"))
