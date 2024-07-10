from anonymous_survery import AnonymousSurvery

language_survery = AnonymousSurvery('What language did you learn to speak first: ')

print("Enter `q` to exit")
while True:
    language_survery.show_question()
    answer = input()
    if answer == 'q':
        break

    language_survery.store_response(answer)

language_survery.show_results()