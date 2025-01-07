import openai
from django.http import JsonResponse
from django.db import connection
from dotenv import load_dotenv
import os

# Load environment variables (API key)
load_dotenv()

# Initialize OpenAI Client
client = openai.Client(api_key=os.getenv('OPENAI_API_KEY'))

def text_to_sql(request):
    user_query = request.GET.get('query')

    if not user_query:
        return JsonResponse({"error": "Query parameter is missing or empty"}, status=400)

    try:
        # Send the request to OpenAI to generate an SQL query
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",  # Or any other model that supports chat completions
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {"role": "user", "content": user_query},
            ],
        )

        # Extract the generated SQL query
        sql_query = response.choices[0].message.content.strip()

        # Validate if the response is a proper SQL query
        if not sql_query.lower().startswith("select"):
            return JsonResponse({"error": "The AI did not generate a valid SELECT query."}, status=400)

        # Validate and execute SQL query
        with connection.cursor() as cursor:
            cursor.execute(sql_query)
            results = cursor.fetchall()

        return JsonResponse({'query': sql_query, 'results': results})

    except Exception as e:
        return JsonResponse({"error": str(e)}, status=500)
