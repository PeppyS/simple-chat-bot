from abc import ABC, abstractmethod


class ChatProvider(ABC):
    @abstractmethod
    def send_message(self, message: str) -> None:
        pass
