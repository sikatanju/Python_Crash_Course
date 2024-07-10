class AnonymousSurvery:
    def __init__(self, question):
        self.question = question
        self.responses = []
        
    def show_question(self):
        print(self.question, end='')

    def store_response(self, response):
        self.responses.append(response)

    def show_results(self):
        print("Survey Results: ")
        for response in self.responses:
            print(f' - {response}')
    