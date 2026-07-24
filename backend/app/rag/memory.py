from collections import defaultdict


class ConversationMemory:

    _memory = defaultdict(list)

    @classmethod
    def add_message(
        cls,
        user_id: int,
        role: str,
        content: str
    ):
        cls._memory[user_id].append(
            {
                "role": role,
                "content": content
            }
        )

        # Keep only last 10 messages
        cls._memory[user_id] = cls._memory[user_id][-10:]

    @classmethod
    def get_history(
        cls,
        user_id: int
    ) -> str:

        history = cls._memory[user_id]

        if not history:
            return ""

        return "\n".join(
            f"{item['role']}: {item['content']}"
            for item in history
        )

    @classmethod
    def clear(
        cls,
        user_id: int
    ):
        cls._memory[user_id] = []