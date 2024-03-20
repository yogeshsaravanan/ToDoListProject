from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
from .models import ChatBot
from .forms import ChatBotForm
from django.contrib import messages
from django.contrib.auth.decorators import login_required
import numpy as np

from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.sequence import pad_sequences

import os
import pickle

model = load_model(r'C:\e\Taskmate_running\ToDoListProject\ChatBot\trained_model.h5')

with open(r'C:\e\Taskmate_running\ToDoListProject\ChatBot\tokenizer.pkl', 'rb') as f:
    tokenizer = pickle.load(f)

def generate_suggestions(user_input,top_n=5):
    # Preprocess user input
    tokenized_input = tokenizer.texts_to_sequences([user_input])
    tokenized_input = pad_sequences(tokenized_input, maxlen=50)
    predictions = model.predict(tokenized_input)
    top_n_indices = np.argsort(predictions[0])[-top_n:][::-1]
    suggestions = [tokenizer.index_word[index] for index in top_n_indices]
    return suggestions

@login_required
def chatbot(request):
    if request.method =="POST":
        form = ChatBotForm(request.POST or None)
        if form.is_valid:
            prompt = request.POST['prompt']
            generated_value = generate_suggestions(prompt)
        return render(request, 'chatbot.html', {'generated_value': generated_value})
    else:
        prompt = ChatBot.objects.filter(manage=request.user)
        context = {'welcome_text':'welcome to checklist','prompt':prompt}
        return render(request,'chatbot.html',context)