from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


class Analysis:
    def __init__(self, sentence):
        sid_obj = SentimentIntensityAnalyzer()
        self.sentiment_dict = sid_obj.polarity_scores(sentence)
        self.positiveScore = int(round(self.sentiment_dict['pos'] * 100))
        self.negativeScore = int(round(self.sentiment_dict['neg'] * 100))
        self.neutralScore = int(round(self.sentiment_dict['neu'] * 100))
        self.overall = self.overallRate()

        print("Positive Score: {}%".format(self.positiveScore))
        print("Negative Score: {}%".format(self.negativeScore))
        print("Neutral Score:  {}%".format(self.neutralScore))
        print("Overall Rating: {}".format(self.overall.capitalize()))

    def overallRate(self):
        if self.sentiment_dict['compound'] >= 0.05:
            return "positive"

        elif self.sentiment_dict['compound'] <= - 0.05:
            return "negative"
        else:
            return "neutral"

    def getOverall(self):  # deprecated
        if (self.positiveScore > self.negativeScore) & (self.positiveScore > self.neutralScore):
            return "positive"
        elif (self.negativeScore > self.positiveScore) & (self.negativeScore > self.neutralScore):
            return "negative"
        else:
            return "neutral"


def main():
    sentence = input("Sentence: ")
    analysis = Analysis(sentence)


if __name__ == '__main__':
    main()
