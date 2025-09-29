from translate_text_list import translate_text_list, translate_text

# Dummy client to avoid real API calls
class DummyResp:
    def __init__(self, content):
        self.content = content

class DummyChoice:
    def __init__(self, message_content):
        self.message = type("M", (), {"content": message_content})

class DummyClient:
    class chat:
        class completions:
            @staticmethod
            def create(**kwargs):
                text = kwargs['messages'][1]['content']
                # Simplified fake translation
                if "Hello" in text:
                    return type("Resp", (), {"choices": [DummyChoice("Xin chào")]})
                elif "I am Peter" in text:
                    return type("Resp", (), {"choices": [DummyChoice("Tôi tên là Peter")]})
                else:
                    return type("Resp", (), {"choices": [DummyChoice("Translated")]})

def test_translate_text_list():
    fake_client = DummyClient()
    result = translate_text_list(["Hello", "I am Peter"], "vi", client=fake_client)
    assert result == ["Xin chào", "Tôi tên là Peter"]
