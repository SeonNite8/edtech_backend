from django.shortcuts import render
from django.http import JsonResponse

def index(request):
    return render(request, 'chatbot/index.html')

def get_response(request):
    if request.method == 'POST':
        user_message = request.POST.get('user_message')
        bot_response = get_bot_response(user_message)
        return JsonResponse({'bot_response': bot_response})
    else:
        return JsonResponse({'error': 'Invalid request method'})

def get_bot_response(user_message):
    user_message = user_message.lower()

    if 'hello' in user_message:
        return 'Hello! How can I assist you today?'

    elif 'help' in user_message or 'assist' in user_message:
        return 'I can help you with topics like math, science, history, and more. What do you need assistance with?'

    elif 'math' in user_message:
        return 'Sure, I can help with math! What specifically would you like to learn about?'

    elif 'science' in user_message:
        return 'Science is fascinating! Are you interested in biology, chemistry, physics, or another branch of science?'

    elif 'history' in user_message:
        return 'History is full of interesting stories! What historical period or event are you curious about?'

    elif 'bye' in user_message or 'goodbye' in user_message:
        return 'Goodbye! Feel free to come back if you have more questions.'
    
    elif 'subscription' in user_message:
        return 'Sure! Here is a <a href="D:\Website\edtech_backend\chatbot\templates\chatbot\subscription.html">link</a> for you.'

    else:
        return "I'm sorry, I'm not sure how to help with that. Can you please ask another question or phrase it differently?"