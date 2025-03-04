import asyncio
from googletrans import Translator, LANGUAGES

translator = Translator()

language = {
    "bn": "Bangla",
    "en": "English",
    "ko": "Korean",
    "fr": "French",
    "de": "German",
    "he": "Hebrew",
    "hi": "Hindi",
    "it": "Italian",
    "ja": "Japanese",
    'la': "Latin",
    "ms": "Malay",
    "ne": "Nepali",
    "ru": "Russian",
    "ar": "Arabic",
    "zh": "Chinese",
    "es": "Spanish"
}

allow = True  # variable to control correct language code input

while allow:  # checking if language code is valid
    user_code = input(
        f"Please input desired language code. To see the language code list, enter 'options': \n")

    if user_code == "options":  # showing language options
        print("Code : Language")  # Heading of language option menu
        for code, lang in language.items():
            print(f"{code} => {lang}")
        print()  # adding an empty space

    else:  # validating user input
        if user_code in language:
            print(f"You have selected {language[user_code]}")
            allow = False
        else:
            print("It's not a valid language code!")


async def translate_text(text, dest):
    try:
        result = await translator.translate(text, dest=dest)

        # printing translation
        print(f"\n{language[dest]} translation: {result.text}")
        # printing pronunciation
        print(f"Pronunciation: {result.pronunciation}")

        # checking if the source language is listed in the language dictionary and printing it
        source_language = LANGUAGES.get(result.src, "Unknown")
        print(f"Translated from: {source_language}")

    except Exception as e:
        print(f"Error occurred during translation: {e}")


async def main():
    while True:  # starting translation loop
        text = input(
            "\nWrite the text you want to translate: \nTo exit the program, write 'close'\n")

        if text.lower() == "close":  # exit program command
            print(f"\nHave a nice day!")
            break

        await translate_text(text, user_code)


if __name__ == "__main__":
    asyncio.run(main())