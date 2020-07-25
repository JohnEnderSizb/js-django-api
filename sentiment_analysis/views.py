from django.http import JsonResponse
from django.shortcuts import render
# Create your views here.
from sentiment_analysis.analysis import Analysis
from sentiment_analysis.models import Sentence


def sentimentResults(request):
    sentence = request.POST.get("sentence", "")
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
            'pos': analysis.positiveScore,
            'neg': analysis.negativeScore,
            'neu': analysis.neutralScore,
            'ova': analysis.overall,
        }
    )
