class ChatEventHandler:
    def __init__(self, consumer):
        self.consumer = consumer

    def get_handler(self, event):
        return getattr(self, f'on_{event}', None)

    # event 별로 해당 on이 prefix 로 붙은 handler 의 메서드가 실행 됨
    def on_(self, data):
        pass