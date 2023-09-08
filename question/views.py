from rest_framework.decorators import api_view
from rest_framework.response import Response
import openai
import json
from .serializers import QuestionSerializer
import re

api_key = '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'
openai.api_key = api_key

@api_view(['POST'])
def generate_question(request):
   
    topic = request.data.get('topic', '') 
    user_message1 = f"give me random one question about {topic}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": user_message1}
        ]
    )

    assistant_reply1 = response['choices'][0]['message']['content']

    print(assistant_reply1)

    user_message2 = f"give me solution of question {assistant_reply1} using just and only number not the full phrase alaways"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": user_message2}
        ]
    )

    assistant_reply2 = response['choices'][0]['message']['content']

    # Extract the solution from assistant_reply2
    if "solution" in assistant_reply2:
        solution_match = re.search(r'\d+', assistant_reply2)
        if solution_match:
            assistant_reply2 = solution_match.group()
        else:
            # If no numbers found, you can set a default value or handle the situation accordingly.
            assistant_reply2 = "0"  # Default to 0

    print(assistant_reply2)

    user_message3 = f"give me five random and different choices of the response number of this question {assistant_reply1}"

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": user_message3}
        ]
    )

    assistant_reply3 = response['choices'][0]['message']['content']

    print(assistant_reply3)

    data = {
        "question": assistant_reply1,
        "choices": assistant_reply3,
        "solution": assistant_reply2
    }
    serializer = QuestionSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
    return Response(data)