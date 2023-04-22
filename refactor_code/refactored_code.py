
def check_sentence(sentence):
    print(f"split the sentence with blank and check the size: {sentence.split(' ')}")

if __name__ == '__main__':
    example_text_1 = "I'am storyparks. I lived in korea."
    check_sentence(example_text_1)

    example_text_2 = "What's the clean code? I don't know what it should be."
    check_sentence(example_text_2)
