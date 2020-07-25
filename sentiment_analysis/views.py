from django.http import JsonResponse
from django.shortcuts import render
# Create your views here.
from sentiment_analysis.analysis import Analysis
from sentiment_analysis.models import Sentence
from django.views.decorators.csrf import csrf_exempt
import json

# A comment

@csrf_exempt
def sentimentResults(request):
    # sentence = request.POST.get("sentence", "")
    sentence = json.loads(request.body.decode('utf-8'))["sentence"]

    print(sentence)

    if sentence == "":
        return

    analysis = Analysis(sentence)

    q = Sentence()
    q.positive = analysis.positiveScore
    q.negative = analysis.negativeScore
    q.neutral = analysis.neutralScore
    q.overall = analysis.overall
    q.sentence = sentence
    q.save()

    return JsonResponse(
        {
            's': sentence,
            'pos': analysis.positiveScore,
            'neg': analysis.negativeScore,
            'neu': analysis.neutralScore,
            'ova': analysis.overall.capitalize(),
        }
    )
