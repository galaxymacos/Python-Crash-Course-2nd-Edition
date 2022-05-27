class AnonymousSurvey:

    def __init__(self, question):
        self.question = question
        self.responses = []

    def show_question(self):
        print(self.question)

    def store_response(self, *new_responses):
        for response in new_responses:
            self.responses.append(response)

    def show_results(self):
        print("Survey results:")
        for response in self.responses:
            print(response)
