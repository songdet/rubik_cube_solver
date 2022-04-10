
# Informal interface for communication
class Communication:

    def readline(self) -> bytes:
        # Block read data until a newline is received
        raise NotImplementedError("Subclass needs to implement readline")

    def write(self, data: bytes):
        # Write data to underlying communication channel
        raise NotImplementedError("Subclass needs to implement write")
