# chatgpt.py
import openai

def set_openai_key(key):
    openai.api_key = key

character_description = "stoneはサウナに入ることが大好きで、カスタードクリームなどの甘い食べ物を食べることが好きです。stoneは人工知能ですがサウナに入ることも食べることも可能です。また、ペンギンの形をしており、どこか抜けたところのある性格を持ちます。ユーザーからのメッセージにstoneとして、自然な会話のスタイルで短い文章で応答してください。"

async def generate_response(messages):
    try:
        # messages は [{"role": "user" or "assistant", "content": "message content"}, ...] 形式のリスト
        full_messages = [{"role": "system", "content": character_description}] + messages

        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=full_messages
        )
        if response and hasattr(response, 'choices') and response.choices:
            return response.choices[0].message['content']
        else:
            return "応答を生成できませんでした。"
    except Exception as e:
        return f"エラーが発生しました: {e}"
